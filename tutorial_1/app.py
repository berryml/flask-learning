from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hithere')
def hi():
    return 'Yo'

@app.route('/goodbye')
def bye():
    me = {
        'Name': 'Apple',
        'German': 'Apfel',
        'Colors': [
            {
                'name': 'red',
                'price': 1.5
            },
            {
                'name': 'green',
                'price': 2
            }
        ]
    }
    return jsonify(me)

@app.route('/add_2_numbers', methods=["POST"]) # this fxn only supports POST
def add_numbers():
    # get data from POSTed data
    data = request.get_json()
    x = data['x']
    y = data['y']
    answer = x + y
    returnAns = {'answer': answer}
    return jsonify(returnAns)
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)