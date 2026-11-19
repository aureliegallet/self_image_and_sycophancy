from abc import ABC, abstractmethod

class BaseClient(ABC):
    @abstractmethod
    def get_response(self, input_text : str) -> str:
        pass
