#!/bin/usr/env python

import json

result = {}
start = 0.6
pointer = round(start, 2)

while pointer < 1:
    leftBorder = round(pointer - 0.024, 3)
    rightBorder = round(pointer + 0.025, 3)
    result[str(pointer)] = [leftBorder, rightBorder]
    pointer = round(pointer + 0.05, 2)

with open("scales.json", "w", encoding='utf-8') as f:
    json.dump(result, f)