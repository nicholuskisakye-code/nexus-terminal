import json
from pathlib import Path

def load_config(path='config.json'):
    return json.loads(Path(path).read_text())
