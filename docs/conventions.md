# OpenIntent Schema Conventions

This document describes conventions for how the OpenIntent schemas are
written, and how payloads are expected to use them. These rules apply to
every model in the repo unless a schema says otherwise.

## Inclusion: include it with content, or don't include it

JSON Schema treats any property that is not listed in an object's
`required` array as optional. "Optional" means *omit the key entirely when
you have nothing to say* — it does not mean "include the key with an empty
value." If a key appears in a payload, the producer is asserting that it
carries meaningful data.

An empty placeholder (`{}`, `null`, `""`, `[]`) is ambiguous: a consumer
cannot tell the difference between "this object has no location" and "this
object's location is unknown and the producer emitted a stub." Omitting
the key is unambiguous, and it keeps consumers from having to write
defensive checks around every optional field.

### Example: coordinate

The `coordinate` object describes a location in one or both coordinate
systems: `coordinate_xyz` (cartesian, relative to the floorplan) and
`coordinate_lat_long` (geospatial). Both sub-objects are individually
optional — a location may be known in only one system — but at least one
must be present. The schema enforces this with `anyOf` over `required`:

```json
"coordinate": {
  "anyOf": [
    { "required": ["coordinate_xyz"] },
    { "required": ["coordinate_lat_long"] }
  ],
  "properties": {
    "coordinate_xyz": { "$ref": "#/$defs/coordinate_xyz" },
    "coordinate_lat_long": { "$ref": "#/$defs/coordinate_lat_long" }
  }
}
```

So the rule for any object that embeds a coordinate (access points,
switches, closets, buildings, reference markers, ...) is:

- If you include `coordinate`, it must include a coordinate — at least one
  of `coordinate_xyz` or `coordinate_lat_long`.
- If the location is unknown, do not include a `coordinate: {}`. Leave the
  `coordinate` key out entirely.

Correct:

```json
{
  "name": "AP-101",
  "coordinate": {
    "coordinate_xyz": { "x": 120, "y": 45, "unit": "pixels" }
  }
}
```

Also correct (location unknown — key omitted):

```json
{
  "name": "AP-101"
}
```

Invalid (empty stub — fails validation):

```json
{
  "name": "AP-101",
  "coordinate": {}
}
```

### Applying the rule elsewhere

The same pattern generalizes to every optional object in the schemas:

- Prefer omitting the key over emitting an empty object or array.
- When an optional object is only meaningful if at least one of its
  sub-fields is set, define it with `anyOf`/`required` (as `coordinate`
  does above) so "present but empty" is invalid by construction.
- For optional scalars, omit rather than sending `null` or an empty string
  as a placeholder.
