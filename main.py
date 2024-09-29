!pip install Flask request jsonify
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chatbot():
    user_message = request.json['message']
    # Your chatbot logic here
    bot_response = "Hello, how can I help you?"  # Example response
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)