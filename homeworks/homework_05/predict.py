import requests
from flask import Flask, jsonify, request
import pickle

model_file = "model1.bin"
dv_file = "dv.bin"

def read_pickle(file_path):
    with open(file_path, "rb") as f_in:
        py_object = pickle.load(f_in)
    return py_object




app = Flask("Credit")


@app.route("/predict", methods=["POST"])
def predict():
    customer_dict = request.get_json()

    X = dv.transform([customer_dict])
    y_pred = model.predict_proba(X)[0, 1]
    get_credit = y_pred >= 0.5

    result = {"credit_probability": float(y_pred), "get_credit": bool(get_credit)}

    return jsonify(result)




if __name__ == "__main__":
    model = read_pickle(model_file)
    dv = read_pickle(dv_file)
    app.run(debug=True, host="0.0.0.0", port=9696)
