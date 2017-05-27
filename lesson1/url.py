import requests

url = input('Enter URL: ')

secure_url = {'google' , 'fb', 'facebook'}

if url[0:4] != 'http':
	if url.split('.')[0] in secure_url:
		url = 'https://' + url	
	else:
		url = 'http://' + url
else: 
	if url.replace('http://', '').split('.')[0] in secure_url:
		url = url.replace('http://', 'https://')


try:
	r = requests.get(url)
	if r.status_code == 200:
		print("--- === ---")
		print("Вы зашли на сайт: " + url)
		print("Status code: " + str(r.status_code))	
	else:
		print("--- === ---")
		print("Вы не смогли зайти на сайт: " + url)
		print("Status code: " + str(r.status_code))

except requests.exceptions.ConnectionError as e:
	print("--- === ---")
	print("Вы не смогли зайти на сайт: " + url)

