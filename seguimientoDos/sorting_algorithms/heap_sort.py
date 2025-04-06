# heap_sort.py
import time
from collections import Counter
import re
from combine_term_frequencies import combine_term_frequencies

def heap_sort(entries, TERMS):
    """
    Ordena los términos utilizando el algoritmo Heap Sort.
    :param entries: Lista de entradas con campos 'abstract'.
    :param TERMS: Lista de términos a buscar.
    :return: Tupla con los términos ordenados y el tiempo de ejecución.
    """
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and (-arr[left][1], arr[left][0]) > (-arr[largest][1], arr[largest][0]):
            largest = left
        if right < n and (-arr[right][1], arr[right][0]) > (-arr[largest][1], arr[largest][0]):
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def heap_sort_helper(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
        return arr

    start_time = time.time()
    term_counts = combine_term_frequencies(entries)
    terms_with_frequencies = [(term, term_counts[term]) for term in TERMS]
    sorted_terms = heap_sort_helper(terms_with_frequencies)
    end_time = time.time()
    return sorted_terms, end_time - start_time