import time
import bibtexparser
import re

# Leer el archivo bibtex
with open('todo_filtrado_part7.bib', encoding='utf-8') as bibtext_file:
    bib_database = bibtexparser.load(bibtext_file)

entries = bib_database.entries
entries_with_pages = [entry for entry in entries if 'pages' in entry]  # Filtrar entradas que tengan 'pages'

# Función para extraer el número de páginas
def extract_pages(entry):
    pages = entry.get('pages', '')
    match = re.match(r'(\d+)-(\d+)', pages)  # Extraer el rango de páginas "start_page-end_page"
    if match:
        start_page = int(match.group(1))
        end_page = int(match.group(2))
        return end_page - start_page + 1  # Calcular el número de páginas
    return 0  # Si no hay información de páginas, devolver 0

# Obtener el número de páginas de las entradas
pages = [extract_pages(entry) for entry in entries_with_pages]

# Funciones de ordenamiento

def pigeonhole_sort(entries, pages):
    min_pages = min(pages)
    max_pages = max(pages)
    size = max_pages - min_pages + 1

    # Crear un array de pigeonholes vacío
    holes = [[] for _ in range(size)]

    # Colocar cada entrada en el pigeonhole adecuado
    for entry, page_count in zip(entries, pages):
        holes[page_count - min_pages].append(entry)

    # Construir el array ordenado
    sorted_entries = []
    for hole in holes:
        sorted_entries.extend(hole)

    return sorted_entries

def bucket_sort(entries, pages):
    max_pages = max(pages)
    size = len(entries)

    # Crear buckets vacíos
    buckets = [[] for _ in range(size)]

    # Distribuir las entradas en los buckets
    for i in range(size):
        index = pages[i] * size // (max_pages + 1)
        buckets[index].append((pages[i], entries[i]))

    # Ordenar los buckets y combinarlos
    sorted_entries = []
    for bucket in buckets:
        sorted_entries.extend(sorted(bucket, key=lambda x: x[0]))  # Ordenar por el número de páginas (x[0])

    sorted_entries = [entry for _, entry in sorted_entries]  # Obtener solo las entradas, no los números de páginas
    return sorted_entries

def quicksort_entries(entries, pages):
    if len(entries) <= 1:
        return entries
    
    pivot = pages[len(entries) // 2]
    
    left = [(p, e) for p, e in zip(pages, entries) if p < pivot]
    middle = [(p, e) for p, e in zip(pages, entries) if p == pivot]
    right = [(p, e) for p, e in zip(pages, entries) if p > pivot]

    return quicksort_entries([e for _, e in left], [p for p, _ in left]) + \
           [e for _, e in middle] + \
           quicksort_entries([e for _, e in right], [p for p, _ in right])

def heapify(entries, pages, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and pages[left] > pages[largest]:
        largest = left

    if right < n and pages[right] > pages[largest]:
        largest = right

    if largest != i:
        pages[i], pages[largest] = pages[largest], pages[i]
        entries[i], entries[largest] = entries[largest], entries[i]
        heapify(entries, pages, n, largest)

def heapsort(entries, pages):
    n = len(entries)

    # Crear el max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(entries, pages, n, i)

    # Extraer elementos del heap
    for i in range(n - 1, 0, -1):
        pages[i], pages[0] = pages[0], pages[i]
        entries[i], entries[0] = entries[0], entries[i]
        heapify(entries, pages, i, 0)

    return entries

# Aplicar quicksort y medir el tiempo
start = time.time()
sorted_entries_quicksort = quicksort_entries(entries_with_pages, pages)
time_quicksort = time.time() - start
print(f"quicksort took {time_quicksort:.6f} seconds")

# Aplicar bucket_sort y medir el tiempo
start = time.time()
sorted_entries_bucket = bucket_sort(entries_with_pages, pages)
time_bucket = time.time() - start
print(f"bucket_sort took {time_bucket:.6f} seconds")

# Aplicar pigeonhole_sort y medir el tiempo
start = time.time()
sorted_entries_pigeonhole = pigeonhole_sort(entries_with_pages, pages)
time_pigeonhole = time.time() - start
print(f"pigeonhole_sort took {time_pigeonhole:.6f} seconds")

# Aplicar heapsort y medir el tiempo
start = time.time()
sorted_entries_heap = heapsort(entries_with_pages, pages)
time_heap = time.time() - start
print(f"heapsort took {time_heap:.6f} seconds")
