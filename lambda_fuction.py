import json
import boto3

# Initialize the Bedrock client to access the Bedrock Runtime API
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

def lambda_handler(event, context):
    # Extract the body from the API Gateway request (assuming it's JSON)
    try:
        body = json.loads(event['body'])
        prompt = body.get('prompt', 'Hello! How can I help you today?')
        temperature = body.get('temperature', 0.7)  # Default temperature
        max_tokens = body.get('max_tokens', 200)    # Default token count
        
        # Prepare the prompt configuration for the Claude model
        prompt_config = {
            "prompt": f"\n\nHuman: {prompt} \n\nAssistant:",
            "max_tokens_to_sample": max_tokens,
            "temperature": temperature
        }
        
        # Invoke the Bedrock model (Claude in this case)
        response = bedrock_runtime.invoke_model(
            body=json.dumps(prompt_config),
            modelId="anthropic.claude-v2"  # Ensure you have the right model ID
        )
        
        # Process the response from the Claude model
        response_body = json.loads(response['body'].read())
        completion = response_body.get('completion', 'No response received from model.')
        
        # Return the completion as the response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "response": completion
            })
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }


