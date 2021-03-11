import json
from collections import Counter
from pprint import pprint

a = "123451"

x = dict(map(reversed, enumerate(a)))["1"]


print(next(enumerate(a)))