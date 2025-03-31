from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'HELLO TO VK WORLD! FIRST CI/CD PROJECT'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    

