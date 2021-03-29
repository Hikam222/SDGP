from flask import Flask
app = Flask(__name__)

@app.route('/<int:name>')
def greet(name):
    return f'Hello {name}'


if __name__ == '__main__':
    app.run(debug=True)