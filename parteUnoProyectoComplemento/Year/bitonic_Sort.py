import time
import bibtexparser
import re

# Leer el archivo bibtex
with open('todo_filtrado_part7.bib', encoding='utf-8') as bibtext_file:
    bib_database = bibtexparser.load(bibtext_file)

entries = bib_database.entries
entries_with_year = [entry for entry in entries if 'year' in entry]

# Extraer los años utilizando una expresión regular
def extract_year(year_str):
    match = re.match(r'(\d+)', year_str)
    return int(match.group(1)) if match else None

# Obtener los años de las entradas
years = [extract_year(entry['year']) for entry in entries_with_year]

# Funciones de Bitonic Sort
def compare_and_swap(arr, i, j, dire):
    if (dire == 1 and arr[i] > arr[j]) or (dire == 0 and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]

def bitonic_merge(arr, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compare_and_swap(arr, i, i + k, dire)
        bitonic_merge(arr, low, k, dire)
        bitonic_merge(arr, low + k, k, dire)

def bitonic_sort(arr, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        bitonic_sort(arr, low, k, 1)  # Ascendente
        bitonic_sort(arr, low + k, k, 0)  # Descendente
        bitonic_merge(arr, low, cnt, dire)

# Ordenar las entradas utilizando Bitonic Sort
def sort_entries(entries, years):
    n = len(years)
    bitonic_sort(years, 0, n, 1)  # 1 para orden ascendente

    sorted_entries = [None] * n
    for i in range(n):
        sorted_entries[i] = entries[years.index(years[i])]
    return sorted_entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_year, years)
time_bitonic_sort = time.time() - start

# Imprimir resultados
print(f"Bitonic sort took {time_bitonic_sort:.6f} seconds")
#print(f"Años ordenados: {[entry['year'] for entry in sorted_entries]}")

# Guardar resultados en un nuevo archivo
save_sorted_entries(sorted_entries, 'ie_bitonic_sort.bib')
