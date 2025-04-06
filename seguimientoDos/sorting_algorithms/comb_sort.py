# comb_sort.py
import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def comb_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Comb Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def comb_sort_helper(arr):
        gap = len(arr)
        shrink = 1.3
        sorted = False
        while not sorted:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted = True
            i = 0
            while i + gap < len(arr):
                if (-arr[i][1], arr[i][0]) > (-arr[i + gap][1], arr[i + gap][0]):
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    sorted = False
                i += 1
        return arr

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = comb_sort_helper(terms_with_frequencies)
    end_time = time.time()
    return sorted_terms, end_time - start_time