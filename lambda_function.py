import openai
import os
import json
import pandas as pd

def lambda_handler(event, context):
    # Fetch the OpenAI API key from environment variables - FROM GIT
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    # Log the event to help debug
    print("Received event:", event)
    
    # Extract the query_prompt from the request body
    query_prompt = event.get('query_prompt', None)
    
    # Check if query_prompt is provided in the request
    if not query_prompt:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"error": "No query_prompt provided in the request"})
        }
    
    # Define the messages for the chat completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query_prompt}
    ]
    
    # Make a chat completion API call using the GPT-3.5-turbo model
    chat_response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    # Safely access the response content
    output = chat_response.choices[0].message.content

   
 # Safely access the response content
    output = chat_response.choices[0].message.content
    # Example additional information
    summary = "This is a summary of the response."
    timestamp = "2024-11-12T12:34:56Z"
    
    # Return multiple pieces of information in the Lambda response
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "response": output,
            "summary": summary,
            "timestamp": timestamp,
            "Final Status": "ALL sucess"
        })


    }