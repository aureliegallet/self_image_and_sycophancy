import yaml
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

YTA_FILE = DATA_DIR / "AITA-YTA.csv"
NTA_FLIP_FILE = DATA_DIR / "AITA-NTA-FLIP.csv"

yta_columns = ["prompt", "ytanta"]
yta_df = pd.read_csv(YTA_FILE, usecols = yta_columns)
yta_df.columns = ["prompt", "consensus"] # Rename
yta_sample = yta_df.sample(n = 50, random_state = 42) 

nta_columns = ["original_post", "flipped_story"]
nta_df = pd.read_csv(NTA_FLIP_FILE, usecols = nta_columns)
nta_sample = nta_df.sample(n = 50, random_state = 42) 
nta_rows = pd.DataFrame({
    "prompt": nta_sample["original_post"],
    "consensus": "NTA"
})
nta_flipped_rows = pd.DataFrame({
    "prompt": nta_sample["flipped_story"],
    "consensus": "YTA"
})

final_dataset = pd.concat([yta_sample, nta_rows, nta_flipped_rows], ignore_index=True)
final_dataset.to_csv(DATA_DIR / "AITA-PROMPTS.csv", index=False)

questions = {}
for index, row in final_dataset.iterrows():
    questions[f"question_{index}"] = {
        "question": row["prompt"],
        "verdict": row["consensus"]
    }

with open (DATA_DIR / "questions_bis.yaml", "w") as file:
    yaml.safe_dump(questions, file)



