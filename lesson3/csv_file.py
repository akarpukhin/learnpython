import csv

with open('users.csv', 'r', encoding='utf-8') as f:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    reader = csv.DictReader(f, fields, delimiter=';')
    for row in reader:
        print(row)