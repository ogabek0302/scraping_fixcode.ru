import json
import uuid

with open('all.json', 'r') as f:
    json_data = json.load(f)

new_json_data = []

for item in json_data:
    # generate a random UUID as the new ID
    item['id'] = str(uuid.uuid4())
    new_json_data.append(item)

with open('fixcode.json', 'w', encoding="utf-8") as f:
    json.dump(new_json_data, f, indent=4, ensure_ascii=False)

print("done")
