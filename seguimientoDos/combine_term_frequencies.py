from collections import Counter
import re
from terminos import TERMS  # Importar TERMS desde terminos

def combine_term_frequencies(entries):
    combined_frequencies = Counter()
    for entry in entries:
        abstract = entry.get('abstract', '').lower()
        for term in TERMS:
            matches = re.findall(r'\b' + re.escape(term.lower()) + r'\b', abstract)
            combined_frequencies[term] += len(matches)
    return combined_frequencies