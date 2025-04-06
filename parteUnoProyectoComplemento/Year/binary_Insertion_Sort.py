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

# Función de búsqueda binaria
def binary_search(years, year, high):
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if years[mid] < year:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Función de Binary Insertion Sort
def binary_insertion_sort(years, entries):
    for i in range(1, len(years)):
        year = years[i]
        entry = entries[i]
        
        # Encuentra la posición correcta para el año actual
        pos = binary_search(years, year, i - 1)
        
        # Mueve los elementos hacia la derecha
        years[pos + 1:i + 1] = years[pos:i]
        entries[pos + 1:i + 1] = entries[pos:i]
        
        # Coloca el año actual en la posición correcta
        years[pos] = year
        entries[pos] = entry

# Ordenar las entradas utilizando Binary Insertion Sort
def sort_entries(entries, years):
    binary_insertion_sort(years, entries)
    return entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_year, years)
time_binary_insertion_sort = time.time() - start

# Imprimir resultados
print(f"Binary insertion sort took {time_binary_insertion_sort:.6f} seconds")
#print(f"Años ordenados: {[entry['year'] for entry in sorted_entries]}")

# Guardar resultados en un nuevo archivo
save_sorted_entries(sorted_entries, 'ie_binary_insertion_sort.bib')
