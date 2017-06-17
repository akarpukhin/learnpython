import requests

def get_weather(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("что-то пошло не так!")

if __name__ == "__main__":
    data = get_weather("http://api.openweathermap.org/data/2.5/weather?q=Moscow&APPID=990a7da878286d1ebaaeb45810e9a714")
    print(data)