# Model Ideas Feb-2023

This is just a place to track model ideas that include some visual components.


## Top level Models


### Floorplan
In order to reference which floorplan the AP lives on, we need to establish the floorplan object.

Requirements:
 * dimensions in a coordinate schema
 * references between coordinate systems

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
    }


    Floorplan_raster ||..|| Floorplan : augments
    Floorplan_raster {
        int width "Dimension pixels in X from LL" 
        int length "Dimension pixels in Y from LL"
        int height "Dimension pixels of floor height"
        float scale_px_to_m "Number of pixels to 1m (for all dimensions)"
    }
    Floorplan_GEO ||..|| Floorplan: augments
    Floorplan_GEO {
        float lattitude
        float longitude
        float elevation_m
    }
    Floorplan ||..|| References : uses
    References {
        container reference[]
        
    }
```

### Device and accessPoint

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
    AccessPoint ||..|| dot11_radio: uses
    dot11_radio {
        int id
        enum frequency
        int channel
        enum channel_width
        int power
    }

    antenna {

    }
```


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

    orientation {
        float rotation "yaw: 0 pointing toward x on map 0-360"
        float downtilt "pitch: 0 aligned with horizontal"
        float roll "roll"
    }
```