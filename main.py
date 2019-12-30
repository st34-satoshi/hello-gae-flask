from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "Hello Flask in GAE" 

if __name__ == '__main__':
    app.run()
