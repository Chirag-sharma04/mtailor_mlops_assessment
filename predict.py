import torch
from model import MLPClassifier
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load model
model = MLPClassifier(input_dim=20)
model.load_state_dict(torch.load("model.pth", map_location=torch.device("cpu")))
model.eval()

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        input_data = np.array(data["input"])
        input_tensor = torch.tensor(input_data).float()

        with torch.no_grad():
            outputs = model(input_tensor)
            predictions = torch.argmax(outputs, dim=1).tolist()

        return jsonify({"predictions": predictions})

    except Exception as e:
        return jsonify({"error": str(e)})

# For local testing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
