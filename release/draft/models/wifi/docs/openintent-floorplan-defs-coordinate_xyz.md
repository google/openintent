# Untitled object in undefined Schema

```txt
https://example.com/schema/floorplan#/$defs/coordinate_xyz
```

A coordinate that references cartesian coordinates using x,y,z and/or a geospatial coordinate using lat/long

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [openintent-floorplan.schema.json\*](../out/openintent-floorplan.schema.json "open original schema") |

## coordinate\_xyz Type

`object` ([Details](openintent-floorplan-defs-coordinate_xyz.md))

# coordinate\_xyz Properties

| Property | Type     | Required | Nullable       | Defined by                                                                                                                                            |
| :------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [x](#x)  | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_xyz-properties-x.md "https://example.com/schema/floorplan#/$defs/coordinate_xyz/properties/x") |
| [y](#y)  | `number` | Required | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_xyz-properties-y.md "https://example.com/schema/floorplan#/$defs/coordinate_xyz/properties/y") |
| [z](#z)  | `number` | Optional | cannot be null | [Untitled schema](openintent-floorplan-defs-coordinate_xyz-properties-z.md "https://example.com/schema/floorplan#/$defs/coordinate_xyz/properties/z") |

## x

coordinate in X dimension represented as a number

`x`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_xyz-properties-x.md "https://example.com/schema/floorplan#/$defs/coordinate_xyz/properties/x")

### x Type

`number`

### x Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## y

coordinate in Y dimension represented as a number

`y`

*   is required

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_xyz-properties-y.md "https://example.com/schema/floorplan#/$defs/coordinate_xyz/properties/y")

### y Type

`number`

### y Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## z

coordinate in Z dimension as height from floor represented as a number

`z`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Untitled schema](openintent-floorplan-defs-coordinate_xyz-properties-z.md "https://example.com/schema/floorplan#/$defs/coordinate_xyz/properties/z")

### z Type

`number`
