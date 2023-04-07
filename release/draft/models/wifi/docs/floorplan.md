# JSON Schema

*representation of an floorplan*

## Properties

- **`name`** *(string)*: unique name of floorplan.
- **`vendor_id`** *(string)*: vendor's ID for this floorplan.
- **`map_url`** *(string)*: url endpoint of where to retrieve the map.
- **`project_name`** *(string)*: Name of the project/file.
- **`floor_id`** *(string)*: string representation of the floor id.
- **`rotation`** *(number)*: rotation of the floorplan from native orientation.
- **`dimensions`** *(array)*: dimensions of the floorplan.
  - **Items**: Refer to *#/$defs/dimension*.
- **`wall_segments`** *(array)*: segments of wall on floorplan.
  - **Items**: Refer to *#/$defs/wall_segment*.
- **`reference_markers`** *(array)*: list of reference markers.
  - **Items**: Refer to *#/$defs/reference_marker*.
