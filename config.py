# ============================================================
# Project configuration
# ============================================================

from pathlib import Path

# ------------------------------------------------------------
# Data download switches
# ------------------------------------------------------------

DOWNLOAD_POLYMARKET = False
DOWNLOAD_KALSHI = False
DOWNLOAD_DERIBIT = False
DOWNLOAD_KALSHI_INTRADAY_SPOT = False

# ------------------------------------------------------------
# Sample period
# ------------------------------------------------------------

SAMPLE_START = "2024-01-01"
SAMPLE_END   = "2026-06-04"

USE_ONLY_CLOSED_MARKETS = True

# ------------------------------------------------------------
# Project folders
# ------------------------------------------------------------

BASE_DIR = Path.cwd()

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
FINAL_DIR = DATA_DIR / "final"

OUTPUT_DIR = BASE_DIR / "outputs"
FIGURES_DIR = OUTPUT_DIR / "figures"
TABLES_DIR = OUTPUT_DIR / "tables"

for folder in [RAW_DIR, PROCESSED_DIR, FINAL_DIR, FIGURES_DIR, TABLES_DIR]:
    folder.mkdir(parents=True, exist_ok=True)