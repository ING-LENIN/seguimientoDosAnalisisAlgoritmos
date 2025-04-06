# binary_insertion_sort.py
import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def binary_insertion_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Binary Insertion Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def binary_search(arr, val, start, end):
        while start <= end:
            mid = (start + end) // 2
            if (-arr[mid][1], arr[mid][0]) <= (-val[1], val[0]):
                start = mid + 1
            else:
                end = mid - 1
        return start

    def binary_insertion_sort_helper(arr):
        for i in range(1, len(arr)):
            val = arr[i]
            j = binary_search(arr, val, 0, i - 1)
            arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
        return arr

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = binary_insertion_sort_helper(terms_with_frequencies)
    end_time = time.time()
    return sorted_terms, end_time - start_time