#double_direction_bubble_sort

import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def double_direction_bubble_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Double Direction Bubble Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def double_direction_bubble_sort_helper(arr):
        n = len(arr)
        first = 0
        last = n - 1
        while first < last:
            # Fase 1: Mover los elementos más pequeños hacia arriba
            new_last = first
            for i in range(first, last):
                if (-arr[i][1], arr[i][0]) > (-arr[i + 1][1], arr[i + 1][0]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    new_last = i
            last = new_last

            # Fase 2: Mover los elementos más grandes hacia abajo
            new_first = last
            for i in range(last, first, -1):
                if (-arr[i - 1][1], arr[i - 1][0]) > (-arr[i][1], arr[i][0]):
                    arr[i - 1], arr[i] = arr[i], arr[i - 1]
                    new_first = i
            first = new_first
        return arr

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = double_direction_bubble_sort_helper(terms_with_frequencies)
    end_time = time.time()
    return sorted_terms, end_time - start_time
