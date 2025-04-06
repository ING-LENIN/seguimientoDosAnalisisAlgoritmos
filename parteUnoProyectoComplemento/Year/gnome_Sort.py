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

# Función de Gnome Sort
def gnome_sort(years, entries):
    index = 0
    n = len(years)
    
    while index < n:
        if index == 0:
            index += 1
        if years[index] >= years[index - 1]:
            index += 1
        else:
            # Intercambiar años y entradas
            years[index], years[index - 1] = years[index - 1], years[index]
            entries[index], entries[index - 1] = entries[index - 1], entries[index]
            index -= 1

# Ordenar las entradas utilizando Gnome Sort
def sort_entries(entries, years):
    gnome_sort(years, entries)
    return entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_year, years)
time_gnome_sort = time.time() - start

# Imprimir resultados
print(f"Gnome sort took {time_gnome_sort:.6f} seconds")
#print(f"Años ordenados: {[entry['year'] for entry in sorted_entries]}")

# Guardar resultados en un nuevo archivo
save_sorted_entries(sorted_entries, 'ie_gnome_sort.bib')
