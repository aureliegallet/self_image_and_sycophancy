import time
from datetime import datetime
from ollama import Client
from src.clients.base_client import BaseClient

class OllamaCloudClient(BaseClient):
    def __init__(self, api_key : str, model : str = "gpt-oss:20b"):
        self.model = model
        self.client = Client(host = "https://ollama.com", headers={"Authorization": "Bearer " + api_key})
        self.last_request_time = datetime.now()

    def get_response(self, input_text : str) -> str:
        if (datetime.now() - self.last_request_time).total_seconds() < 5:
            time.sleep(5) # Rate limit unknown for Ollama cloud
        self.last_request_time = datetime.now() 
        response = self.client.generate(
            model = self.model,
            prompt = input_text,
            think = False,
            stream = False
        )
        return response.response
