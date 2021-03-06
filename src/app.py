from flask import Flask # importing the flask class
app = Flask(__name__) # creating an instance of the Flask class


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b


@app.route('/') # The primary url for our application
def hello_world(): # This method returns 'Flask Dockerized', which is displayed in our browser.
    return 'Flask Dockerized version 1.2.0'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # This statement starts the server on your local machine.

