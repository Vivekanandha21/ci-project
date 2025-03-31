from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    message = "Hope you are getting an idea on how it works!!!"
    return f"{message}<br>HELLO TO VK WORLD! FIRST CI/CD PROJECT"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    
    

