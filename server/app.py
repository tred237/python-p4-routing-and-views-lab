#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:word>")
def print_string(word):
    print(word)
    return word

@app.route("/count/<int:n>")
def count(n):
    l = []
    for i in range(n): l.append(f'{i}\n')
    return ''.join(l)

@app.route('/math/<num1>/<operator>/<num2>')
def math(num1, operator, num2):
    num1_int = int(num1)
    num2_int = int(num2)
    if operator == '+':
        return f'{num1_int + num2_int}'
    elif operator == '-':
        return f'{num1_int - num2_int }'      
    elif operator == '*':
        return f'{num1_int * num2_int}'
    elif operator == 'div':
        return f'{num1_int / num2_int}'
    elif operator == '%':
        return f'{num1_int % num2_int}'
    else:
        return 'Oops'
        

if __name__ == '__main__':
    app.run(port=5555, debug=True)
