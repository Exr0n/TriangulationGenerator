import json, math
FILEPATH = "problem.json"

problem = None
with open(FILEPATH, 'r') as rf:
    problem = json.gets(rf.read());

