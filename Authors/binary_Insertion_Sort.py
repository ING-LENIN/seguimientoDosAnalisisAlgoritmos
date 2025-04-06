import time
import bibtexparser
import re

# Leer el archivo bibtex
with open('todo_filtrado_part7.bib', encoding='utf-8') as bibtext_file:
    bib_database = bibtexparser.load(bibtext_file)

entries = bib_database.entries

# Filtrar entradas que tienen el campo 'author'
entries_with_author = [entry for entry in entries if 'author' in entry]

# Extraer autores
def extract_author(author_str):
    # Aquí puedes ajustar la forma en que extraes los autores si es necesario
    return author_str

# Obtener los autores de las entradas
authors = [extract_author(entry['author']) for entry in entries_with_author]

# Función de búsqueda binaria
def binary_search(authors, author, high):
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if authors[mid] < author:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Función de Binary Insertion Sort
def binary_insertion_sort(authors, entries):
    for i in range(1, len(authors)):
        author = authors[i]
        entry = entries[i]
        
        # Encuentra la posición correcta para el autor actual
        pos = binary_search(authors, author, i - 1)
        
        # Mueve los elementos hacia la derecha
        authors[pos + 1:i + 1] = authors[pos:i]
        entries[pos + 1:i + 1] = entries[pos:i]
        
        # Coloca el autor actual en la posición correcta
        authors[pos] = author
        entries[pos] = entry

# Ordenar las entradas utilizando Binary Insertion Sort
def sort_entries(entries, authors):
    binary_insertion_sort(authors, entries)
    return entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_author, authors)
time_binary_insertion_sort = time.time() - start

# Imprimir resultados
print(f"Binary insertion sort took {time_binary_insertion_sort:.6f} seconds")
#print(f"Autores ordenados: {[entry['author'] for entry in sorted_entries]}")

# Guardar resultados en un nuevo archivo
save_sorted_entries(sorted_entries, 'todo_binary_insertion_sort_by_author.bib')
