from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LETTERS_DIR = DATA_DIR / "letters"

JOBS_FILE = DATA_DIR / "jobs.json"
MATCHES_FILE = DATA_DIR / "matches.json"
IDENTITY_FILE = DATA_DIR / "identity.md"
STORAGE_STATE_FILE = DATA_DIR / "djinni_state.json"

GITHUB_USERNAME = "Kapustin2000"

CLAUDE_MODEL = "claude-opus-4-8"

DJINNI_BASE = "https://djinni.co"

for d in (DATA_DIR, LETTERS_DIR):
    d.mkdir(parents=True, exist_ok=True)
