import json

with open('mugglecode.json', 'r') as f:
    print(f.readline().encode('utf-8').decode('unicode_escape'), type(f.read()))