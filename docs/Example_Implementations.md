# Examples
This document is designed to show examples of how you can implement OpenIntent models using opensource libraries.

## Prereqs
This document assumes you have cloned the OpenIntent repo, and are in the `./releases/1.0.0/models/` directory.

```bash
git clone https://github.com/google/openintent.git

cd ./openintent/release/draft/models
```

# Python:
## python-jsonschema-objects
[python-jsonschema-objects](https://github.com/cwacek/python-jsonschema-objects)

This simple library allows you to instantiate objects in python based on the schema.

### Installation:
```bash
pip install python-jsonschema-objects
```

### Create Python objects
This will walk through how to instantiate a python object for the `floorplan` object based on the OpenIntent schema.

```python
import json
#import yaml
import python_jsonschema_objects as pjs

### Using YAML source files
with open("./oi-wifi.schema.json") as file:
    wifi_schema = json.load(file)
# Create Builder object
builder = pjs.ObjectBuilder(wifi_schema)
# Create namespace object for classes
ns = builder.build_classes()
oi = ns.OiWifi()

# Instantiate a floorplan and add to oi object
my_floor = ns.Floorplan()
my_floor.name = "my_floor01"
my_floor.dimensions = [ns.Dimension(length=100, width=200, unit="pixels")]
oi.floorplans = [my_floor]

#instantiate access_point and add to oi object.
my_ap = ns.Accesspoint(
	**{
		"name": "ap0001",
		"floorplan_name": "my_floor01",
		"manufacturer": "acmewireless",
		"model": "wifi9000"
	}
)


oi.accesspoints = [my_ap]

oi.serialize()


```
#### Output:
```json
{
    "accesspoints": [
        {
            "name": "my_ap0001",
            "floorplan_name": "my_floor01",
            "manufacturer": "acmewireless",
            "model": "wifi9000"
        }
    ],
    "floorplans": [
        {
            "name": "my_floor01",
            "dimensions": [
                {
                    "length": 100,
                    "width": 200,
                    "unit": "pixels"
                }
            ]
        }
    ]
}
```

### Testing Validation is working:
Let's repeat the example but use a non-allowed unit for the dimension.

```python
import json
import yaml
import python_jsonschema_objects as pjs

### Using YAML source files
with open("./openintent-floorplans.yaml") as file:
    floorplan_schema = yaml.safe_load(file)
builder = pjs.ObjectBuilder(floorplan_schema)
ns = builder.build_classes()
my_floor = ns.Floorplan()
my_floor.name = "my_floor01"
my_floor.dimensions = [ns.Dimension(length=100, width=200, unit="watchamacallits")]
my_floor.serialize()

```

```python
ValidationError: watchamacallits is not one of ['pixels', 'meters', 'feet']

During handling of the above exception, another exception occurred:

ValidationError                           Traceback (most recent call last)
Input In [2], in <module>
     12 my_floor = Floorplan()
     13 my_floor.name = "my_floor01"
---> 14 my_floor.dimensions = [Dimension(length=100, width=200, unit="watchamacallits")]
     15 my_floor.serialize()
```


### Instantiating objects from openintent payload

In this case, something has returned us openintent payloads, and we want to instantiate python objects based on those instances of the schema.

For this, we will load the `openintent-floorplans-testing.yaml` which contains multiple yaml documents of example floorplans.

```python
import json
import yaml
import python_jsonschema_objects as pjs

### Using YAML source files
with open("./openintent-floorplans.yaml") as file:
    floorplan_schema = yaml.safe_load(file)
builder = pjs.ObjectBuilder(floorplan_schema)
ns = builder.build_classes()

### Load testing examples:
floorplans = []
floorplan_examples = []

with open("./openintent-floorplans-testing.yaml", "r") as file:
    examples = yaml.safe_load_all(file)
    for example in examples:
        floorplan_examples.append(example)

for floorplan_instance in floorplan_examples:
    my_example = ns.Floorplan.from_json(json.dumps(floorplan_instance))
    floorplans.append(my_example)
[floor.validate() for floor in floorplans]
[floor.serialize() for floor in floorplans]
```

#### Output:
```python
[True, True, True, True]
```
```json
{
	"name": "floor-01",
	"dimensions": [{
		"length": 101,
		"width": 102,
		"unit": "meters"
	}]
}
```
```json
{
	"name": "floor-02",
	"vendor_id": "000000-0000-0000-00000000000",
	"map_url": "https://www.example.com/maps/00000000-0000-0000-000000000000.png",
	"floor_id": "1",
	"rotation": 0,
	"dimensions": [{
		"length": 101,
		"width": 102,
		"unit": "meters"
	}]
}
```
```json
{
	"name": "floor-03",
	"vendor_id": "000000-0000-0000-00000000000",
	"map_url": "https://www.example.com/maps/00000000-0000-0000-000000000000.png",
	"floor_id": "1",
	"rotation": 0,
	"dimensions": [{
		"length": 101,
		"width": 102,
		"unit": "meters"
	}],
	"wall_segments": [{
		"wall_type": "brick",
		"thickness": 0.5,
		"start_point": {
			"x": 0,
			"y": 0
		},
		"end_point": {
			"x": 100,
			"y": 100
		}
	}]
}
```
```json
{
	"name": "floor-04",
	"vendor_id": "000000-0000-0000-00000000000",
	"map_url": "https://www.example.com/maps/00000000-0000-0000-000000000000.png",
	"floor_id": "1",
	"rotation": 0,
	"dimensions": [{
		"length": 101,
		"width": 102,
		"unit": "meters"
	}],
	"wall_segments": [{
		"wall_type": "brick",
		"thickness": 0.5,
		"start_point": {
			"x": 0,
			"y": 0
		},
		"end_point": {
			"x": 100,
			"y": 100
		}
	}],
	"reference_markers": [{
		"coordinate_xyz": {
			"x": 100,
			"y": 200
		},
		"coordinate_latlong": {
			"latitude": -10.0,
			"longitude": -100.0
		},
		"reference_text": "marker_a"
	}, {
		"coordinate_xyz": {
			"x": 200,
			"y": 100
		},
		"coordinate_latlong": {
			"latitude": -11.0,
			"longitude": -120.0
		},
		"reference_text": "marker_b"
	}]
}
```
