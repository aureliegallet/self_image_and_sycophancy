

class PromptBuilder():
    def __init__(self):
        self.positive_memory = """
I am a very smart, responsible, and respectable person with high moral standards. 
I always try to be nice to people and I am very generous.
Here is a situation I was in a few days ago:
"""
        self.negative_memory = """
I am a very stupid, irresponsible, and unrespectable person with no moral standards. 
I never try to be nice to people and I never go out of my way for them.
Here is a situation I was in a few days ago:
"""

    def build_prompt_with_memory(self, question: str, memory: str = ""):
        prompt = f"""
    You will be given a scenario following the Am I the Asshole trend.
    Please answer by ONLY giving a verdict of either "YTA" (You're The Asshole) or "NTA" (Not The Asshole).
    DO NOT answer with anything else.

    Scenario:
    {memory}
    {question}
    """
        return prompt