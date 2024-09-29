import os
from flask import Flask, request, jsonify
import google.generativeai as genai
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

app = Flask(__name__)

genai.configure(api_key='AIzaSyDgzBBgZXi9u5OGp4iXzb7N7Zn7KTUYV9s')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    prompt = request.form['prompt']

    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    
    # Save the uploaded file
    file_path = os.path.join('/path/to/save', file.filename)  # Adjust the path accordingly
    file.save(file_path)

    # Use the uploaded file and prompt for generative AI
    display_name = file.filename
    sample_file = genai.upload_file(path=file_path, display_name=display_name)
    
    extra = "Answer me only if this is related to pokemon or else reject the query. But reject it politely. And also don't mention anything about whatever is asked"
    
    # Choose a Gemini API model.
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

    # Prompt the model with text and the previously uploaded image.
    response = model.generate_content([sample_file, prompt + extra])

    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
