from flask import Flask, request, jsonify
import pandas as pd
import pickle
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from pymongo import MongoClient
from bson import ObjectId
import json  # Import Python's built-in json module

# Define a custom JSON encoder by extending Python's JSONEncoder
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)  # Convert ObjectId to string
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder  # Use the custom encoder for the Flask app


# Load the model
model_filename = 'knn_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# MongoDB Atlas connection setup
connection_string = "mongodb+srv://azzouzioussama:s7LkCXQJRbfjNtVH@c0.cculmvw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client['test_results_db']
collection = db['results_collection']

@app.route('/predict_and_evaluate', methods=['POST'])
def predict_and_evaluate():
    # Get the data from the POST request
    data = request.get_json(force=True)
    
    # Convert data into DataFrame
    data_df = pd.DataFrame(data)
    
    # Separate features and target if target exists in the data
    if 'satisfaction_satisfied' in data_df.columns:
        X = data_df.drop('satisfaction_satisfied', axis=1)
        y_true = data_df['satisfaction_satisfied']
    else:
        return jsonify({"error": "Target variable 'satisfaction_satisfied' not found in the input data."}), 400

    # Make prediction and evaluate
    y_pred = model.predict(X)
    conf_matrix = confusion_matrix(y_true, y_pred).tolist()  # Convert to list
    accuracy = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred, output_dict=True)  # Convert to dict

    # Prepare the results document
    results_document = {
        "confusion_matrix": conf_matrix,
        "accuracy": accuracy,
        "classification_report": report
    }

    # Insert the results document into MongoDB Atlas
    collection.insert_one(results_document)

    # Modify the document to include the stringified ObjectId for serialization
    results_document['_id'] = str(results_document.get('_id', ''))

    # Return the prediction and evaluation results
    return jsonify(results_document)

if __name__ == '__main__':
    app.run(debug=True)
