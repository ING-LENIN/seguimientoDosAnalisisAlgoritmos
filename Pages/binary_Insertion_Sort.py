import time
import bibtexparser
import re

# Leer el archivo bibtex
with open('todo_filtrado_part7.bib', encoding='utf-8') as bibtext_file:
    bib_database = bibtexparser.load(bibtext_file)

entries = bib_database.entries

# Filtrar entradas que tienen el campo 'pages'
entries_with_pages = [entry for entry in entries if 'pages' in entry]

# Extraer las páginas
def extract_pages(pages_str):
    # Extraer el primer número de 'pages'
    match = re.match(r'(\d+)', pages_str)
    return int(match.group(1)) if match else 0

# Obtener las páginas de las entradas
pages = [extract_pages(entry['pages']) for entry in entries_with_pages]

# Función de búsqueda binaria
def binary_search(pages, page, high):
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if pages[mid] < page:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Función de Binary Insertion Sort
def binary_insertion_sort(pages, entries):
    for i in range(1, len(pages)):
        page = pages[i]
        entry = entries[i]
        
        # Encuentra la posición correcta para la página actual
        pos = binary_search(pages, page, i - 1)
        
        # Mueve los elementos hacia la derecha
        pages[pos + 1:i + 1] = pages[pos:i]
        entries[pos + 1:i + 1] = entries[pos:i]
        
        # Coloca la página actual en la posición correcta
        pages[pos] = page
        entries[pos] = entry

# Ordenar las entradas utilizando Binary Insertion Sort por 'pages'
def sort_entries(entries, pages):
    binary_insertion_sort(pages, entries)
    return entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_pages, pages)
time_binary_insertion_sort = time.time() - start

# Imprimir resultados
print(f"Binary insertion sort took {time_binary_insertion_sort:.6f} seconds")
#print(f"Páginas ordenadas: {[entry['pages'] for entry in sorted_entries]}")

# Guardar resultados en un nuevo archivo
save_sorted_entries(sorted_entries, 'ie_binary_insertion_sort_by_pages.bib')
