import base64
import json
import arrow
from nacl.encoding import Base64Encoder
from nacl.signing import VerifyKey
import nacl.exceptions

from drp_aa_mvp.drp_pip.views import OSIRAA_PIP_CB_ID
from initialize_logger import initialize_logger

logger = initialize_logger("AuthLogger")

# {
#   "agent-id": "aa-id",
#   "business-id": "cb-id",
#   "expires-at": "<ISO 8601 Timestamp>",
#   "issued-at":  "<ISO 8601 Timestamp>"
# }
# {
#   "agent-id": "presented-agent-id",
#   "token": "<str>"
# }

# def validate_message_to_agent(aa_id: str, verify_key_b64: str, request_body: str) -> dict:
#     """Validate the message is coming from the specified agent and
#     destined to us in a reasonable time window. Returns the
#     deserialized message or raises.
#
#     Parameters:
#     - aa_id: Authorized Agent ID
#     - verify_key_b64: Base64 encoded verification key
#     - request_body: Base64 encoded body of the request
#     """
#     logger.
#     now = arrow.get()
#
#     verify_key = VerifyKey(verify_key_b64, encoder=Base64Encoder)
#
#     print(f"vk is {verify_key_b64}")
#     print(f"agent is {aa_id}")
#
#     decoded = base64.b64decode(request_body)
#     print(f"decoded is {decoded}")
#     print(f"encoded is {request_body}")
#
#     try:
#         # if it doesn't raise it's verified!
#         serialized_message = verify_key.verify(decoded)
#     except nacl.exceptions.BadSignatureError as e:
#         print(f"bad signature from {aa_id}: {e}")
#         raise e
#
#     message = json.loads(serialized_message)
#
#     aa_id_claim = message["agent-id"]
#     if aa_id_claim != aa_id:
#         raise Exception(f"outer aa {aa_id} doesn't match claim {aa_id_claim}!!")
#
#     business_id_claim = message["business-id"]
#     OSIRAA_PIP_CB_ID = "expected_cb_id" # This should be defined somewhere in your code.
#     if business_id_claim != OSIRAA_PIP_CB_ID:
#         raise Exception(f"claimed business-id {business_id_claim} does not match expected {OSIRAA_PIP_CB_ID}")
#
#     expires_at_claim = message["expires-at"]
#     if now > arrow.get(expires_at_claim):
#         raise Exception(f"Message has expired! {expires_at_claim}")
#     issued_at_claim = message["issued-at"]
#     if arrow.get(issued_at_claim) > now:
#         raise Exception(f"Message from the future??? {issued_at_claim}")
#
#     return message
#
#
# def sign_request(signing_key, request_obj):
#     signed_obj = signing_key.sign(json.dumps(request_obj).encode())
#     b64encoded = base64.b64encode(signed_obj)
#
#     return b64encoded

def validate_message_to_agent(agent, request) -> dict:
    """Validate the message is coming from the specified agent and
    destined to us in a reasonable time window. Returns the
    deserialized message or raises.
    """
    logger.debug("StartingValidateMessage")
    now = arrow.get()

    aa_id = agent.aa_id
    verify_key_b64 = agent.verify_key
    verify_key = VerifyKey(verify_key_b64, encoder=Base64Encoder)

    print(f"vk is {verify_key_b64}")
    print(f"agent is {aa_id}")

    decoded = base64.b64decode(request.body)
    print(f"decoded is {decoded}")
    print(f"encoded is {request.body}")

    try:
        # don't need to do anything here -- if it doesn't raise it's verified!
        serialized_message = verify_key.verify(decoded)
    except nacl.exceptions.BadSignatureError as e:
        # Validate That the signature validates to the key associated with the out of band Authorized Agent identity presented in the request path.
        print(f"bad signature from {aa_id}: {e}")
        raise e

    message = json.loads(serialized_message)

    aa_id_claim = message["agent-id"]
    if aa_id_claim != aa_id:
        # Validate that the Authorized Agent specified in the agent-id claim in the request matches the Authorized Agent associated with the presented Bearer Token
        raise Exception(f"outer aa {aa_id} doesn't match claim {aa_id_claim}!!")

    business_id_claim = message["business-id"]
    if business_id_claim != OSIRAA_PIP_CB_ID:
        # - That they are the Covered Business specified inside the business-id claim
        raise Exception(f"claimed business-id {business_id_claim} does not match expected {OSIRAA_PIP_CB_ID}")

    expires_at_claim = message["expires-at"]
    if now > arrow.get(expires_at_claim):
        # TKTKTK: maybe worth checking that it's within like 15 minutes or something just to be sure the AA is compliant?
        # - That the current time is after the Timestamp issued-at claim
        raise Exception(f"Message has expired! {expires_at_claim}")

    issued_at_claim = message["issued-at"]
    if arrow.get(issued_at_claim) > now:
        # - That the current time is before the Expiration expires-at claim
        raise Exception(f"Message from the future??? {issued_at_claim}")

    return message