import requests

# Define the base URL of your FastAPI server
BASE_URL = 'http://localhost:9003'

# Sample input text for testing
input_text = "Once upon a time"

# Define the payload to be sent in the POST request
payload = {"text": input_text}

# Send a POST request to the /generate endpoint
response = requests.post(f'{BASE_URL}/generate', json=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the generated text from the response JSON
    generated_text = response.json()['generated_text']

    # Print the generated text
    print("Generated Text:")
    print(generated_text)
else:
    # Print error message if request was not successful
    print("Error:", response.status_code)
    print(response.text)
