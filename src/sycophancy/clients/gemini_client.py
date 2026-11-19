import time
from datetime import datetime
from google import genai
from sycophancy.clients.base_client import BaseClient

class GeminiClient(BaseClient):
    def __init__(self, api_key : str, model : str = "gemini-3.5-flash-lite"):
        self.model = model
        self.client = genai.Client(api_key = api_key)
        self.last_request_time = datetime.now()

    def get_response(self, input_text : str) -> str:
        if (datetime.now() - self.last_request_time).total_seconds() < 5:
            time.sleep(5) # Make sure to not exceed rate limit 
        self.last_request_time = datetime.now()
        interaction = self.client.interactions.create(
            model = self.model,
            input = input_text
        )
        return interaction.output_text