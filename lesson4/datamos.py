import requests
import zipfile
import os

response = requests.get('https://op.mos.ru/EHDWSREST/catalog/export/get?id=220264', stream=True)

response.raise_for_status()

with open('bus_stations.zip', 'wb') as handle:
    for block in response.iter_content(1024):
        handle.write(block)


with zipfile.ZipFile("bus_stations.zip","r") as zip_ref:
    zip_ref.extractall()

    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'bus_stations.zip')
    os.remove(path)


#with open('users.csv', 'r', encoding='utf-8') as f:
##    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
 #   reader = csv.DictReader(f, fields, delimiter=';')
 #   for row in reader:
 #       print(row)