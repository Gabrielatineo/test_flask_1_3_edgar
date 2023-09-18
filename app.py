from flask import Flask, request
app = Flask(__name__)

@app.route("/init")
def main():
    return {"payload":"welcome to my project"}





if __name__ == "main":
    app.run(debug=True)
