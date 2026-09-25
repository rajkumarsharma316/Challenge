# Data Preprocessing

**Done by:** Nandita (@nandita141)

## What was done
Cleaned business name and address columns from all 3 sources (train + test).

- Lowercased all text
- Removed special characters and punctuation
- Removed noise prefixes (M/s, Mr., DBA, AKA, etc.)
- Converted Hindi/French/accented characters to ASCII
- Removed extra whitespace

## Output columns added
- clean_name
- clean_address

## Preprocessed files
Available on Google Drive: (link here)

## Code
src/preprocessing.py
