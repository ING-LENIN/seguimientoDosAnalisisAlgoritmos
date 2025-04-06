import time
import bibtexparser

# Leer el archivo bibtex
with open('todo_filtrado_part7.bib', encoding='utf-8') as bibtext_file:
    bib_database = bibtexparser.load(bibtext_file)

entries = bib_database.entries
entries_with_author = [entry for entry in entries if 'author' in entry]  # Filtrar entradas que tengan 'author'

# Función para extraer el autor (asumiendo que solo tomamos el primer autor)
def extract_author(entry):
    authors = entry.get('author', '')
    return authors.split(' and ')[0]  # Retornar el primer autor, asumiendo que se separan por 'and'

# Obtener los autores de las entradas
authors = [extract_author(entry) for entry in entries_with_author]

# Funciones de ordenamiento
def pigeonhole_sort(entries, authors):
    # Crear un diccionario para almacenar las entradas por autor
    author_dict = {}
    
    for entry, author in zip(entries, authors):
        if author not in author_dict:
            author_dict[author] = []
        author_dict[author].append(entry)

    # Construir el array ordenado
    sorted_entries = []
    for author in sorted(author_dict.keys()):  # Ordenar las claves (autores)
        sorted_entries.extend(author_dict[author])

    return sorted_entries

def bucket_sort(authors):
    buckets = {}

    for author in authors:
        if author:  # Verificar que el autor no esté vacío
            key = author[0]  # Tomamos la primera letra del autor como clave
            if key not in buckets:
                buckets[key] = []
            buckets[key].append(author)

    sorted_authors = []
    for key in sorted(buckets.keys()):
        sorted_authors.extend(sorted(buckets[key]))  # Solo ordenar los autores dentro del bucket
    return sorted_authors

def quicksort_authors(entries, authors):
    if len(entries) <= 1:
        return entries
    pivot = authors[len(entries) // 2]
    
    left = [e for e, a in zip(entries, authors) if a < pivot]
    middle = [e for e, a in zip(entries, authors) if a == pivot]
    right = [e for e, a in zip(entries, authors) if a > pivot]
    
    return quicksort_authors(left, [a for a in authors if a < pivot]) + middle + quicksort_authors(right, [a for a in authors if a > pivot])

def heapify(entries, authors, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and authors[left] > authors[largest]:
        largest = left

    if right < n and authors[right] > authors[largest]:
        largest = right

    if largest != i:
        authors[i], authors[largest] = authors[largest], authors[i]
        entries[i], entries[largest] = entries[largest], entries[i]
        heapify(entries, authors, n, largest)

def heapsort(entries, authors):
    n = len(entries)

    # Crear el max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(entries, authors, n, i)

    # Extraer elementos del heap
    for i in range(n - 1, 0, -1):
        authors[i], authors[0] = authors[0], authors[i]
        entries[i], entries[0] = entries[0], entries[i]
        heapify(entries, authors, i, 0)

    return entries

# Aplicar quicksort y medir el tiempo
start = time.time()
sorted_entries_quicksort = quicksort_authors(entries_with_author, authors)
time_quicksort = time.time() - start
print(f"quicksort took {time_quicksort:.6f} seconds")

# Aplicar bucket_sort y medir el tiempo
start = time.time()
sorted_authors_bucket = bucket_sort(authors)  # Solo ordenar autores aquí
time_bucket = time.time() - start
print(f"bucket_sort took {time_bucket:.6f} seconds")

# Aplicar pigeonhole_sort y medir el tiempo
start = time.time()
sorted_entries_pigeonhole = pigeonhole_sort(entries_with_author, authors)
time_pigeonhole = time.time() - start
print(f"pigeonhole_sort took {time_pigeonhole:.6f} seconds")

# Aplicar heapsort y medir el tiempo
start = time.time()
sorted_entries_heap = heapsort(entries_with_author, authors)
time_heap = time.time() - start
print(f"heapsort took {time_heap:.6f} seconds")
