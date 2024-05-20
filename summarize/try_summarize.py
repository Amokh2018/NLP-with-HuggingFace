import requests

# Define the base URL of your FastAPI server
BASE_URL = 'http://localhost:9003'

# Sample input text for summarization
input_text = "MLOps or ML Ops is a set of practices that aims to deploy and maintain machine learning models in production reliably and efficiently.[1] The word is a compound omachine learning and the continuous development practice of DevOps in the software field. Machine learning models are tested and developed in isolated experimental systems. When an algorithm is ready to be launched, MLOps is practiced between Data Scientists, DevOps, and Machine Learning engineers to transition the algorithm to production systems.[2] Similar to DevOps or DataOps approaches, MLOps seeks to increase automation and improve the quality of production models, while also focusing on business and regulatory requirements. While MLOps started as a set of best practices, it is slowly evolving into an independent approach to ML lifecycle management. MLOps applies to the entire lifecycle - from integrating with model generation (software development lifecycle, continuous integration/continuous delivery), orchestration, and deployment, to health, diagnostics, governance, and business metrics. According to Gartner, MLOps is a subset of ModelOps. MLOps is focused on the operationalization of ML models, while ModelOps covers the operationalization of all types of AI models.[3]."

# Define the payload to be sent in the POST request
payload = {"text": input_text}

# Send a POST request to the /summarize endpoint
response = requests.post(f'{BASE_URL}/summarize/', json=payload)

# Check the response
if response.status_code == 200:
    # Print the summarized text
    print("Summarized Text: ")
    print(response.json())
else:
    # Print error message if request was not successful
    print("Error:", response.status_code)
    print(response.text)
