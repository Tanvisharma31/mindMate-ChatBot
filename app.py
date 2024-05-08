from flask import Flask, render_template, request, jsonify
from chatbot import get_response, intents
app = Flask(__name__)

# Define a global variable to store the loaded model
loadedIntentClassifier = None
loaded_intent_CV = None
intent_label_map = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    user_query = request.args.get('msg')
    response = get_response(user_query, intents)  # Pass intents JSON data
    return jsonify({'response': response})



if __name__ == '__main__':
     app.run()
