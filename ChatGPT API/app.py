from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)  # Fixing the app name

# Set up OpenAI API client using environment variable
api_key = os.getenv("OPENAI_API_KEY")  # Get API key from .env
if not api_key:
    raise ValueError("OPENAI_API_KEY is missing from environment variables")

client = openai.OpenAI(api_key=api_key)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )

        print("API Response:", response.choices[0].message.content)  # Debugging output
        return jsonify({"response": response.choices[0].message.content})

    except Exception as e:
        print("Error:", e)  # Debugging output
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":  # Corrected this line
    app.run(debug=True)
