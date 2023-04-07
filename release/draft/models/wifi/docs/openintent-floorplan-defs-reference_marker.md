# Untitled object in undefined Schema

```txt
https://example.com/schema/floorplan#/$defs/reference_marker
```

A reference marker to denote a location on the floorplan. Can be used to provide notes, or a translation between coordinate systems.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [openintent-floorplan.schema.json\*](../out/openintent-floorplan.schema.json "open original schema") |

## reference\_marker Type

`object` ([Details](openintent-floorplan-defs-reference_marker.md))

# reference\_marker Properties

| Property                                   | Type     | Required | Nullable       | Defined by                                                                                                                                                                          |
| :----------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [coordinate\_xyz](#coordinate_xyz)         | `object` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_xyz.md "https://example.com/schema/floorplan#/$defs/reference_marker/properties/coordinate_xyz")                             |
| [coordinate\_latlong](#coordinate_latlong) | `object` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_latlong.md "https://example.com/schema/floorplan#/$defs/reference_marker/properties/coordinate_latlong")                     |
| [reference\_text](#reference_text)         | `string` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-reference_marker-properties-reference_text.md "https://example.com/schema/floorplan#/$defs/reference_marker/properties/reference_text") |

## coordinate\_xyz

A coordinate that references cartesian coordinates using x,y,z and/or a geospatial coordinate using lat/long

`coordinate_xyz`

*   is optional

*   Type: `object` ([Details](openintent-floorplan-defs-coordinate_xyz.md))

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_xyz.md "https://example.com/schema/floorplan#/$defs/reference_marker/properties/coordinate_xyz")

### coordinate\_xyz Type

`object` ([Details](openintent-floorplan-defs-coordinate_xyz.md))

## coordinate\_latlong

A coordinate that references geospatial coordinates using using lat/long and altitude

`coordinate_latlong`

*   is optional

*   Type: `object` ([Details](openintent-floorplan-defs-coordinate_latlong.md))

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_latlong.md "https://example.com/schema/floorplan#/$defs/reference_marker/properties/coordinate_latlong")

### coordinate\_latlong Type

`object` ([Details](openintent-floorplan-defs-coordinate_latlong.md))

## reference\_text

text string from reference

`reference_text`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-reference_marker-properties-reference_text.md "https://example.com/schema/floorplan#/$defs/reference_marker/properties/reference_text")

### reference\_text Type

`string`
