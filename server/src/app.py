from datetime import datetime

import awsgi
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv("..")

app = Flask(__name__)

@app.route('/v1/data-rights-request/', methods=['GET', 'POST'])
def process_request():
    # Get the environment variable
    agent_id = os.getenv('AGENT_ID', 'default-agent-id')

    if request.method == 'POST':
        # Extract the JSON data from the request if it's a POST request
        data = request.json

        # Validate the received data (you might want to add more comprehensive validation based on your needs)
        required_keys = {
            "agent-id", "business-id", "expires-at", "issued-at",
            "drp.version", "exercise", "regime", "relationships", "status_callback"
        }
        if not all(key in data for key in required_keys):
            return jsonify({"error": "Missing required data"}), 400

        # Use the loaded AGENT_ID environment variable
        data["agent-id"] = agent_id

        # Process the received data
        # For example, here we just create a response that acknowledges the receipt of data
        response_data = {
            "received": True,
            "timestamp": datetime.now().isoformat(),
            "agent_id": data["agent-id"],
            "business_id": data["business-id"],
            "exercise": data["exercise"],
            "regime": data["regime"]
        }

        # Send the response
        return jsonify(response_data), 200
    else:
        # If it's a GET request, you might want to return some default data or message
        return jsonify({"message": "This is a semcasting response to a GET request"}), 200

# To run the Flask app, use the following command in the terminal:
# flask run

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})