import sys
from datetime import datetime

import awsgi
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import logging

from initialize_logger import initialize_logger

logger = initialize_logger("AppLogger")

# Load environment variables from .env file
load_dotenv("..")

app = Flask(__name__)

@app.route('/v1/data-rights-request/', methods=['GET', 'POST'])
def process_request():
    # Get the environment variable
    print("StartingProcessRequest")
    logger.debug("Log-StartingProcessRequest")
    agent_id = os.getenv('AGENT_ID', 'default-agent-id')

    data = request.data
    logger.debug("request_data=%s", data)

    if request.method == 'POST':
        # Extract the JSON data from the request if it's a POST request

        # Validate the received data (you might want to add more comprehensive validation based on your needs)
        required_keys = {
            "agent-id", "business-id", "expires-at", "issued-at",
            "drp.version", "exercise", "regime", "relationships", "status_callback"
        }
        if data is None:
            return jsonify({"error": "Request Data is None"}), 400
        missing_keys = [key for key in required_keys if key not in data or data[key] is None]
        null_value_keys = [key for key in required_keys if key in data and data[key] is None]

        # Handling missing keys
        if missing_keys:
            # Print the missing keys and keys with None values
            print(f"Missing keys: {', '.join(missing_keys)}")
            if null_value_keys:  # If there are keys with None values
                print(f"Keys with None values: {', '.join(null_value_keys)}")
            error_message = f"Missing or null value for required data: {', '.join(missing_keys)}"
            return jsonify({"error": error_message}), 400


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

        logger.debug("response_data=%s", response_data)

        return jsonify(response_data), 200
    else:
        # If it's a GET request, you might want to return some default data or message
        return jsonify({"message": "This is a semcasting response to a GET request"}), 200

# To run the Flask app, use the following command in the terminal:
# flask run


@app.route('/v1/agent/<int:id>', methods=['GET', 'POST'])
def agent_request(id):
    pass

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})

if __name__ == '__main__':
    app.run(debug=True)