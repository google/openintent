# Untitled object in undefined Schema

```txt
https://example.com/schema/floorplan#/$defs/dimension
```

dimension of a floorplan where the origin is located in the lower left corner, making all refences to location positive values

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [openintent-floorplan.schema.json\*](../out/openintent-floorplan.schema.json "open original schema") |

## dimension Type

`object` ([Details](openintent-floorplan-defs-dimension.md))

# dimension Properties

| Property          | Type     | Required | Nullable       | Defined by                                                                                                                                            |
| :---------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [length](#length) | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-dimension-properties-length.md "https://example.com/schema/floorplan#/$defs/dimension/properties/length") |
| [width](#width)   | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-dimension-properties-width.md "https://example.com/schema/floorplan#/$defs/dimension/properties/width")   |
| [height](#height) | `number` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-dimension-properties-height.md "https://example.com/schema/floorplan#/$defs/dimension/properties/height") |
| [unit](#unit)     | `string` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-dimension-properties-unit.md "https://example.com/schema/floorplan#/$defs/dimension/properties/unit")     |

## length

y-dimension of the floorplan

`length`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-dimension-properties-length.md "https://example.com/schema/floorplan#/$defs/dimension/properties/length")

### length Type

`number`

### length Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## width

x-dimension of the floorplan

`width`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-dimension-properties-width.md "https://example.com/schema/floorplan#/$defs/dimension/properties/width")

### width Type

`number`

### width Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## height

z-dimension of the floor (default height)

`height`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-dimension-properties-height.md "https://example.com/schema/floorplan#/$defs/dimension/properties/height")

### height Type

`number`

### height Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## unit

the dimension unit for length, width, height.

`unit`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-dimension-properties-unit.md "https://example.com/schema/floorplan#/$defs/dimension/properties/unit")

### unit Type

`string`

### unit Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"pixels"` |             |
| `"meters"` |             |
| `"feet"`   |             |
