import json


def decrypt_json(json_path: str) -> dict:
    with open(json_path) as f:
        return json.load(f)
