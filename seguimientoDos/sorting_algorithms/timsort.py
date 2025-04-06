# timsort.py
import time
import re
from combine_term_frequencies import combine_term_frequencies

def timsort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo TimSort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = sorted(terms_with_frequencies, key=lambda x: (-x[1], x[0]))
    end_time = time.time()
    return sorted_terms, end_time - start_time