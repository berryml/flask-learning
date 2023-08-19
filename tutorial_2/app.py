from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def check_response(posted_data, resource_call='add'):
    if 'x' and 'y' not in posted_data.keys():
        return 'The posted response did not contain both x and y', 400
    elif resource_call == 'divide' and posted_data['y'] == 0:
        return 'Division by zero!', 400
    else:
        return 'All good', 200


# define API resources
class Add(Resource):
    def post(self):
        data = request.get_json()
        
        message, status_code = check_response(data)
        
        if status_code != 200:
            z = message
        else:
            x = data['x']
            y = data['y']
            z = x + y
        return_map = {
            'message': z,
            'status_code': status_code
        }
        return jsonify(return_map)


class Subtract(Resource):
    def post(self):
        data = request.get_json()
        
        message, status_code = check_response(data, resource_call='subtract')
        
        if status_code != 200:
            z = message
        else:
            x = data['x']
            y = data['y']
            z = x - y
        return_map = {
            'message': z,
            'status_code': status_code
        }
        return jsonify(return_map)

class Multiply(Resource):
    def post(self):
        data = request.get_json()
        
        message, status_code = check_response(data, resource_call='multiply')
        
        if status_code != 200:
            z = message
        else:
            x = data['x']
            y = data['y']
            z = x * y
        return_map = {
            'message': z,
            'status_code': status_code
        }
        return jsonify(return_map)

class Divide(Resource):
    def post(self):
        data = request.get_json()
        
        message, status_code = check_response(data, resource_call='divide')
        
        if status_code != 200:
            z = message
        else:
            x = data['x']
            y = data['y']
            z = x / y
        return_map = {
            'message': z,
            'status_code': status_code
        }
        return jsonify(return_map)


@app.route('/')
def hello():
    return "hello!"

api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')

if __name__ == '__main__':
    app.run(debug=True)