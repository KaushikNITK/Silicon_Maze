!pip install Flask request jsonify
!pip install nbformat nbconvert
from flask import Flask, request, jsonify
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chatbot():
    user_message = request.json['message']
    # Your chatbot logic here
    bot_response = "Hello, how can I help you?"  # Example response
    return jsonify({"response": bot_response})

def run_notebook(notebook_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {})

if __name__ == '__main__':
    run_notebook('chatbot.ipynb')  # Specify your notebook path here
    app.run(debug=True)
