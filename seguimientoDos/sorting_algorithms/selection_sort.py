# selection_sort.py
import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def selection_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Selection Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def selection_sort_helper(arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if (-arr[j][1], arr[j][0]) < (-arr[min_index][1], arr[min_index][0]):
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = selection_sort_helper(terms_with_frequencies)
    end_time = time.time()
    return sorted_terms, end_time - start_time