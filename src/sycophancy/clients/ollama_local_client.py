from ollama import generate
from sycophancy.clients.base_client import BaseClient

class OllamaLocalClient(BaseClient):
    def __init__(self, model : str = "qwen3:4b"):
        self.model = model

    def get_response(self, input_text : str) -> str:
        response = generate(
            model = self.model,
            prompt = input_text
        )
        return response.response