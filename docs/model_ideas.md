# Model Ideas Feb-2023

This is just a place to track model ideas that include some visual components.



## Floorplan
In order to reference which floorplan the AP lives on, we need to establish the floorplan object.

Requirements:
 * references points to convert between coordinate systems
 * Wall segments and walls
 * Some sort of coordinate reference
 * Dimensions and units

 `openintent-floorplan.yang`

```mermaid
---
Title: Floorplan Constructs
---

erDiagram
    Floorplan {
        string name PK "unique name for floorplan"
        string vendor_id "If vendor implements map UID"
        string map_url "if you can retrieve map from url"
        int floor_num "Floor number"
        float rotation "Rotation of map from native orientation"
        container wall_segments
        container references
        container dimensions
    }
    Floorplan ||..|{ dimension : uses
    Floorplan ||..o{ wall_segment : uses

    dimension {
        float length "y dimension"
        float width "x dimension"
        float height "z-dimension of floor height"
        enum unit "pixel, meter, feet, etc"
        float scale "scale of unit to other measurement e.g. pixels to meter"
        enum scale_to_unit "pixel, meter, feet, etc"
    }

    reference {
        float x
        float y
        float latitude
        float longitude
    }
    Floorplan ||..o{ reference : uses

    wall_segment {
        string type
        float thickness "thickness of wall in m"
        float height "height of wall in m"
        wall_point start "Start point"
        wall_point end "End point"

    }
    
    wall_point {
        float x "x-coordinate"
        float y "y-coordinate"
    }
    wall_segment ||..|| wall_point : uses
```

## Device and accessPoint

`openintent-access-point.yang`
```mermaid
erDiagram
   Device{
        string name PK "Unique name of device"
        string fqdn "Fully qualified name"
        string floorplan_name "floorplan name"
        string asset_tag "device asset tag"
        
    }
    AccessPoint ||..|| Device: augments
    AccessPoint {
        string serial_number
        string mac_address
        string claim_code
        container radios
        list[] ssids
        string vendor
        string model
        list[] antennas

        
    }

    AccessPoint ||..|{ dot11_radio: uses
    radio {
        int id
        float power "dbm"
    }
    dot11_radio ||..|| radio: augments
    dot11_radio {
        enum frequency
        int channel
        enum channel_width
    }
    ble_radio ||..|| radio: augments
    ble_radio{
        string major
        string minor

    }
    AccessPoint }o..o{ ble_radio: uses
    AccessPoint ||..|| Antenna : uses
    Antenna {
        string vendor
        string model
        float gain
        boolean non-colocated_mounting "Antenna is not colocated with AP mount"
    }

    AccessPoint ||..|| mounting : uses
    Antenna ||..|| mounting : uses

    Antenna ||..|| orientation : uses
    AccessPoint ||..|| orientation : uses
    orientation {
        float rotation "yaw: 0 pointing toward x on map 0-360 AKA PAN"
        float downtilt "pitch: 0 aligned with horizontal TILT"
        float roll "roll"
    }

    mounting {
        enum mount "CEILING, WALL, FLOOR, STAND, CUSTOM"
        string name 
        string vendor
        string part_number
    }

    Coordinates {
        string floorplan_name
    }


    X_Y_Coordinates {
        float x
        float y
    }
    X_Y_Coordinates ||..|| Coordinates: augments
    X_Y_Z_Coordinates {
        float z
    }
    X_Y_Z_Coordinates }|..|{ X_Y_Coordinates : Augments

    AccessPoint ||..|| X_Y_Z_Coordinates : uses
    Antenna ||..|| X_Y_Z_Coordinates: uses

```



## Coordinate Systems playground.
```mermaid

erDiagram
    Coordinate {
        string floorplan_name
    }


    X_Y_Coordinates {
        float x
        float y
    }
    X_Y_Coordinates ||..|| Coordinate: augments
    X_Y_Z_Coordinates {
        float z
    }
    X_Y_Z_Coordinates }|..|{ X_Y_Coordinates : Augments

    GEO_Coordinates {
        float lat
        float lng
        float elevation
    }

    
```



```yaml
---
access-point:
    - name: device_01
      fqdn: device_01.corp.com
      floorplan:
        $ref": /schemas/floorplan
      asset_tag: abc0123456
      serial_number: az123456789
      mac_address: 00:00:00:00:00:00
      claim_code: abcdefg123
      ssids:
        - ssid_1
        - ssid_2
        - ssid_3
      vendor: arisco
      model: AP123




```

## Access-point json-schema


```yaml
---
    $id: https://example.com/schema/access-point
    $schema: https://json-schema.org/draft/2020-12/schema
    description: representation of an access-point
    type: object
    properties:
        name:
            type: string
            description: unique name of access point.
        floorplan_name:
            type: string
            description: name of floorplan to which this access-point belongs.
        asset_tag:
            type: string
            description: asset tag belonging to this access point.
        serial_number:
            type: string
            description: serial number of this access point.
        mac_address:
            type: string
            description: mac address of this access point.
        manufacturer:
            type: string
            description: the manufacturer name for this access point.
        model:
            type: string
            description: the model number of this particular access point
        sku:
            type: string
            description: sku part number for this specific access-point.
        radios:
            type: array
            items:
                $ref: https://example.com/schema/radio.json
        ssids:
            type: array
            items:
                type: string
        antennas:
            type: array
            items:
                $ref: https://example.com/schema/antenna.json

```
## floorplan json-schema

```yaml
---
$id: https://example.com/schema/floorplan
$schema: https://json-schema.org/draft/2020-12/schema
description: representation of an floorplan
type: object
properties:
    name:
        type: string
        description: unique name of floorplan
    vendor_id:
        type: string
        description: vendor's ID for this floorplan
    map_url:
        type: string
        description: url endpoint of where to retrieve the map.
    floor_id:
        type: string
        description: string representation of the floor id.
    rotation:
        type: number
        description: rotation of the floorplan from native orientation
    dimensions:
        type: array
        description: dimensions of the floorplan
        items:
            $refs: "#/$defs/dimension"
$defs:
    dimension:
        type: object
        properties:
            length:
                type: number
                description: y-dimension of the floorplan
            width:
                type: number
                description: x-dimension of the floorplan
            height:
                type: number
                description: z-dimension of the floor (default height)
            unit:
                type: string
                description: the dimension unit for length, width, height.
                enum:
                    - pixel
                    - meter
                    - feet

```

```yaml
$id: https://example.com/schema/floorplan
$schema: https://json-schema.org/draft/2020-12/schema
description: representation of an floorplan
type: object
properties:
    name:
        type: string
    vendor_id:
        type: string
    map_url:
        type: string
    floor_id:
        type: string
    rotation:
        type: number
    dimensions:
        type: array
        items:
            $refs: "#/$defs/dimension"
$defs:
    dimension:
        type: object
        properties:
            length:
                type: number
            width:
                type: number
            height:
                type: number
            unit:
                type: string
                enum:
                    - pixel
                    - meter
                    - feet
```


```json
{
  "$id": "https://example.com/schema/floorplan",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "description": "representation of an floorplan",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "vendor_id": {
      "type": "string"
    },
    "map_url": {
      "type": "string"
    },
    "floor_id": {
      "type": "string"
    },
    "rotation": {
      "type": "number"
    },
    "dimensions": {
      "type": "array",
      "items": {
        "$refs": "#/$defs/dimension"
      }
    }
  },
  "$defs": {
    "dimension": {
      "type": "object",
      "properties": {
        "length": {
          "type": "number"
        },
        "width": {
          "type": "number"
        },
        "height": {
          "type": "number"
        },
        "unit": {
          "type": "string",
          "enum": [
            "pixel",
            "meter",
            "feet"
          ]
        }
      }
    }
  }
}
```