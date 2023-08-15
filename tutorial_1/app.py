from flask import Flask, jsonify

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
    
if __name__ == '__main__':
    app.run(host='localhost', debug=True)