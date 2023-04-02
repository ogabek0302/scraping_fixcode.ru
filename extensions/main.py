import requests
from bs4 import BeautifulSoup
import csv
import json

all_data = []
with open('links.csv', 'r') as f:
    links = csv.reader(f)
    next(links)


    for row in links:
        url = row[0]
        id = 1
        print("connecting to ", url)
        print("downloading....")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        name = soup.find('h1', class_='extension-title-single').text.strip()
        img = soup.find('img', class_='img-fluid')['src']
        desc = soup.find('div', class_='tab-pane fade show active', id='description').text.strip()
        
        data = {
        'id': id,    
        'name': name,
        'img': img,
        'description': desc,
        'link': url
        }
        all_data.append(data)
        id = id + 1
with open('data.json', 'w', encoding="utf-8") as f:
    json.dump(all_data, f, indent = 6, ensure_ascii=False)   
    print("done")