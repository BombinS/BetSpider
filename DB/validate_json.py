#!bin/usr/env python

from pathlib import Path
import json

# количество матчей в чемпионате равно x * (x - 1)
# 16	240
# 17	272
# 18	306

def validate(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        print(f"{data["season"]} {len(data["schedule"])}")
    
if __name__ == "__main__":
    path = Path("ParsedData")
    for filepath in list(path.rglob("*.json")):
        validate(filepath)
