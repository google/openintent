# Untitled object in undefined Schema

```txt
https://example.com/schema/floorplan
```

representation of an floorplan

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [openintent-floorplan.schema.json](../out/openintent-floorplan.schema.json "open original schema") |

## Untitled object in undefined Type

`object` ([Details](openintent-floorplan.md))

# Untitled object in undefined Properties

| Property                                 | Type     | Required | Nullable       | Defined by                                                                                                                                   |
| :--------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                            | `string` | Required | cannot be null | [Untitled schema](openintent-floorplan-properties-name.md "https://example.com/schema/floorplan#/properties/name")                           |
| [vendor\_id](#vendor_id)                 | `string` | Optional | cannot be null | [Untitled schema](openintent-floorplan-properties-vendor_id.md "https://example.com/schema/floorplan#/properties/vendor_id")                 |
| [map\_url](#map_url)                     | `string` | Optional | cannot be null | [Untitled schema](openintent-floorplan-properties-map_url.md "https://example.com/schema/floorplan#/properties/map_url")                     |
| [project\_name](#project_name)           | `string` | Optional | cannot be null | [Untitled schema](openintent-floorplan-properties-project_name.md "https://example.com/schema/floorplan#/properties/project_name")           |
| [floor\_id](#floor_id)                   | `string` | Optional | cannot be null | [Untitled schema](openintent-floorplan-properties-floor_id.md "https://example.com/schema/floorplan#/properties/floor_id")                   |
| [rotation](#rotation)                    | `number` | Optional | cannot be null | [Untitled schema](openintent-floorplan-properties-rotation.md "https://example.com/schema/floorplan#/properties/rotation")                   |
| [dimensions](#dimensions)                | `array`  | Required | cannot be null | [Untitled schema](openintent-floorplan-properties-dimensions.md "https://example.com/schema/floorplan#/properties/dimensions")               |
| [wall\_segments](#wall_segments)         | `array`  | Optional | cannot be null | [Untitled schema](openintent-floorplan-properties-wall_segments.md "https://example.com/schema/floorplan#/properties/wall_segments")         |
| [reference\_markers](#reference_markers) | `array`  | Optional | cannot be null | [Untitled schema](openintent-floorplan-properties-reference_markers.md "https://example.com/schema/floorplan#/properties/reference_markers") |

## name

unique name of floorplan

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-properties-name.md "https://example.com/schema/floorplan#/properties/name")

### name Type

`string`

## vendor\_id

vendor's ID for this floorplan

`vendor_id`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-properties-vendor_id.md "https://example.com/schema/floorplan#/properties/vendor_id")

### vendor\_id Type

`string`

## map\_url

url endpoint of where to retrieve the map.

`map_url`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-properties-map_url.md "https://example.com/schema/floorplan#/properties/map_url")

### map\_url Type

`string`

## project\_name

Name of the project/file

`project_name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-properties-project_name.md "https://example.com/schema/floorplan#/properties/project_name")

### project\_name Type

`string`

## floor\_id

string representation of the floor id.

`floor_id`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-properties-floor_id.md "https://example.com/schema/floorplan#/properties/floor_id")

### floor\_id Type

`string`

## rotation

rotation of the floorplan from native orientation

`rotation`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-properties-rotation.md "https://example.com/schema/floorplan#/properties/rotation")

### rotation Type

`number`

## dimensions

dimensions of the floorplan

`dimensions`

*   is required

*   Type: `object[]` ([Details](openintent-floorplan-defs-dimension.md))

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-properties-dimensions.md "https://example.com/schema/floorplan#/properties/dimensions")

### dimensions Type

`object[]` ([Details](openintent-floorplan-defs-dimension.md))

### dimensions Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## wall\_segments

segments of wall on floorplan

`wall_segments`

*   is optional

*   Type: `object[]` ([Details](openintent-floorplan-defs-wall_segment.md))

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-properties-wall_segments.md "https://example.com/schema/floorplan#/properties/wall_segments")

### wall\_segments Type

`object[]` ([Details](openintent-floorplan-defs-wall_segment.md))

## reference\_markers

list of reference markers

`reference_markers`

*   is optional

*   Type: `object[]` ([Details](openintent-floorplan-defs-reference_marker.md))

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-properties-reference_markers.md "https://example.com/schema/floorplan#/properties/reference_markers")

### reference\_markers Type

`object[]` ([Details](openintent-floorplan-defs-reference_marker.md))

# Untitled object in undefined Definitions

## Definitions group dimension

Reference this group by using

```json
{"$ref":"https://example.com/schema/floorplan#/$defs/dimension"}
```

| Property          | Type     | Required | Nullable       | Defined by                                                                                                                                            |
| :---------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [length](#length) | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-dimension-properties-length.md "https://example.com/schema/floorplan#/$defs/dimension/properties/length") |
| [width](#width)   | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-dimension-properties-width.md "https://example.com/schema/floorplan#/$defs/dimension/properties/width")   |
| [height](#height) | `number` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-dimension-properties-height.md "https://example.com/schema/floorplan#/$defs/dimension/properties/height") |
| [unit](#unit)     | `string` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-dimension-properties-unit.md "https://example.com/schema/floorplan#/$defs/dimension/properties/unit")     |

### length

y-dimension of the floorplan

`length`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-dimension-properties-length.md "https://example.com/schema/floorplan#/$defs/dimension/properties/length")

#### length Type

`number`

#### length Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### width

x-dimension of the floorplan

`width`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-dimension-properties-width.md "https://example.com/schema/floorplan#/$defs/dimension/properties/width")

#### width Type

`number`

#### width Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### height

z-dimension of the floor (default height)

`height`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-dimension-properties-height.md "https://example.com/schema/floorplan#/$defs/dimension/properties/height")

#### height Type

`number`

#### height Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### unit

the dimension unit for length, width, height.

`unit`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-dimension-properties-unit.md "https://example.com/schema/floorplan#/$defs/dimension/properties/unit")

#### unit Type

`string`

#### unit Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"pixels"` |             |
| `"meters"` |             |
| `"feet"`   |             |

## Definitions group wall\_segment

Reference this group by using

```json
{"$ref":"https://example.com/schema/floorplan#/$defs/wall_segment"}
```

| Property                     | Type     | Required | Nullable       | Defined by                                                                                                                                                        |
| :--------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wall\_type](#wall_type)     | `string` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-wall_segment-properties-wall_type.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/wall_type") |
| [thickness](#thickness)      | `number` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-wall_segment-properties-thickness.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/thickness") |
| [height](#height-1)          | `number` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-wall_segment-properties-height.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/height")       |
| [start\_point](#start_point) | `object` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-wall_point.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/start_point")                      |
| [end\_point](#end_point)     | `object` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-wall_point.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/end_point")                        |

### wall\_type

Description of the wall type.

`wall_type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-wall_segment-properties-wall_type.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/wall_type")

#### wall\_type Type

`string`

### thickness

thickness in meters of the wall.

`thickness`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-wall_segment-properties-thickness.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/thickness")

#### thickness Type

`number`

### height

height of the wall in meters.

`height`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-wall_segment-properties-height.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/height")

#### height Type

`number`

### start\_point

Two-dimensional coordinate of a wall point

`start_point`

*   is required

*   Type: `object` ([Details](openintent-floorplan-defs-wall_point.md))

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-wall_point.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/start_point")

#### start\_point Type

`object` ([Details](openintent-floorplan-defs-wall_point.md))

### end\_point

Two-dimensional coordinate of a wall point

`end_point`

*   is required

*   Type: `object` ([Details](openintent-floorplan-defs-wall_point.md))

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-wall_point.md "https://example.com/schema/floorplan#/$defs/wall_segment/properties/end_point")

#### end\_point Type

`object` ([Details](openintent-floorplan-defs-wall_point.md))

## Definitions group wall\_point

Reference this group by using

```json
{"$ref":"https://example.com/schema/floorplan#/$defs/wall_point"}
```

| Property | Type     | Required | Nullable       | Defined by                                                                                                                                    |
| :------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| [x](#x)  | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-wall_point-properties-x.md "https://example.com/schema/floorplan#/$defs/wall_point/properties/x") |
| [y](#y)  | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-wall_point-properties-y.md "https://example.com/schema/floorplan#/$defs/wall_point/properties/y") |

### x

x-coordinate of the point

`x`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-wall_point-properties-x.md "https://example.com/schema/floorplan#/$defs/wall_point/properties/x")

#### x Type

`number`

### y

y-coordinate of the point

`y`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-wall_point-properties-y.md "https://example.com/schema/floorplan#/$defs/wall_point/properties/y")

#### y Type

`number`

## Definitions group coordinate\_xyz

Reference this group by using

```json
{"$ref":"https://example.com/schema/floorplan#/$defs/coordinate_xyz"}
```

| Property  | Type     | Required | Nullable       | Defined by                                                                                                                                            |
| :-------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [x](#x-1) | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_xyz-properties-x.md "https://example.com/schema/floorplan#/$defs/coordinate_xyz/properties/x") |
| [y](#y-1) | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_xyz-properties-y.md "https://example.com/schema/floorplan#/$defs/coordinate_xyz/properties/y") |
| [z](#z)   | `number` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_xyz-properties-z.md "https://example.com/schema/floorplan#/$defs/coordinate_xyz/properties/z") |

### x

coordinate in X dimension represented as a number

`x`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_xyz-properties-x.md "https://example.com/schema/floorplan#/$defs/coordinate_xyz/properties/x")

#### x Type

`number`

#### x Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### y

coordinate in Y dimension represented as a number

`y`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_xyz-properties-y.md "https://example.com/schema/floorplan#/$defs/coordinate_xyz/properties/y")

#### y Type

`number`

#### y Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### z

coordinate in Z dimension as height from floor represented as a number

`z`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_xyz-properties-z.md "https://example.com/schema/floorplan#/$defs/coordinate_xyz/properties/z")

#### z Type

`number`

## Definitions group coordinate\_latlong

Reference this group by using

```json
{"$ref":"https://example.com/schema/floorplan#/$defs/coordinate_latlong"}
```

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                                    |
| :---------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [latitude](#latitude)   | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_latlong-properties-latitude.md "https://example.com/schema/floorplan#/$defs/coordinate_latlong/properties/latitude")   |
| [longitude](#longitude) | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_latlong-properties-longitude.md "https://example.com/schema/floorplan#/$defs/coordinate_latlong/properties/longitude") |
| [elevation](#elevation) | `number` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_latlong-properties-elevation.md "https://example.com/schema/floorplan#/$defs/coordinate_latlong/properties/elevation") |

### latitude

Latitude expressed as ISO 6709 in degrees

`latitude`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_latlong-properties-latitude.md "https://example.com/schema/floorplan#/$defs/coordinate_latlong/properties/latitude")

#### latitude Type

`number`

#### latitude Constraints

**maximum**: the value of this number must smaller than or equal to: `90`

**minimum**: the value of this number must greater than or equal to: `-90`

### longitude

Longitude expressed as ISO 6709 in degrees

`longitude`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_latlong-properties-longitude.md "https://example.com/schema/floorplan#/$defs/coordinate_latlong/properties/longitude")

#### longitude Type

`number`

#### longitude Constraints

**maximum**: the value of this number must smaller than or equal to: `180`

**minimum**: the value of this number must greater than or equal to: `-180`

### elevation

height in meters above sea level

`elevation`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_latlong-properties-elevation.md "https://example.com/schema/floorplan#/$defs/coordinate_latlong/properties/elevation")

#### elevation Type

`number`

## Definitions group reference\_marker

Reference this group by using

```json
{"$ref":"https://example.com/schema/floorplan#/$defs/reference_marker"}
```

| Property                                   | Type     | Required | Nullable       | Defined by                                                                                                                                                                          |
| :----------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [coordinate\_xyz](#coordinate_xyz)         | `object` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_xyz.md "https://example.com/schema/floorplan#/$defs/reference_marker/properties/coordinate_xyz")                             |
| [coordinate\_latlong](#coordinate_latlong) | `object` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_latlong.md "https://example.com/schema/floorplan#/$defs/reference_marker/properties/coordinate_latlong")                     |
| [reference\_text](#reference_text)         | `string` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-reference_marker-properties-reference_text.md "https://example.com/schema/floorplan#/$defs/reference_marker/properties/reference_text") |

### coordinate\_xyz

A coordinate that references cartesian coordinates using x,y,z and/or a geospatial coordinate using lat/long

`coordinate_xyz`

*   is optional

*   Type: `object` ([Details](openintent-floorplan-defs-coordinate_xyz.md))

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_xyz.md "https://example.com/schema/floorplan#/$defs/reference_marker/properties/coordinate_xyz")

#### coordinate\_xyz Type

`object` ([Details](openintent-floorplan-defs-coordinate_xyz.md))

### coordinate\_latlong

A coordinate that references geospatial coordinates using using lat/long and altitude

`coordinate_latlong`

*   is optional

*   Type: `object` ([Details](openintent-floorplan-defs-coordinate_latlong.md))

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_latlong.md "https://example.com/schema/floorplan#/$defs/reference_marker/properties/coordinate_latlong")

#### coordinate\_latlong Type

`object` ([Details](openintent-floorplan-defs-coordinate_latlong.md))

### reference\_text

text string from reference

`reference_text`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-reference_marker-properties-reference_text.md "https://example.com/schema/floorplan#/$defs/reference_marker/properties/reference_text")

#### reference\_text Type

`string`
