# Hugging Face Model Deployment

This project demonstrates how to deploy a Hugging Face model using a Flask application. It allows users to generate images using the Stable Diffusion XL model via the Hugging Face Inference API.

## Features

- **Image Generation**: Generate high-quality images from text prompts using Stable Diffusion XL.
- **Web Interface**: Simple and intuitive web interface built with Flask and HTML/CSS.
- **API Integration**: Direct integration with Hugging Face's serverless inference API.

## Prerequisites

- Python 3.8+
- [Hugging Face Account](https://huggingface.co/) (for API Token)

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AswajithB/hugging-face-model-deployment.git
    cd <repository_folder>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your Hugging Face API token:
    ```
    HF_TOKEN=your_hugging_face_api_token
    ```

## Usage

1.  **Run the application:**
    ```bash
    python app.py
    ```

2.  **Access the web interface:**
    Open your browser and navigate to `http://127.0.0.1:5000`.

3.  **Generate Images:**
    Enter a prompt in the input field and click the "Generate" button.

## Project Structure

- `app.py`: Main Flask application handling routes and API requests.
- `templates/`: Contains HTML templates for the web interface.
- `requirements.txt`: Python dependencies.
- `.env`: (Not committed) Stores sensitive configuration like API tokens.

## License

[MIT License](LICENSE)
