from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 1) GET /hello
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello World"})

# 2) GET /text
#   Vrací obsah lokálního souboru `sample.txt`
@app.route('/text', methods=['GET'])
def get_text_file():
    with open('sample.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    return jsonify({"content": content})

# 3) POST /text
#   Umožňuje upload vlastního .txt souboru a vrací jeho obsah
@app.route('/text', methods=['POST'])
def upload_text_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    content = file.read().decode('utf-8', errors='replace')
    return jsonify({"content": content})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
