from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Add this
from model import predict_aqi

app = Flask(__name__)
CORS(app)  # ✅ This allows frontend to call backend

@app.route('/')
def home():
    return "POLLULENS Backend Running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    pm25 = data['pm25']
    pm10 = data['pm10']
    no2 = data['no2']
    so2 = data['so2']
    co = data['co']
    o3 = data['o3']

    predicted_aqi = predict_aqi(pm25, pm10, no2, so2, co, o3)

    # Simple health logic (you can improve later)
    if predicted_aqi <= 50:
        status = "Good"
        suggestion = "Enjoy outdoor activities!"
        clothes = "Normal clothes"
    elif predicted_aqi <= 100:
        status = "Moderate"
        suggestion = "Sensitive people should be careful."
        clothes = "Light mask recommended"
    else:
        status = "Unhealthy"
        suggestion = "Avoid outdoor activities."
        clothes = "Wear N95 mask, full sleeves"

    return jsonify({
        "predicted_aqi": predicted_aqi,
        "status": status,
        "suggestion": suggestion,
        "clothes": clothes
    })

if __name__ == '__main__':
    app.run(debug=True)
