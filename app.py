# app.py
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

model = pickle.load(open('parkinson_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

feature_mapping = {
    'mdvp_fo': 'MDVP:Fo(Hz)',
    'mdvp_fhi': 'MDVP:Fhi(Hz)',
    'mdvp_flo': 'MDVP:Flo(Hz)',
    'jitter_percent': 'MDVP:Jitter(%)',
    'jitter_abs': 'MDVP:Jitter(Abs)',
    'rap': 'MDVP:RAP',
    'ppq': 'MDVP:PPQ',
    'jitter_ddp': 'Jitter:DDP',
    'shimmer': 'MDVP:Shimmer',
    'shimmer_db': 'MDVP:Shimmer(dB)',
    'apq3': 'Shimmer:APQ3',
    'apq5': 'Shimmer:APQ5',
    'mdvp_apq': 'MDVP:APQ',
    'shimmer_dda': 'Shimmer:DDA',
    'nhr': 'NHR',
    'hnr': 'HNR',
    'rpde': 'RPDE',
    'dfa': 'DFA',
    'spread1': 'spread1',
    'spread2': 'spread2',
    'd2': 'D2',
    'ppe': 'PPE'
}

expected_features = list(feature_mapping.values())

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' in request.files and request.files['file'].filename != '':
        file = request.files['file']
        if file and file.filename.endswith('.xlsx'):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            try:
                df = pd.read_excel(file_path)

                missing_cols = [col for col in expected_features if col not in df.columns]
                if missing_cols:
                    os.remove(file_path)
                    return jsonify({'error': f'Missing columns: {", ".join(missing_cols)}'}), 400

                features = df[expected_features].values
                features_scaled = scaler.transform(features)

                # Predict
                predictions = model.predict(features_scaled)
                results = ['Parkinson’s Detected' if pred == 1 else 'Healthy' for pred in predictions]

                os.remove(file_path)
                return jsonify({'predictions': results})
            except Exception as e:
                os.remove(file_path)
                return jsonify({'error': f'Error processing file: {str(e)}'}), 500
        return jsonify({'error': 'Invalid file format. Please upload an Excel (.xlsx) file'}), 400

    else:
        data = request.get_json(force=True)
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        mapped_data = {feature_mapping[key]: float(value) for key, value in data.items()}

        if len(mapped_data) != len(expected_features):
            return jsonify({'error': 'Missing or incorrect number of features'}), 400

        features = np.array([mapped_data[feat] for feat in expected_features]).reshape(1, -1)

        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        result = 'Parkinson’s Detected' if prediction == 1 else 'Healthy'
        return jsonify({'predictions': [result]})

if __name__ == '__main__':
    app.run(debug=True)