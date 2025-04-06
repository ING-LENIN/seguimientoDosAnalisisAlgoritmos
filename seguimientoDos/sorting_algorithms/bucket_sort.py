# bucket_sort.py
import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def bucket_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Bucket Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def bucket_sort_helper(arr):
        max_freq = max(-freq for _, freq in arr)
        min_freq = min(-freq for _, freq in arr)
        size = max_freq - min_freq + 1
        buckets = [[] for _ in range(size)]
        for term, freq in arr:
            buckets[-freq - min_freq].append((term, freq))
        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(sorted(bucket, key=lambda x: (x[1], x[0])))
        return sorted_arr

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = bucket_sort_helper(terms_with_frequencies)
    end_time = time.time()
    return sorted_terms, end_time - start_time