#merge_sort
import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def merge_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Merge Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def merge_sort_helper(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_helper(arr[:mid])
        right = merge_sort_helper(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if (-left[i][1], left[i][0]) <= (-right[j][1], right[j][0]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = merge_sort_helper(terms_with_frequencies)
    end_time = time.time()
    return sorted_terms, end_time - start_time