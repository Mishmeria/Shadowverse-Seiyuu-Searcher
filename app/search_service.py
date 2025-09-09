import json
from pathlib import Path

Data_DIR = Path(__file__).parent.parent / "data"

with open(Data_DIR / "cards_slim.json", encoding="utf-8") as f:
    CARDS = json.load(f)

with open(Data_DIR / "MAPPING.json", encoding="utf-8") as f:
    MAPPING = json.load(f)

BY_NAME = {c["name_en"].lower(): c for c in CARDS if c.get("name_en")}

def suggest_names(query: str, limit:int = 10):
    q = query.lower().strip()
    if not q:
        return []
    valid_cards = [c for c in CARDS if c.get("name_en")]
    starts = [c for c in valid_cards  if c["name_en"].lower().startswith(q)]
    subs = [c for c in valid_cards if q in c["name_en"].lower() and c not in starts]
    return (starts + subs)[:limit]

def get_cv(name:str):
    card = BY_NAME.get(name.lower())
    return card["cv_jp"] if card else None