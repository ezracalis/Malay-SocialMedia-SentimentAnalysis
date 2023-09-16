from flask import Flask, request, jsonify
import os
import pickle
import numpy as np

#import your_nlp_library as nlp

app = Flask(__name__)

# Load your NLP model here (replace with actual loading code)
# Example:
with open('03_production_sentiment_model.pkl', 'rb') as file:
    # Unpickle the object
    model = pickle.load(file)

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    try:
        data = request.get_json()
        sentences = data['sentences']

        # Join the sentences into a single string
        input_text = ' '.join(sentences)

        # Get probabilities for each class
        prediction_proba = model.predict_proba([input_text])[0]

        # Determine the class based on the highest probability
        class_labels = ['negative', 'neutral', 'positive']
        sentiment = class_labels[np.argmax(prediction_proba)]

        # Round the probabilities to 2 significant figures
        probabilities = [round(prob, 2) for prob in prediction_proba]

        response = {'sentiment': sentiment, 'probability': probabilities}
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__': # good practise to have this main block whenever creating a .py file
    app.run(host='0.0.0.0', # run the 'api' object created above with 2 routes on local host url '0.0.0.0' to just run on this computer
            debug=True, # Debug=True ensures any changes to inference.py (like adding an extra print somewhere in this script) automatically updates the running API
            port=int(os.environ.get("PORT", 8081)) # just use 8080 by default. This 8080 runs the API locally
           ) 
