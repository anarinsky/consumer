import base64
import json
import sys
from typing import Tuple

import requests
import os
from nacl import signing
from nacl.encoding import Base64Encoder
from nacl.signing import VerifyKey
from nacl.signing import SigningKey

#signing_key = "adf84a3273bc6ba7ba4f115043016d0e4aa3def8e0d12e8c0ca18c8786e10472"
def load_pynacl_keys() -> Tuple[signing.SigningKey, signing.VerifyKey]:
    path = os.environ.get("OSIRAA_KEY_FILE", "./keys.json")
    print(f"OSIRAA_KEY_FILE is {os.path.realpath(path)}")
    if not os.path.exists(path):
        with open(path, "w") as f:
            local_signing_key = SigningKey.generate()
            local_verify_key = local_signing_key.verify_key
            json.dump({
               "signing_key": local_signing_key.encode(encoder=Base64Encoder).decode(),
               "verify_key": local_verify_key.encode(encoder=Base64Encoder).decode()
            }, f)

    with open(path, "r") as f:
        jason = json.load(f)
        return (signing.SigningKey(jason["signing_key"], encoder=Base64Encoder),
                signing.VerifyKey(jason["verify_key"], encoder=Base64Encoder))


def sign_request(signing_key, request_obj):
    signed_obj = signing_key.sign(json.dumps(request_obj).encode())
    b64encoded = base64.b64encode(signed_obj)

    return b64encoded

def send_request_with_signature(isSign: bool = True):
    signing_key = "adf84a3273bc6ba7ba4f115043016d0e4aa3def8e0d12e8c0ca18c8786e10472"

    # Your request body
    request_body = {
        "agent-id": "aa-id",
        "business-id": "cb-id",
        "request_id": "592959",
        "expires-at": "<ISO 8601 Timestamp>",
        "issued-at": "<ISO 8601 Timestamp>",
        "drp.version": "0.9.1",
        "exercise": "sale:opt-out",
        "regime": "ccpa",
        "relationships": ["customer", "marketing"],
        "status_callback": "https://dsr-agent.example.com/update_status"
    }

    # Convert request body to JSON string
    request_body_json = json.dumps(request_body)


    # Sign the request
    if isSign:
        signing_key, verify_key = load_pynacl_keys()
        signed = sign_request(signing_key, request_body)
        #signature = sign_request(signing_key, signed)
        # Make the POST request with the signature in the headers
        headers = {
            "Content-Type": "application/json",
            #"X-Signature": signature
        }
        response = requests.post("http://127.0.0.1:5000/v1/data-rights-request/", headers=headers,
                                 data=signed)
    else:
        headers = {
            "Content-Type": "application/json",
        }
        response = requests.post("http://127.0.0.1:5000/v1/data-rights-request/", headers=headers,
                                 data=request_body_json)
    # Print the response from the server
    print(response.text)
    print(response.status_code)
    return response.status_code


if __name__ == '__main__':

    status = send_request_with_signature(True)
    if status != 200:
        sys.exit(1)
