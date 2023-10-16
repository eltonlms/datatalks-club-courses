import requests
from flask import Flask, jsonify, request
import pickle


app = Flask("Credit")


@app.route("/predict_docker", methods=["POST"])
def predict():
    customer_dict = request.get_json()

    X = dv.transform([customer_dict])
    y_pred = model.predict_proba(X)[0, 1]
    get_credit = y_pred >= 0.5

    result = {"credit_probability": float(y_pred), "get_credit": bool(get_credit)}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
