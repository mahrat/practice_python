# json practice - used constantly for apis and config files

import json

data = {
    "name": "sahil",
    "age": 22,
    "skills": ["python", "sql", "git"],
    "is_employed": False,
    "address": None
}

# python dict -> json string
json_string = json.dumps(data, indent=4)
print(json_string)

# json string -> python dict
parsed = json.loads(json_string)
print(parsed["name"])
print(type(parsed))

# writing json to a file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# reading json from a file
with open("data.json", "r") as f:
    loaded = json.load(f)
print(loaded)

# note: json doesn't have a "tuple" type, tuples become lists after round-tripping
sample = {"coords": (1, 2, 3)}
dumped = json.dumps(sample)
print(dumped)   # coords becomes a list [1, 2, 3] in the json output
back = json.loads(dumped)
print(type(back["coords"]))   # list, not tuple anymore -> lost info here, good to remember

# handling json decode errors
bad_json = "{name: sahil}"  # missing quotes around keys, invalid json
try:
    json.loads(bad_json)
except json.JSONDecodeError as e:
    print("invalid json:", e)

# cleanup
import os
os.remove("data.json")
