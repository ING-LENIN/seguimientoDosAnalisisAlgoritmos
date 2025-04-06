# bubble_sort.py
import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def bubble_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Bubble Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    n = len(terms_with_frequencies)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (-terms_with_frequencies[j][1], terms_with_frequencies[j][0]) > \
               (-terms_with_frequencies[j + 1][1], terms_with_frequencies[j + 1][0]):
                terms_with_frequencies[j], terms_with_frequencies[j + 1] = \
                    terms_with_frequencies[j + 1], terms_with_frequencies[j]
    end_time = time.time()
    return terms_with_frequencies, end_time - start_time