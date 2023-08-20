from flask import Flask
import json

app = Flask(__name__)

@app.route('/blog')
def articles():
    with open('data.json') as file:
        data = json.load(file)
        return data


if __name__ == "__main__":
    app.run(debug=True)