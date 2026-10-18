from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os


# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Explicit template and static folders
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR,
    static_folder=STATIC_DIR
)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "predictive_maintenance_model.pkl"
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "iot_sensor_data.csv"
)


model = joblib.load(MODEL_PATH)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    temperature = float(data["temperature"])
    vibration = float(data["vibration"])
    current = float(data["current"])

    input_data = pd.DataFrame({
        "temperature": [temperature],
        "vibration": [vibration],
        "current": [current]
    })

    prediction = int(model.predict(input_data)[0])

    probability = float(
        model.predict_proba(input_data)[0][1]
    )

    status = (
        "FAILURE PREDICTED"
        if prediction == 1
        else "NORMAL"
    )

    return jsonify({
        "prediction": prediction,
        "status": status,
        "failure_probability": round(
            probability * 100,
            2
        ),
        "temperature": temperature,
        "vibration": vibration,
        "current": current
    })


@app.route("/sensor-data")
def sensor_data():

    df = pd.read_csv(DATA_PATH)

    latest = df.tail(50)

    return jsonify(
        latest.to_dict(
            orient="records"
        )
    )


if __name__ == "__main__":

    print("Template folder:", TEMPLATE_DIR)
    print("Template exists:", os.path.exists(
        os.path.join(TEMPLATE_DIR, "dashboard.html")
    ))

    print("Static folder:", STATIC_DIR)

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
