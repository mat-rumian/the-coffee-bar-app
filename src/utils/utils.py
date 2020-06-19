import json


def to_json(obj):
    if isinstance(obj, str):
        return json.loads(obj)
    elif isinstance(obj, dict):
        return obj
