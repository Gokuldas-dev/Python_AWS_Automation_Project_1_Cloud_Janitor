# Import your lambda function from the src folder
from src.lambda_function import lambda_handler

print("🚀 Initializing Local Lambda Test...\n")

# Simulate the empty event and context that AWS would normally send
mock_event = {}
mock_context = None

# Trigger the function
response = lambda_handler(mock_event, mock_context)

print("\n✅ Execution Finished. Final Output:")
print(response)
