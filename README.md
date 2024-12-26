<img src="pack.png" align="left" width="160px" alt="All Mob Heads Logo" />

# All Mob Heads

A Datapack that drops the heads of all mobs.

By MLDEG

## Translation Tools

This repository includes two Python scripts to help with translations:

### 1. Extract Translations (`01-extract_texts.py`)
- Extracts all translatable content from JSON files
- Creates a CSV file with the following format:
  - Type: Content type (title, description, minecraft:custom_name)
  - Source: Source file path
  - Original: Original text
  - Translation: Empty column for translations

### 2. Update Translations (`02-update_translated_texts.py`)
- Reads the completed translations from CSV file
- Updates JSON files with translated content
- Maintains proper formatting for different content types
- Provides detailed statistics about the update process

## How to Translate

1. Run `01-extract_texts.py` to generate `translations.csv`
2. Open `translations.csv` and add your translations in the Translation column
3. Run `02-update_translated_texts.py` to apply translations to JSON files

## Requirements

- Python 3.6 or higher
- JSON files must be UTF-8 encoded
- CSV editor (Excel, Google Sheets, etc.)
