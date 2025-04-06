#shell_sort
import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def shell_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Shell Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def shell_sort_helper(arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and (-arr[j - gap][1], arr[j - gap][0]) > (-temp[1], temp[0]):
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = shell_sort_helper(terms_with_frequencies)
    end_time = time.time()
    return sorted_terms, end_time - start_time