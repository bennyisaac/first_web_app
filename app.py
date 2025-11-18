from flask import Flask

app = Flast(__name__)

@app.route("/")
def home():
    return "Hello"

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=10000)