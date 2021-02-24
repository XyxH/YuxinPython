from flask import Flask

app=Flask(__name__)
@app.route("/index",methods=["get","post"])
def index():
    return "HELLO WORLD!"

if __name__ == '__main__':
    app.run(debug=True,host="localhost",port=10000)