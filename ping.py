from flask import Flask

app = Flask("Ping")

@app.route('/')
def initial_page():
    return 'Initial Page. 😉'


@app.route("/ping", methods=["GET"])
def ping():
    return "Pong"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
