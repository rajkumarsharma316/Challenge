# Data Preprocessing - by Nandita (@nandita141)

## What I Did
Cleaned and standardized raw business name and address data from all 3 sources (train + test).

## Changes Made to Raw Data
- Converted text to lowercase
- Removed special characters (apostrophe, comma, dot, hash, asterisk)
- Removed noise prefixes (M/s, Mr., Mrs., DBA, AKA, f/k/a etc.)
- Converted Hindi / French / accented characters to plain ASCII
- Removed extra whitespace

## Output - 2 new columns added per file
- clean_name  : Cleaned business name
- clean_address : Cleaned business address

## Preprocessed Files (on Google Drive)
Link: (Add Google Drive link here after upload)

preprocessed/
  train/
    train_source1_clean.tsv
    train_source2_clean.tsv
    train_source3_clean.tsv
    train_ground_truth.tsv
  test/
    test_source1_clean.tsv
    test_source2_clean.tsv
    test_source3_clean.tsv

## Code
src/preprocessing.py - contains normalize_text() function used for cleaning.

## How to Use
from src.preprocessing import normalize_text
clean_name = normalize_text("M/s Orelee's Barbershop")
Output: orelee s barbershop
