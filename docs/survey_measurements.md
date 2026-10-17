# External Wi-Fi survey measurements (proposal)

This proposal defines a small shared model for passive Wi-Fi scan results and
an initial JSON representation. Dense measurements live outside the main
OpenIntent Wi-Fi project and are referenced through the existing
`survey_path.path_data_uri` field.

The released Wi-Fi schema is unchanged. The proposal lives under
[`proposals/wifi-survey`](../proposals/wifi-survey/) with its own draft version
`0.1.0`; this is not a new released OpenIntent project version.

## Project and measurement resource

The project owns floor plans, path points, timestamps, and the existing
`host_device_*` and `survey_device_*` metadata. The host is the controlling
computer or phone; the survey device is the measurement adapter or chipset.
Only report device details that the collector actually exposes.

The external document owns `scan_events`, each containing `wifi_observations`.
Each resource represents one survey device. A project using multiple devices
uses separate resources and survey paths so observations cannot be attributed
to the wrong device merely because their timestamps match.

Use the existing `path_data_type: OTHER` for this proposal. The external
document identifies itself with `survey_format: openintent-wifi-survey` and
`survey_version: 0.1.0`. A consumer must inspect and support that format/version
before interpreting it; `OTHER` alone is not a format discriminator.

The existing URI constraint remains unchanged. The example uses an absolute
HTTPS URI on `example.org` as a placeholder, not a hosted resource. A local
consumer can explicitly map that URI to the supplied example file. Archive
packaging, relative URI support, fetching, and resource discovery are separate
concerns, not requirements of this proposal.

Multiple survey paths may reference the same resource, as they can with PCAP.
For each path, consider observation timestamps within its START–END intervals.
Do not assume that the entire resource belongs to every referencing path.
Resource sharing does not merge devices or coordinate systems.

## Scan events and observations

A scan event preserves one collector result set. Its required `timestamp` is
the time when that result set became available to the collector. A result set
does not imply that all channels were visited, that every BSS was found, or
that all observations were made simultaneously. An empty array means no
observations were supplied; it does not prove that no Wi-Fi signal was present.

Each observation requires:

| Field | Meaning |
| --- | --- |
| `bssid` | Lowercase colon-separated BSSID |
| `rssi_dbm` | Unmodified collector-reported RSSI in dBm |
| `frequency_mhz` | Primary channel center frequency in MHz |

An observation can also include its own `timestamp`, losslessly representable
`ssid`, and collector-reported `noise_dbm` or `snr_db`. Missing optional fields
mean unavailable, not zero. Use omission rather than `null`. Do not infer
noise from RSSI or populate unavailable values with sentinel numbers.

“Unmodified” refers to the value exposed by the measurement API or driver, not
raw RF samples. Exporters must not apply compensation or averaging to these
values. Visualization and subsequent processing can use separate settings.

The schema intentionally permits additional properties for experimentation.
Consumers must not rely on unknown properties to interpret the defined core.
Future incompatible changes require a different survey version; permissive
JSON validation is not a promise of semantic compatibility.

## Time and position

All timestamps use the existing Unix epoch seconds representation, allowing
fractional seconds. There is no new time origin, relative offset system, or
deprecation of `path_point.timestamp`. Numeric precision is not a guarantee of
measurement clock accuracy. Producers must map any monotonic device clock to
the epoch time reference used by the path.

Use the observation's timestamp when present. Otherwise, use the scan event
timestamp as an explicitly approximate positioning time. This fallback is
useful when a platform supplies only result-set timing; it must not be
interpreted as an exact reception time. Consumers requiring precise timing
can leave such observations unpositioned.

Cached observations may predate the result set or the current path interval.
Preserve known observation timestamps instead of replacing them with delivery
time. A cached observation outside the path interval must not be moved to a
path endpoint or positioned using the newer event timestamp.

The existing path determines position: POINT segments hold a fixed coordinate;
CONTINUOUS segments interpolate linearly by time between consecutive points.
Do not interpolate across END–START gaps or extrapolate beyond a segment.
See the separate [interpolation documentation PR](https://github.com/google/openintent/pull/30)
for examples and boundary handling. Coordinates are not duplicated per scan.
An observation without an unambiguous path position remains in the external
resource without an assigned position.

## Initial JSON representation

The YAML source is
[`openintent-wifi-survey.yaml`](../proposals/wifi-survey/src/openintent-wifi-survey.yaml).
Its generated JSON Schema is
[`oi-wifi-survey.schema.json`](../proposals/wifi-survey/oi-wifi-survey.schema.json).
Examples are provided as a pair:

- [Wi-Fi project](../proposals/wifi-survey/examples/project.json)
- [External measurements](../proposals/wifi-survey/examples/measurements.json)

In these examples, the first observation was received at `1700000005` and
maps to `(15, 20)`, although its result set arrived one second later. The
second observation is cached from before START and remains unpositioned. The
last observation has no individual timestamp and uses result-set time
`1700000020` for the approximate position `(20, 30)`.

JSON Schema checks structure and field types. It does not verify clock
synchronization, path membership, device identity across files, or the physical
plausibility of radio readings. Those require consumer-side semantic checks.

This JSON representation makes the initial model concrete and reviewable. It
is not a requirement to use JSON for every dataset size. Additional encodings
can be proposed with explicit mappings that preserve units, time semantics,
missing values, device association, and scan grouping. This proposal specifies
no binary encoding or performance claim.

## Scope and open questions

The initial core excludes compensation, active tests, spectrum data, derived
heatmaps, raw frame storage, security/PHY normalization, and MLO-specific
metadata. These can be discussed as extensions after the core is agreed.

Review feedback is particularly useful on the observation-time fallback, the
one-device-per-resource boundary, and whether a future dedicated
`path_data_type` should replace `OTHER` for discovery.

Run the focused validation with Python, PyYAML, and jsonschema installed:

```sh
python3 proposals/wifi-survey/validate.py
```
