#!bin/usr/env python

from pathlib import Path
import json

# x это количество команд в чемпионате
# количество туров: (x - 1) * 2
# в каждом туре: x /2 матчей   
# количество матчей в чемпионате равно (x - 1) * 2 * (x / 2) 
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
