from flask import Flask, request, jsonify
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

app = Flask(__name__)

# Обучаем модель
iris = load_iris()
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(iris.data, iris.target)

VERSION = "v1.1.0"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "version": VERSION})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    x = np.array(data['x']).reshape(1, -1)
    pred = model.predict(x)[0]
    return jsonify({"prediction": int(pred)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
