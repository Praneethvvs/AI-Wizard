import json
from collections import Counter
from pprint import pprint

with open("i129.json") as f:
    data  = json.load(f)

result_list = []
for keys,values in data.items():
    result_list.extend(list(values.keys()))


a = Counter(result_list)
pprint(a)

print("Changes in branch2")
