from flask import Flask
from flask import request
from flask import json

import CoordHandler

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Acoustic Multilateration Location Web Server'

@app.route('/updateloc/')
def update_loc():
    x = request.args.get('x')
    y = request.args.get('y')
    if (x == None and y == None):
        return 'false'
    else:
        return CoordHandler.CoordHandler.update_loc(x, y)


@app.route('/getloc/')
def get_loc():
    x = CoordHandler.CoordHandler.get_loc()
    y = json.jsonify(x)
    return y


if __name__ == '__main__':
    app.run()
