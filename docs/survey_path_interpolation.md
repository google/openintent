# Survey path interpolation

This document describes how the existing Wi-Fi model associates timestamped
measurements with positions along a `survey_path`. It clarifies the behavior of
`path_type`, `path_points`, and `path_indicator` without introducing new fields
or changing schema validation requirements.

Measurement data is referenced by `path_data_uri`. The path points describe
where the collector was at known times. A measurement timestamp and the path
point timestamps must use the same Unix epoch time reference, in seconds.
Fractional seconds may be used. A collector using another clock must map its
measurement times to that reference before they can be used for positioning.

## Path segments and coordinates

The ordered `path_points` array can contain multiple path segments. Each segment
starts with a point marked `START` and ends with a point marked `END`.
Intermediate points have no `path_indicator`.

Coordinates used together for interpolation must have a consistent coordinate
reference and units, matching the containing floor plan. The examples below use
local floor-plan `(x, y)` coordinates in meters; they are explanatory tables,
not additional serialized fields. The same interpolation formula applies to
`z` when it is supplied at both endpoints. Do not invent a missing coordinate
component or interpolate between different coordinate representations.

## Point surveys

For `path_type: POINT`, `START` and `END` have identical coordinates. They
bound the time spent collecting measurements at that position, rather than a
movement between two positions.

| Indicator | Unix timestamp (seconds) | Position (meters) |
| --- | --- | --- |
| START | 1700000000 | (10, 20) |
| END | 1700000010 | (10, 20) |

Measurements throughout this interval, including its endpoints, have position
`(10, 20)`. Another stop can be represented by another `START`–`END` segment.
Do not interpolate movement between stops.

## Continuous surveys

For `path_type: CONTINUOUS`, interpolate position linearly with respect to time
between consecutive timestamped path points within the same segment.

For endpoint positions `p0`, `p1`, endpoint times `t0`, `t1`, and a measurement
time `t`, where `t0 <= t <= t1` and `t1 > t0`:

```text
fraction = (t - t0) / (t1 - t0)
position = p0 + fraction * (p1 - p0)
```

Apply this formula to each available coordinate component. At an endpoint's
timestamp, use that endpoint's coordinate.

| Indicator | Unix timestamp (seconds) | Position (meters) |
| --- | --- | --- |
| START | 1700000000 | (10, 20) |
| — | 1700000010 | (20, 20) |
| END | 1700000030 | (20, 40) |

A measurement at `1700000005` has position `(15, 20)`. A measurement at
`1700000020` has position `(20, 30)`. Each uses its surrounding pair of points;
interpolating directly from `START` to `END` would incorrectly cut the corner.

This reconstructs position assuming constant velocity between each pair of
points. It does not claim that the collector actually moved at constant
velocity. Additional path points can capture turns, stops, and changes in
speed. The RSSI and other measurement values remain unchanged: interpolation
assigns a position, not a new signal value.

The declared `path_type` determines the survey mode. Matching first and last
coordinates alone do not imply `POINT`: a continuous route may return to its
starting position through intermediate points.

## Boundaries and unavailable positions

- Do not extrapolate before `START` or after `END`.
- Do not interpolate across an `END`–`START` gap, even if the surrounding points
  are adjacent in the array or refer to the same measurement file.
- Interpolation requires coordinates and timestamps at both bounding points
  and a positive time difference. Missing values or equal/reversed timestamps
  do not provide a valid interpolation interval.
- If the path does not determine an unambiguous position, leave the measurement
  unpositioned or report the ambiguity rather than assigning an arbitrary
  position. For example, overlapping segments can associate the same timestamp
  with different positions.

These are interpretation rules for consumers. The current schema does not
enforce all of the conditions needed to reconstruct a position. Measurements
without a determined position can still be retained in the external resource.
