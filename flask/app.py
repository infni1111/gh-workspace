from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Codespace!"

if __name__ == '__main__':
    # host='0.0.0.0' pour écouter toutes les interfaces
    app.run(host='0.0.0.0', port=5000)
