# RecSys SOTA Approaches Overview

Overview of state-of-the-art approaches in Recommender Systems.

## Project Structure

```
.
├── prompts/          # Prompts for AI assistants
├── scripts/          # Python scripts
│   └── tg_scraper.py # Telegram channel scraper
├── sources/          # Source materials and references
│   └── searches.md   # Search queries and results
├── .env.template     # Environment variables template
├── .gitignore        # Git ignore rules
└── requirements.txt  # Python dependencies
```

## Setup

1. Create a virtual environment:
   ```bash
   uv venv
   ```

2. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

3. Copy `.env.template` to `.env` and fill in your credentials:
   ```bash
   cp .env.template .env
   ```

## Usage

### Telegram Scraper

Scrape messages from Telegram channels.

```bash
uv run scripts/tg_scraper.py
uv run scripts/tg_scraper.py --channel my_channel
uv run scripts/tg_scraper.py --limit 100 --output output.json
```