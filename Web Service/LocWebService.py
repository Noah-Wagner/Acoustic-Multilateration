from flask import Flask
from flask import request
from flask import json
from flask_cors import CORS, cross_origin
import numpy

import CoordHandler

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'hi'

@app.route('/updatesensorloc/', methods=['POST'])
def update_loc():
    _sensor_loc = request.get_json()
    return CoordHandler.CoordHandler.update_loc(_sensor_loc)

@app.route('/getloc/')
def get_loc():
    x = CoordHandler.CoordHandler.get_loc()
    y = json.jsonify(x)
    return y

@app.route('/updateabsloc/')
def update_abs_loc():
    x = request.args.get('x')
    y = request.args.get('y')
    z = request.args.get('z')
    return CoordHandler.CoordHandler.update_abs_loc(x, y, z)

@app.route('/getabsloc/')
def get_abs_loc():
    x = CoordHandler.CoordHandler.get_abs_loc()
    y = json.jsonify(x)
    return y

@app.route('/getsensorloc/')
def get_sensor_loc():
    return json.dumps(CoordHandler.CoordHandler.get_sensor_loc())

@app.route('/getsourceloc/')
def multilateration():
    try:
        _loc = CoordHandler.CoordHandler.get_loc(request.args.get('arrivaltimes'))
    except ValueError as err:
        return str(err)

    y = _loc[0]
    y = numpy.ndarray.tolist(y)
    y = json.dumps(y)


    return y


if __name__ == '__main__':
    app.run()
