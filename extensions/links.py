import requests
from bs4 import BeautifulSoup
import csv


for i in range(1,137):
    print(f"Обработка страницы номер: {i}...")
    url = f'https://fixcode.ru/extensions/wordpress/page/{i}/'

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a', class_='btn btn-secondary btn-sm')

    with open('links.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for link in links:
            writer.writerow([link['href']])
    print("Обработка успешно прошла...")
print("Все ссылки успешно сохранены.")   

