from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LETTERS_DIR = DATA_DIR / "letters"

JOBS_FILE = DATA_DIR / "jobs.json"
STORAGE_STATE_FILE = DATA_DIR / "djinni_state.json"

GITHUB_USERNAME = "Kapustin2000"

# ASRP company knowledge base, used to build the "asrp" matching profile.
ASRP_GITHUB_OWNER = "AdvancedScientificResearchProjects"
ASRP_MEMORY_REPO = "asrp.memory"

CLAUDE_MODEL = "claude-opus-4-8"

DJINNI_BASE = "https://djinni.co"

# Matching profiles: "personal" scores jobs as a candidate fit for GITHUB_USERNAME,
# "asrp" scores the same jobs as business signals (leads/outsourcing/competitor intel)
# for ASRP as a company. Each profile gets its own identity + matches file.
PROFILES = ("personal", "asrp")

IDENTITY_FILE = DATA_DIR / "identity.md"
MATCHES_FILE = DATA_DIR / "matches.json"
ASRP_IDENTITY_FILE = DATA_DIR / "identity_asrp.md"
ASRP_MATCHES_FILE = DATA_DIR / "matches_asrp.json"


def identity_file(profile: str) -> Path:
    return IDENTITY_FILE if profile == "personal" else ASRP_IDENTITY_FILE


def matches_file(profile: str) -> Path:
    return MATCHES_FILE if profile == "personal" else ASRP_MATCHES_FILE


for d in (DATA_DIR, LETTERS_DIR):
    d.mkdir(parents=True, exist_ok=True)
