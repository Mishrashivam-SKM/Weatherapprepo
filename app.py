from flask import Flask , render_template, request
import requests 

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp', methods=['POST'])
def get_weatherdata():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameter = {
        'q': request.form.get("city"),
        'appid': request.form.get("appid"),
        'units' : request.form.get("units")
        }
    data_request = requests.get(url , params= parameter)
    city = data['name']
    data = data_request.json()
    return f"data :{data} city:c{city}"


if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5002)
