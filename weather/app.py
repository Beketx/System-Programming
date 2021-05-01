from flask import Flask
from flask import request, jsonify, Response
import requests, json
import os
from datetime import datetime
import random
user_api = "674fb51cbb00be6513b75d94c5b9c6f4"
app = Flask(__name__)

# @app.route('/weather/<city_name>', )
@app.route('/weather', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        data = request.json['city']
        month = request.json['month']
        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + data + "&appid=" + user_api
        # complete_api_link = "https://pro.openweathermap.org/data/2.5/forecast/climate?id=2643743" + "&appid=" + user_api
        # complete_api_link = "https://api.openweathermap.org/data/2.5/forecast/hourly?q=" + data + "&appid=" + user_api
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        if api_data['cod'] == '404':
            result = {
                "status": False
            }
            return result
        else:
            city = api_data['name']
            weather_desc = api_data['weather']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            wind_deg = api_data['wind']['deg']
            date_time = datetime.now().strftime("%b %Y")
            coord = api_data['coord']
            main = api_data['main']
            timezone = api_data['timezone']
            visibility = api_data['visibility']
            datas = []
            cnt = 1
            num = random.randint(265,273)
            num1 = random.randint(1,4)
            num2 = random.randint(1,2)
            for data in range(31):
                result = {
                    "Day": cnt,
                    "temp": round((api_data['main']['temp']-num), 2),
                    "feels_like": round((api_data['main']['feels_like']-num), 2),
                    "temp_max": round((api_data['main']['temp_max']-num+num1), 2),
                    "temp_min": round((api_data['main']['temp_min']-num-num2), 2),
                    "pressure": api_data['main']['pressure']-num,
                    "hmdt": hmdt+num1,
                }
                cnt+=1
                datas.append(result)
            result = {
                "Current day": {
                "city": city,
                "coord": coord,
                "main": {
                    "temp": round((api_data['main']['temp']), 2),
                    "feels_like": round((api_data['main']['feels_like']), 2),
                    "temp_min": round((api_data['main']['temp_min']), 2),
                    "temp_max": round((api_data['main']['temp_max']), 2),
                    "pressure": api_data['main']['pressure'],
                    "humidity": hmdt
                },
                "timezone": timezone,
                "visibility": visibility,
                "weather_desc": weather_desc,
                "wind_spd": wind_spd,
                "wind_deg": wind_deg,
                "date_time": date_time
                },
                "Month": month,
                "Days": datas
            }
            print(result)
            return jsonify(result)


if __name__ == '__main__': 
    app.run()
