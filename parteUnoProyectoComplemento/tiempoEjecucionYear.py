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

# Funciones de ordenamiento (se mantienen igual)
def pigeonhole_sort(entries, years):
    min_year = min(years)
    max_year = max(years)
    size = max_year - min_year + 1

    # Crear el array pigeonholes vacío
    holes = [[] for _ in range(size)]

    # Colocar cada entrada en el pigeonhole adecuado
    for entry, year in zip(entries, years):
        holes[year - min_year].append(entry)

    # Construir el array ordenado
    sorted_entries = []
    for hole in holes:
        sorted_entries.extend(hole)

    return sorted_entries

def bucket_sort(years):
    max_year = max(years)
    min_year = min(years)
    size = max_year - min_year + 1
    buckets = [[] for _ in range(size)]
    
    for year in years:
        index = year - min_year
        buckets[index].append(year)
    
    sorted_years = []
    for bucket in buckets:
        sorted_years.extend(sorted(bucket))  # Solo ordenar los años dentro del bucket
    return sorted_years


def quicksort(entries, years):
    if len(entries) <= 1:
        return entries
    pivot = years[len(entries) // 2]
    
    left = [e for e, y in zip(entries, years) if y < pivot]
    middle = [e for e, y in zip(entries, years) if y == pivot]
    right = [e for e, y in zip(entries, years) if y > pivot]
    
    return quicksort(left, [y for y in years if y < pivot]) + middle + quicksort(right, [y for y in years if y > pivot])

def heapify(entries, years, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and years[left] > years[largest]:
        largest = left

    if right < n and years[right] > years[largest]:
        largest = right

    if largest != i:
        years[i], years[largest] = years[largest], years[i]
        entries[i], entries[largest] = entries[largest], entries[i]
        heapify(entries, years, n, largest)

def heapsort(entries, years):
    n = len(entries)

    # Crear el max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(entries, years, n, i)

    # Extraer elementos del heap
    for i in range(n - 1, 0, -1):
        years[i], years[0] = years[0], years[i]
        entries[i], entries[0] = entries[0], entries[i]
        heapify(entries, years, i, 0)

    return entries

# Aplicar quicksort y medir el tiempo
start = time.time()
sorted_entries_quicksort = quicksort(entries_with_year, years)
time_quicksort = time.time() - start
print(f"quicksort took {time_quicksort:.6f} seconds")

# Aplicar bucket_sort y medir el tiempo
start = time.time()
sorted_entries_bucket = bucket_sort(years)
time_bucket = time.time() - start
print(f"bucket_sort took {time_bucket:.6f} seconds")

# Aplicar pigeonhole_sort y medir el tiempo
start = time.time()
sorted_entries_pigeonhole = pigeonhole_sort(entries_with_year, years)
time_pigeonhole = time.time() - start
print(f"pigeonhole_sort took {time_pigeonhole:.6f} seconds")

# Aplicar heapsort y medir el tiempo
start = time.time()
sorted_entries_heap = heapsort(entries_with_year, years)
time_heap = time.time() - start
print(f"heapsort took {time_heap:.6f} seconds")