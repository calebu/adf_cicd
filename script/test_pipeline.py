import sys
import json

print(sys.argv[1])
j = json.loads(sys.argv[1])
print(j['pipelines'][0])

