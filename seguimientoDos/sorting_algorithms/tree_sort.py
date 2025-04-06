# tree_sort.py
import time
from collections import Counter
from bisect import insort
import re
from bisect import insort
from combine_term_frequencies import combine_term_frequencies

def tree_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Tree Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def tree_sort_helper(arr):
        sorted_arr = []
        for item in arr:
            insort(sorted_arr, item, key=lambda x: (-x[1], x[0]))
        return sorted_arr

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = tree_sort_helper(terms_with_frequencies)
    end_time = time.time()
    return sorted_terms, end_time - start_time