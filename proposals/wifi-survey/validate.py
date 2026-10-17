"""Validate the proposed external schema and paired examples (no network)."""

import copy
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]


def read_json(path):
    return json.loads(path.read_text())


def main():
    schema = read_json(ROOT / "oi-wifi-survey.schema.json")
    source = yaml.safe_load((ROOT / "src/openintent-wifi-survey.yaml").read_text())
    assert source == schema, "YAML source and generated JSON differ"
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    measurements = read_json(ROOT / "examples/measurements.json")
    validator.validate(measurements)

    # The released project schema has existing meta-schema errors in unrelated
    # definitions. Validate the project instance without claiming that the
    # complete released schema passes meta-validation.
    project_schema = read_json(REPO / "release/2.0.0/models/oi-wifi.schema.json")
    project = read_json(ROOT / "examples/project.json")
    Draft202012Validator(project_schema, format_checker=FormatChecker()).validate(project)
    path = project["floorplans"][0]["survey_paths"][0]
    assert path["path_data_type"] == "OTHER"
    assert path["path_data_uri"] == "https://example.org/surveys/measurements.json"
    assert "scan_events" not in path

    failures_checked = 0
    for field in ("bssid", "rssi_dbm", "frequency_mhz"):
        invalid = copy.deepcopy(measurements)
        del invalid["scan_events"][0]["wifi_observations"][0][field]
        assert not validator.is_valid(invalid), field
        failures_checked += 1
    for field, value in (("bssid", "invalid"), ("rssi_dbm", None),
                         ("frequency_mhz", 0), ("frequency_mhz", 5180.5),
                         ("timestamp", "2026-10-17T00:00:00Z")):
        invalid = copy.deepcopy(measurements)
        invalid["scan_events"][0]["wifi_observations"][0][field] = value
        assert not validator.is_valid(invalid), field
        failures_checked += 1
    for field in ("timestamp", "wifi_observations"):
        invalid = copy.deepcopy(measurements)
        del invalid["scan_events"][0][field]
        assert not validator.is_valid(invalid), field
        failures_checked += 1
    invalid = copy.deepcopy(measurements)
    invalid["survey_version"] = "99.0.0"
    assert not validator.is_valid(invalid)
    failures_checked += 1
    empty = copy.deepcopy(measurements)
    empty["scan_events"][0]["wifi_observations"] = []
    validator.validate(empty)

    # Check the example's intended timing cases without inventing a production
    # interpolation implementation: precise reception, stale cache, fallback.
    first, second = measurements["scan_events"]
    points = path["path_points"]
    observed = first["wifi_observations"][0]["timestamp"]
    fraction = (observed - points[0]["timestamp"]) / (points[1]["timestamp"] - points[0]["timestamp"])
    assert fraction == 0.5  # (15, 20), not the delivery-time position (16, 20).
    assert first["wifi_observations"][1]["timestamp"] < points[0]["timestamp"]
    assert "timestamp" not in second["wifi_observations"][0]
    fraction = (second["timestamp"] - points[1]["timestamp"]) / (points[2]["timestamp"] - points[1]["timestamp"])
    assert fraction == 0.5  # Approximate fallback position (20, 30).
    print(f"Schema, source parity, paired examples, timing cases, and {failures_checked} negative cases passed.")


if __name__ == "__main__":
    main()
