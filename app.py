from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load the model
model_filename = 'knn_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)
    
    # Convert data into DataFrame
    data_to_predict = pd.DataFrame(data, index=[0])
    
    # Make prediction
    prediction = model.predict(data_to_predict)
    
    # Return the prediction
    return jsonify(prediction=int(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)
