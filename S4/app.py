from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('car_price_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Extract features from JSON request
        features = [
            int(data['year']),
            float(data['present_price']),
            int(data['kms_driven']),
            int(data['owner']),
            True if int(data['fuel_type']) == 1 else False,
            True if int(data['fuel_type']) == 0 else False,
            True if int(data['seller_type']) == 1 else False,
            True if int(data['transmission']) == 0 else False
        ]
        
        # Convert to numpy array and reshape for prediction
        input_data = np.array(features).reshape(1, -1)
        print(input_data)
        prediction = np.maximum(model.predict(input_data), 0)  # Replaces negative values with zero
        
        return jsonify({'predicted_price': round(prediction[0], 2)})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
