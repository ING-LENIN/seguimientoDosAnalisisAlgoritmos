# quicksort.py
import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def quicksort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo QuickSort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def quicksort_helper(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if (-x[1], x[0]) < (-pivot[1], pivot[0])]
        middle = [x for x in arr if (-x[1], x[0]) == (-pivot[1], pivot[0])]
        right = [x for x in arr if (-x[1], x[0]) > (-pivot[1], pivot[0])]
        return quicksort_helper(left) + middle + quicksort_helper(right)

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = quicksort_helper(terms_with_frequencies)
    end_time = time.time()
    return sorted_terms, end_time - start_time