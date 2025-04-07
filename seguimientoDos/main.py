import time
import matplotlib.pyplot as plt
import bibtexparser

# Importar funciones auxiliares
from combine_term_frequencies import combine_term_frequencies
from print_table import print_table
from plot_bar_chart import plot_bar_chart

# Importar algoritmos de ordenamiento
from sorting_algorithms.timsort import timsort
from sorting_algorithms.quicksort import quicksort
from sorting_algorithms.comb_sort import comb_sort
from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.gnome_sort import gnome_sort
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.pigeonhole_sort import pigeonhole_sort
from sorting_algorithms.bucket_sort import bucket_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.bitonic_sort import bitonic_sort
from sorting_algorithms.binary_insertion_sort import binary_insertion_sort
from sorting_algorithms.radix_sort import radix_sort
from sorting_algorithms.double_direction_bubble_sort import double_direction_bubble_sort
from sorting_algorithms.shell_sort import shell_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.tree_sort import tree_sort

# Importar términos desde config.py
from terminos import TERMS

# Leer el archivo BibTeX utilizando la codificación UTF-8
with open('complete.bib', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Filtrar entradas que tienen el campo 'abstract'
entries_with_abstract = [entry for entry in bib_database.entries if 'abstract' in entry]

# Ejecutar todos los métodos y comparar tiempos
sorting_algorithms = [
    ("TimSort", timsort),
    ("QuickSort", quicksort),
    ("Comb Sort", comb_sort),
    ("Selection Sort", selection_sort),
    ("Gnome Sort", gnome_sort),
    ("Bubble Sort", bubble_sort),
    ("Pigeonhole Sort", pigeonhole_sort),
    ("Bucket Sort", bucket_sort),
    ("Heap Sort", heap_sort),
    ("Bitonic Sort", bitonic_sort),
    ("Binary Insertion Sort", binary_insertion_sort),
    ("Radix Sort", radix_sort),
    ("Double Direction Bubble Sort", double_direction_bubble_sort),
    ("Shell Sort", shell_sort),
    ("Merge Sort", merge_sort),
    ("Tree Sort", tree_sort)
]

execution_times = []
final_sorted_terms = None  # Variable para almacenar los términos ordenados finales

for algorithm_name, algorithm_function in sorting_algorithms:
    sorted_terms, execution_time = algorithm_function(entries_with_abstract, TERMS)
    execution_times.append(execution_time)
    final_sorted_terms = sorted_terms

# Imprimir una única tabla con los términos ordenados
if final_sorted_terms:
    print_table(final_sorted_terms)

# Gráfico comparativo de tiempos
plt.figure(figsize=(12, 6))
algorithm_names = [name for name, _ in sorting_algorithms]
plt.bar(algorithm_names, execution_times, color='skyblue')
plt.xlabel("Algoritmos de Ordenamiento")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de tiempos de ejecución")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()