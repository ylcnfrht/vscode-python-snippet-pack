import json
 
# Opening JSON file
f = open('python_snippets.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
print(data.keys())

wantedKeys = []
notWanted = ['built_in.', '=>']
for key in data.keys():
    if 'built_in.' not in key and '=>' not in key:
        wantedKeys.append(key)
# Closing file
f.close()

outputData = { your_key: data[your_key] for your_key in wantedKeys }

with open("output.json", "w") as outfile:
    json.dump(outputData, outfile)