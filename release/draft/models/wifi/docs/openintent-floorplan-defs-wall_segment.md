# Untitled object in undefined Schema

```txt
https://example.com/schema/floorplan#/$defs/wall_segment
```

Represents a line segment of a wall on a floorplan.  Each segment requires a start, and end and a description for the wall type.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [openintent-floorplan.schema.json\*](../out/openintent-floorplan.schema.json "open original schema") |

## wall\_segment Type

`object` ([Details](openintent-floorplan-defs-wall_segment.md))

# wall\_segment Properties

| Property                     | Type     | Required | Nullable       | Defined by                                                                                                                                                        |
| :--------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wall\_type](#wall_type)     | `string` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-wall_segment-properties-wall_type.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/wall_type") |
| [thickness](#thickness)      | `number` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-wall_segment-properties-thickness.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/thickness") |
| [height](#height)            | `number` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-wall_segment-properties-height.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/height")       |
| [start\_point](#start_point) | `object` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-wall_point.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/start_point")                      |
| [end\_point](#end_point)     | `object` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-wall_point.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/end_point")                        |

## wall\_type

Description of the wall type.

`wall_type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-wall_segment-properties-wall_type.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/wall_type")

### wall\_type Type

`string`

## thickness

thickness in meters of the wall.

`thickness`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-wall_segment-properties-thickness.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/thickness")

### thickness Type

`number`

## height

height of the wall in meters.

`height`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-wall_segment-properties-height.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/height")

### height Type

`number`

## start\_point

Two-dimensional coordinate of a wall point

`start_point`

*   is required

*   Type: `object` ([Details](openintent-floorplan-defs-wall_point.md))

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-wall_point.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/start_point")

### start\_point Type

`object` ([Details](openintent-floorplan-defs-wall_point.md))

## end\_point

Two-dimensional coordinate of a wall point

`end_point`

*   is required

*   Type: `object` ([Details](openintent-floorplan-defs-wall_point.md))

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-wall_point.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/end_point")

### end\_point Type

`object` ([Details](openintent-floorplan-defs-wall_point.md))
