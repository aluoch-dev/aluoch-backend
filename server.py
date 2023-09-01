from flask import Flask
import json

app = Flask(__name__, static_folder="./aluoch/build", static_url_path="/")

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/')
def articles():
    with open('data.json') as file:
        data = json.load(file)
        return data

if __name__ == "__main__":
    app.run(debug=True)