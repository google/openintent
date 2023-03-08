# Model Ideas Feb-2023

This is just a place to track model ideas that include some visual components.



## Floorplan
In order to reference which floorplan the AP lives on, we need to establish the floorplan object.

Requirements:
 * references to convert between coordinate systems
 * Wall segments and walls
 * Some sort of coordinate reference

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
    }
    Floorplan ||..o{ wall_segment : uses

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
    Floorplan ||..o{ reference : uses
    reference{
        float x
        float y
        float latitude
        float longitude

        
    }

    wall_segment {
        string type
        wall_point start "Start point"
        wall_point end "End point"

    }
    wall_segment ||..|| wall_point : uses
    wall_point {
        float x "x-coordinate"
        float y "y-coordinate"
    }
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
    AccessPoint ||..||dot11_radio: uses
    dot11_radio {
        int id
        enum frequency
        int channel
        enum channel_width
        int power
    }
    AccessPoint ||..|| antenna : uses
    antenna {
        string vendor
        string model
        float gain

    }

    AccessPoint ||..|| mounting : uses
    antenna ||..|| mounting : uses

    antenna ||..|| orientation : uses
    AccessPoint ||..|| orientation : uses
    orientation {
        float rotation "yaw: 0 pointing toward x on map 0-360"
        float downtilt "pitch: 0 aligned with horizontal"
        float roll "roll"
    }

    mounting {
        enum mount "CEILING, WALL, FLOOR, STAND, CUSTOM"
    }

```



## Coordinate System Work
```mermaid

erDiagram
    Coordinate {

    }

    X_Y_Coordinates {
        float x
        float y
    }

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