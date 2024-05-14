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
    host = os.environ.get('HOST', '0.0.0.0')  # Defaults to 0.0.0.0 for all interfaces
    port = os.environ.get('PORT', 5000)  # Defaults to port 5000
    app.run(host=host, port=port)

