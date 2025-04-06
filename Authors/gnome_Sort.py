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

# Función de Gnome Sort
def gnome_sort(authors, entries):
    index = 0
    n = len(authors)
    
    while index < n:
        if index == 0:
            index += 1
        if authors[index] >= authors[index - 1]:
            index += 1
        else:
            # Intercambiar autores y entradas
            authors[index], authors[index - 1] = authors[index - 1], authors[index]
            entries[index], entries[index - 1] = entries[index - 1], entries[index]
            index -= 1

# Ordenar las entradas utilizando Gnome Sort
def sort_entries(entries, authors):
    gnome_sort(authors, entries)
    return entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_author, authors)
time_gnome_sort = time.time() - start

# Imprimir resultados
print(f"Gnome sort took {time_gnome_sort:.6f} seconds")
#print(f"Autores ordenados: {[entry['author'] for entry in sorted_entries]}")

# Guardar resultados en un nuevo archivo
save_sorted_entries(sorted_entries, 'todo_gnome_sort_by_author.bib')
