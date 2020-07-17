from flask import Flask, jsonify, make_response,request,render_template
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

class Openweather(Resource):
    def post(self):
        #zipcode =request.form['zip']
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=90050,us&appid=59bc8f946807f19f26fe31d3082aee90')
        json_object = r.json()
        temp_k = float(json_object['main']['temp'])
        temp_f = (temp_k - 273.15) * 1.8 + 32
        return {'Temperature':temp_f}



class openmap(Resource):
    def get(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=90050,us&appid=59bc8f946807f19f26fe31d3082aee90')
        json_object = r.json()
        temp_k = float(json_object['main']['temp'])
        temp_f = (temp_k - 273.15) * 1.8 + 32
        return {'Temperature':temp_f}

class dee(Resource):
    def delete(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=90050,us&appid=59bc8f946807f19f26fe31d3082aee90')
        json_object = r.json()
        temp_k = float(json_object['main']['temp'])
        return {'temperature Deleted':temp_k}


#@app.route('/index')
#def index():
    #return render_template('index.html')


api.add_resource(Openweather,'/open')
api.add_resource(openmap,'/getinto')
api.add_resource(dee,'/outside')


if __name__ == '__main__':
    app.run(debug=True)
