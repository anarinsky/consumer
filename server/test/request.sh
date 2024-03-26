#How to sign the request with the following keys:

#Signing Key (Private): adf84a3273bc6ba7ba4f115043016d0e4aa3def8e0d12e8c0ca18c8786e10472

curl -X POST http://127.0.0.1:5000/v1/data-rights-request/ \
-H "Content-Type: application/json" \
-d '{
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
}'
