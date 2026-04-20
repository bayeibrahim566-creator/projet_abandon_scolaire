from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model_dropout.pkl")
features = joblib.load("features.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # vérification
        missing = [f for f in features if f not in data]
        if missing:
            return jsonify({"error": f"Missing features: {missing}"}), 400

        # ordre exact du modèle
        X_input = [float(data[f]) for f in features]
        X = np.array(X_input).reshape(1, -1)

        # scaling
        X_scaled = scaler.transform(X)

        prediction = model.predict(X_scaled)[0]

        return jsonify({"prediction": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)