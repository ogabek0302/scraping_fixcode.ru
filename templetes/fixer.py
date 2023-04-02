import json

with open('fixcode.json', 'r') as f:
    json_data = json.load(f)

used_ids = set()
new_json_data = []
new_id = 1

for item in json_data:
    if item['id'] in used_ids:
        item['id'] = new_id
        new_id += 1
    else:
        used_ids.add(item['id'])
    new_json_data.append(item)


with open('fixcode.json', 'w', encoding="utf-8") as f:
    json.dump(new_json_data, f, indent = 6, ensure_ascii=False)   
    print("done")