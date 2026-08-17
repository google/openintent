# Vendor-neutral Wi-Fi survey measurements

## Problem

OpenIntent can currently describe a survey path and associate it with a PCAP,
but it cannot represent the most common survey result directly: a BSSID, RSSI,
frequency, time, and position. Consequently, two conforming implementations can
exchange the floorplan and trajectory while still being unable to exchange the
measurements used to calculate coverage.

A PCAP reference is valuable, but it is not a complete interoperability model:

* many mobile operating systems expose structured scan results without raw
  802.11 frames;
* packet capture metadata and RSSI availability differ between adapters and
  capture formats;
* a packet capture does not define the indoor position of a received frame;
* consumers should not have to reproduce a vendor-specific scan-window
  algorithm to obtain the observations that the producer used; and
* raw captures can be much larger than the normalized observations required by
  planning, validation, and visualization tools.

This extension makes normalized observations interoperable while retaining raw
captures as optional evidence and as a source for future reprocessing.

For example, Android's public
[`ScanResult`](https://developer.android.com/reference/android/net/wifi/ScanResult)
model exposes BSSID, RSSI in dBm, frequency, microsecond timestamps, channel
geometry, security types, information elements, and Wi-Fi 7 MLO identity. A
portable survey model should be able to preserve those results without requiring
a packet capture that the platform does not provide.

## Design goals

The model is intended to:

1. represent stop-and-go and continuous passive Wi-Fi surveys;
2. preserve the measured RSSI for each BSS, including 2.4, 5, and 6 GHz BSSs;
3. bind every usable observation to a time and an indoor position;
4. record enough collector provenance to compare measurements responsibly;
5. work for platform scan APIs, monitor-mode captures, and vendor APIs;
6. support small inline projects and large externally stored datasets; and
7. remain backward compatible with existing `survey_path` documents.

The first version deliberately does not standardize spectrum traces, active
throughput/latency tests, derived heatmaps, interpolation algorithms beyond
trajectory positioning, or a project archive/container. Those can be added as
separate profiles without changing the Wi-Fi observation core.

## Logical model

The model has four layers:

```text
floorplan
  survey_path (time origin, trajectory, collection provenance)
    path_point[] (position over time)
    scan_event[] (one scan result set)
      wifi_observation[] (one observed BSS)
    data_resource[] (optional raw or high-volume payloads)
```

`survey_path` remains the aggregate associated with a floorplan. A
`scan_event` preserves the collection boundary instead of flattening all BSS
records into an unordered list. This matters because scanning is not
instantaneous, scan results can be incomplete, and one scan result set is the
natural unit returned by many platform APIs.

`wifi_observation` identifies a BSS by BSSID and carries the observed RSSI and
primary channel frequency. SSID, PHY type, security mode, channel geometry,
noise, SNR, MLO identity, and raw information elements are optional because
collector capabilities vary. BSSID is used rather than SSID because multiple
BSSs can advertise the same SSID and their RSSI values must not be conflated.

## Time representation

New survey data uses an RFC 3339 `survey_path.start_time` as an absolute time
anchor and non-negative integer microsecond offsets within the path. This avoids
the precision loss caused by representing a large Unix epoch plus sub-second
precision as one JSON number. This follows the interoperability guidance in
[RFC 8259, section 6](https://www.rfc-editor.org/rfc/rfc8259#section-6), which
notes that commonly used binary64 implementations limit exact numeric
interchange.

The existing floating-point `path_point.timestamp` remains valid for backward
compatibility, but it is deprecated for new producers. When both forms are
present, the integer offset is authoritative.

An observation can have its own `observed_offset_us`. If it is absent, the
parent `scan_event.started_offset_us` applies. This permits both snapshot-style
platform results and frame-derived observations with distinct receive times.

## Position representation

A scan event obtains its position in one of two ways:

* it contains `coordinate`; or
* the path declares `position_interpolation: LINEAR_BY_TIME`, and the position
  is linearly interpolated between the adjacent time-referenced path points.

With `position_interpolation: NONE`, every scan event must contain `coordinate`.
With `LINEAR_BY_TIME`, every path point must contain `coordinate` and
`time_offset_us`. Interpolation must use coordinates with the same unit and
coordinate system. A consumer must not interpolate across an `END` to `START`
path discontinuity.

For a stop-and-go survey, producers are encouraged to store the coordinate on
each scan event even when matching point-path entries are also present. For a
continuous survey, time-based path interpolation avoids duplicating a coordinate
for every BSS observation.

## Collector provenance and RSSI

RSSI values are device-dependent. `survey_device` and `survey_wifi_adapter`
therefore record the hardware, software, driver, firmware, and optional
calibration information that produced the values.

`scan_event.adapter_identifier` associates a result set with the adapter that
produced it. It should be present whenever a survey device declares more than
one adapter. Simultaneous result sets from different adapters remain separate
scan events even when their time windows overlap.

`wifi_observation.rssi_dbm` is the collector-reported value after applying
`rssi_calibration_offset_db`, if an offset is declared. For example, a raw value
of -67 dBm with an offset of +2 dB is stored as -65 dBm. This convention lets a
consumer compare the normalized values without silently applying an offset a
second time.

The schema does not impose an artificial RSSI range. Out-of-range values are
better preserved and flagged by an application than discarded during exchange.

When both `ssid` and `ssid_bytes_base64` are present, the raw byte value is
authoritative and `ssid` is its display representation.

## Inline observations and external resources

`scan_events` is the vendor-neutral, schema-defined interchange representation.
It is suitable for mobile surveys and modest datasets and is sufficient to
reconstruct point RSSI maps without a PCAP.

`data_resources` complements it with document-relative or absolute resources.
Typical roles include:

* `RAW_80211_CAPTURE` for PCAP or PCAPNG evidence;
* `WIFI_OBSERVATIONS` for a high-volume structured representation;
* `TRAJECTORY` for a higher-frequency positioning stream; and
* future `SPECTRUM` or `ACTIVE_MEASUREMENTS` profiles.

`media_type` describes the physical encoding. A vendor-neutral external
structured resource that is not defined by the OpenIntent schema also supplies
`schema_uri`; for example, an implementation can use JSON, CBOR, Apache Arrow,
or Parquet without making any of those encodings mandatory for all producers.
`sha256` and `byte_length` allow a portable project archive to verify that the
resource has not been substituted or truncated.

Raw and normalized forms may coexist. When they do, `scan_events` records the
measurements selected by the producer for analysis, while the raw resource is
the lossless source material. Consumers are not expected to regenerate
`scan_events` byte-for-byte from the raw resource because scan windowing and
platform filtering can differ.

## Minimum interoperability profile

A producer claiming support for OpenIntent Wi-Fi survey measurements should:

1. provide `survey_path.start_time` and at least one `scan_event`;
2. give each spatially usable scan event a direct coordinate or a position
   derivable by `LINEAR_BY_TIME` from time-referenced path points;
3. provide `bssid`, `rssi_dbm`, and `frequency_mhz` for every Wi-Fi observation;
4. use canonical lowercase colon-separated MAC addresses;
5. provide survey device and adapter provenance when it is known; and
6. use `data_resources.schema_uri` for external normalized records whose schema
   is not part of OpenIntent.

A raw capture alone remains a valid legacy survey path, but it does not claim
support for the normalized survey-measurement profile.

## Backward compatibility

All previously defined `survey_path` fields remain accepted. In particular,
`path_data_uri`, `path_data_type`, the flattened device fields, floating-point
timestamps, and PCAP-only paths remain valid.

Existing producers need no migration. New producers should use the structured
`survey_device`, `start_time` plus integer offsets, `scan_events`, and
`data_resources`. A producer may emit both legacy and new fields during a
transition; consumers that only understand the earlier model will ignore the
new properties under the current extensible schema policy.

## Privacy and security

Survey data can reveal precise indoor paths, device identifiers, network names,
BSSIDs, and raw management frames. Producers should minimize identifiers that
are not required for the exchange, obtain appropriate consent, and protect the
OpenIntent document and linked resources as sensitive operational data. A
resource digest provides integrity, not confidentiality or authenticity.
