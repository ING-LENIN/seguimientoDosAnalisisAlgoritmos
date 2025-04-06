# gnome_sort.py
import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def gnome_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Gnome Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def gnome_sort_helper(arr):
        index = 0
        n = len(arr)
        while index < n:
            if index == 0:
                index += 1
            if (-arr[index][1], arr[index][0]) >= (-arr[index - 1][1], arr[index - 1][0]):
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index -= 1
        return arr

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = gnome_sort_helper(terms_with_frequencies)
    end_time = time.time()
    return sorted_terms, end_time - start_time