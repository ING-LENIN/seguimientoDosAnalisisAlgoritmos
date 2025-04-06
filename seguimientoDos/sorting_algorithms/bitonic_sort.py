# bitonic_sort.py
import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def bitonic_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Bitonic Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def comp_and_swap(arr, i, j, direction):
        if (arr[i][1] > arr[j][1] and direction == 1) or (arr[i][1] < arr[j][1] and direction == 0):
            arr[i], arr[j] = arr[j], arr[i]

    def bitonic_merge(arr, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                comp_and_swap(arr, i, i + k, direction)
            bitonic_merge(arr, low, k, direction)
            bitonic_merge(arr, low + k, k, direction)

    def bitonic_sort_helper(arr, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            bitonic_sort_helper(arr, low, k, 1)
            bitonic_sort_helper(arr, low + k, k, 0)
            bitonic_merge(arr, low, cnt, direction)
        return arr

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = bitonic_sort_helper(terms_with_frequencies, 0, len(terms_with_frequencies), 1)
    end_time = time.time()
    return sorted_terms, end_time - start_time