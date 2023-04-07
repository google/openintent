# Untitled object in undefined Schema

```txt
https://example.com/schema/floorplan#/$defs/coordinate_latlong
```

A coordinate that references geospatial coordinates using using lat/long and altitude

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [openintent-floorplan.schema.json\*](../out/openintent-floorplan.schema.json "open original schema") |

## coordinate\_latlong Type

`object` ([Details](openintent-floorplan-defs-coordinate_latlong.md))

# coordinate\_latlong Properties

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                                    |
| :---------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [latitude](#latitude)   | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_latlong-properties-latitude.md "https://example.com/schema/floorplan#/$defs/coordinate_latlong/properties/latitude")   |
| [longitude](#longitude) | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_latlong-properties-longitude.md "https://example.com/schema/floorplan#/$defs/coordinate_latlong/properties/longitude") |
| [elevation](#elevation) | `number` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_latlong-properties-elevation.md "https://example.com/schema/floorplan#/$defs/coordinate_latlong/properties/elevation") |

## latitude

Latitude expressed as ISO 6709 in degrees

`latitude`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_latlong-properties-latitude.md "https://example.com/schema/floorplan#/$defs/coordinate_latlong/properties/latitude")

### latitude Type

`number`

### latitude Constraints

**maximum**: the value of this number must smaller than or equal to: `90`

**minimum**: the value of this number must greater than or equal to: `-90`

## longitude

Longitude expressed as ISO 6709 in degrees

`longitude`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_latlong-properties-longitude.md "https://example.com/schema/floorplan#/$defs/coordinate_latlong/properties/longitude")

### longitude Type

`number`

### longitude Constraints

**maximum**: the value of this number must smaller than or equal to: `180`

**minimum**: the value of this number must greater than or equal to: `-180`

## elevation

height in meters above sea level

`elevation`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_latlong-properties-elevation.md "https://example.com/schema/floorplan#/$defs/coordinate_latlong/properties/elevation")

### elevation Type

`number`
