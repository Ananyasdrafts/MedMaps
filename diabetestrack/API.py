from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Load the pre-trained LSTM model and scaler
lstm_model = load_model("lstm_model.h5")  # Replace with the actual path to your LSTM model
scaler = MinMaxScaler()  # Assuming you have an appropriate scaler for the LSTM model

# Endpoint for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.get_json()

        # Extract relevant features for LSTM model
        features = np.array([data['insulin'], data['exercise']])

        # Scale features for LSTM model
        features_scaled = scaler.transform(features.reshape(1, -1))

        # Reshape and predict using LSTM model
        n_steps = 3  # Assuming the same n_steps as in your previous code
        X = features_scaled.reshape(1, n_steps, -1)
        future_prediction_scaled = lstm_model.predict(X)

        # Inverse transform to get the actual predicted glucose values
        future_prediction = scaler.inverse_transform(future_prediction_scaled)

        # Get the predicted value for tomorrow
        predicted_value = future_prediction[0, 0]

        # Trigger flag based on conditions
        flag = 1 if predicted_value > 130 or predicted_value < 80 else 0

        # Return the predicted value and flag
        return jsonify({'predicted_value': predicted_value, 'flag': flag})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
