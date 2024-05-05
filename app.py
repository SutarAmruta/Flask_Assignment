from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
   return "<h1>welcome<h1>"


from controller import userController