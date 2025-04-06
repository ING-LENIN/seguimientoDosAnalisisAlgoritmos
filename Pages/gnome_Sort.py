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

# Función de Gnome Sort
def gnome_sort(pages, entries):
    index = 0
    n = len(pages)
    
    while index < n:
        if index == 0:
            index += 1
        if pages[index] >= pages[index - 1]:
            index += 1
        else:
            # Intercambiar páginas y entradas
            pages[index], pages[index - 1] = pages[index - 1], pages[index]
            entries[index], entries[index - 1] = entries[index - 1], entries[index]
            index -= 1

# Ordenar las entradas utilizando Gnome Sort por 'pages'
def sort_entries(entries, pages):
    gnome_sort(pages, entries)
    return entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_pages, pages)
time_gnome_sort = time.time() - start

# Imprimir resultados
print(f"Gnome sort took {time_gnome_sort:.6f} seconds")
#print(f"Páginas ordenadas: {[entry['pages'] for entry in sorted_entries]}")

# Guardar resultados en un nuevo archivo
save_sorted_entries(sorted_entries, 'ie_gnome_sort_by_pages.bib')

