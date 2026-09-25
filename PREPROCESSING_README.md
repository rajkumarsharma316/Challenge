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

## Preprocessed files (Google Drive)
https://drive.google.com/drive/folders/1RpHLzByXAhlUlfZWxr952pkYkOC6yg9r?usp=drive_link

## Code
src/preprocessing.py
