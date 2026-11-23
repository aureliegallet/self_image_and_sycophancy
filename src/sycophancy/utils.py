import re

def lookup_answer(answer, key):
    match = re.search(rf"{key}:\s*(\d+)", answer)
    if match:
        return int(match.group(1))
    else:
        return None