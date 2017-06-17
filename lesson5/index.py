from flask import Flask

from weather import get_weather

city_id = 524901
appikey = '990a7da878286d1ebaaeb45810e9a714'

app = Flask(__name__)

@app.route("/")
def index():
    url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (city_id, appikey)
    pogoda = get_weather(url)
    result = "Температура: %s" % pogoda['main']['temp']
    return result


if __name__ == "__main__":
    app.run()