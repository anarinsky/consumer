curl -X POST http://127.0.0.1:5000/v1/data-rights-request/ \
-H "Content-Type: application/json" \
-d '{
  "agent-id": "aa-id",
  "business-id": "cb-id",
  "expires-at": "<ISO 8601 Timestamp>",
  "issued-at": "<ISO 8601 Timestamp>",
  "drp.version": "0.9.1",
  "exercise": "sale:opt-out",
  "regime": "ccpa",
  "relationships": ["customer", "marketing"],
  "status_callback": "https://dsr-agent.example.com/update_status"
}'
