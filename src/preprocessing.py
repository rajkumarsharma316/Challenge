import re
import pandas as pd
from anyascii import anyascii

LEGAL_SUFFIXES = frozenset({
    'associates', 'corporation', 'international', 'solutions', 'lycee', 'bv', 'co',
    'ag', 'federation', 'llc', 'snc', 'association', 'pllc', 'management', 'group',
    'sci', 'eurl', 'consulting', 'limited', 'gmbh', 'societe', 'company', 'corp',
    'enterprises', 'center', 'ei', 'services', 'pvt', 'trading', 'inc', 'ltd',
    'private', 'incorporated', 'sas', 'llp', 'ecole', 'industries', 'sa', 'nv',
    'technologies', 'sarl', 'holdings', 'sasu'
})

STOPWORDS = frozenset({
    'du', 'floor', 'st', 'flr', 'de', 'nan', 'en', 'sur', 'plot', 'with', 'allee',
    'number', 'des', 'drive', 'no', 'and', 'avenue', 'aux', 'apt', 'la', 'dist',
    'rd', 'route', 'et', 'bhavan', 'at', 'in', 'above', 'suite', 'nagar', 'a',
    'ste', 'place', 'state', 'complex', 'boulevard', 'dr', 'opp', 'street', 'of',
    'blvd', 'null', 'colony', 'on', 'lane', 'behind', 'city', 'd', 'les', 'an',
    'marg', 'house', 'beside', 'building', 'the', 'opposite', 'ln', 'to', 'below',
    'ave', 'unit', 'rue', 'by', 'district', 'l', 'is', 'near', 'chemin', 'flat',
    'road', 'le', 'township', 'bd', 'shop', 'impasse', 'for'
})

PREFIX_CLEAN = re.compile(
    r'^(m/s\.?|smt\b|mr\b|mrs\b|\*\*\*|#|##|<<|>>|\bformerly\b|\bf/k/a\b|\bd/b/a\b|\bdba\b|\bt/a\b|\ba/k/a\b|\baka\b|c/o\b)\s*',
    re.I
)


def normalize_text(text: str) -> str:
    """
    Transliterates non-ASCII / Indic / Accented characters into ASCII,
    removes punctuation, cleans prefix noise, and lowercases text.
    """
    if not text or pd.isna(text):
        return ""
    text_str = str(text).strip()
    if not text_str or text_str.lower() in ('nan', 'null'):
        return ""
    text_ascii = anyascii(text_str).lower()
    text_clean = PREFIX_CLEAN.sub("", text_ascii)
    text_clean = re.sub(r'[^a-z0-9\s]', ' ', text_clean)
    text_clean = re.sub(r'\s+', ' ', text_clean).strip()
    return text_clean


def get_name_tokens(clean_name: str) -> list[str]:
    """Extract significant name tokens excluding common legal stopwords."""
    return [w for w in clean_name.split() if w not in STOPWORDS and len(w) >= 2]


def get_address_tokens(clean_addr: str) -> list[str]:
    """Extract significant address word tokens."""
    return [w for w in clean_addr.split() if w not in STOPWORDS and len(w) >= 3 and not w.isdigit()]


def get_address_numbers(clean_addr: str) -> list[str]:
    """Extract numeric tokens from address (door numbers, pin codes, etc.)."""
    return re.findall(r'\b\d+\b', clean_addr)
