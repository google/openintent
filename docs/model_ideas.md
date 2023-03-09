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
        enum unit "pixel, meter, foot, etc"
        float scale "scale of unit to other measurement e.g. pixels to meter"
        enum scale_to_unit "pixel, meter, foot, etc"
    }

    Floorplan_raster }o..|| Floorplan : augments
    Floorplan_raster {
        int width "Dimension pixels in X from LL" 
        int length "Dimension pixels in Y from LL"
        int height "Dimension pixels of floor height"
        float scale_px_to_m "Number of pixels to 1m (for all dimensions)"
    }
    Floorplan_GEO }o..|| Floorplan: augments
    Floorplan_GEO {
        float lattitude
        float longitude
        float elevation_m
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