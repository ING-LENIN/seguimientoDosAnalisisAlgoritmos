# radix_sort.py
import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def radix_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Radix Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def counting_sort_for_radix(arr, exp):
        n = len(arr)
        output = [None] * n
        count = [0] * 256
        for i in range(n):
            index = ord(arr[i][0][exp]) if exp < len(arr[i][0]) else 0
            count[index] += 1
        for i in range(1, 256):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            index = ord(arr[i][0][exp]) if exp < len(arr[i][0]) else 0
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        for i in range(n):
            arr[i] = output[i]
        return arr

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    max_length = max(len(term) for term, _ in terms_with_frequencies)
    for exp in range(max_length - 1, -1, -1):
        terms_with_frequencies = counting_sort_for_radix(terms_with_frequencies, exp)
    terms_with_frequencies.sort(key=lambda x: (-x[1], x[0]))
    end_time = time.time()
    return terms_with_frequencies, end_time - start_time