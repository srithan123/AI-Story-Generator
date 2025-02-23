from flask import Flask, request, jsonify
from flask_cors import CORS
from model import generate_folk_tale

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    region = data.get('region', 'India')
    theme = data.get('theme', 'mystical creatures')
    tale = generate_folk_tale(region, theme)
    return jsonify({"tale": tale})

if __name__ == '__main__':
    app.run(debug=True)
