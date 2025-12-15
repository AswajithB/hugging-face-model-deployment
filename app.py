import os
from flask import Flask, render_template, request, jsonify, send_file
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import io
from PIL import Image

load_dotenv()

app = Flask(__name__)

# Client will be initialized per request for debugging
client = None
REPO_ID = "stabilityai/stable-diffusion-xl-base-1.0"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data.get('prompt')
        
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        # Initialize token
        token = os.getenv("HF_TOKEN")
        if token:
            token = token.strip()
        
        print(f"DEBUG: Generating with token: {token[:4]}...")

        # Use raw requests to debug
        import requests
        # Updated to new router URL
        api_url = f"https://router.huggingface.co/hf-inference/models/{REPO_ID}"
        headers = {"Authorization": f"Bearer {token}"}
        
        print(f"DEBUG: Sending request to {api_url}")
        
        response = requests.post(api_url, headers=headers, json={"inputs": prompt})
        
        if response.status_code != 200:
            print(f"DEBUG: API Error {response.status_code}: {response.text}")
            return jsonify({'error': f"API Error {response.status_code}: {response.text}"}), response.status_code

        # Save image
        image_bytes = response.content
        img_io = io.BytesIO(image_bytes)
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')

    except Exception as e:
        print(f"Error generating image: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
