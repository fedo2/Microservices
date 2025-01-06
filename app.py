from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello World"})

if __name__ == '__main__':
    app.run(debug=True)