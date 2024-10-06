from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = 'e9896e79c102370ab332f5d1eeb0aa92'

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather = None
    temp = None
    error = None

    if request.method == 'POST':
        user_input = request.form['city']
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
        
        if weather_data.json()['cod'] == '404':
            error = "No City Found"
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])

    return render_template('index.html', weather=weather, temp=temp, error=error)

if __name__ == '__main__':
    app.run(debug=True)
