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

# Función para realizar Counting Sort basado en un dígito específico
def counting_sort_for_radix(years, entries, exp):
    n = len(years)
    output_years = [0] * n
    output_entries = [None] * n
    count = [0] * 10

    # Contar las ocurrencias de cada dígito
    for i in range(n):
        index = (years[i] // exp) % 10
        count[index] += 1

    # Cambiar count[i] para que contenga la posición de este dígito en output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el array de salida
    for i in range(n - 1, -1, -1):
        index = (years[i] // exp) % 10
        output_years[count[index] - 1] = years[i]
        output_entries[count[index] - 1] = entries[i]
        count[index] -= 1

    # Copiar el array de salida a years y entries
    for i in range(n):
        years[i] = output_years[i]
        entries[i] = output_entries[i]

# Función principal de Radix Sort
def radix_sort(years, entries):
    max_year = max(years)

    # Aplicar Counting Sort para cada dígito
    exp = 1
    while max_year // exp > 0:
        counting_sort_for_radix(years, entries, exp)
        exp *= 10

# Ordenar las entradas utilizando Radix Sort
def sort_entries(entries, years):
    radix_sort(years, entries)
    return entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_year, years)
time_radix_sort = time.time() - start

# Imprimir resultados
print(f"Radix sort took {time_radix_sort:.6f} seconds")
#print(f"Años ordenados: {[entry['year'] for entry in sorted_entries]}")

# Guardar resultados en un nuevo archivo
save_sorted_entries(sorted_entries, 'ie_radix_sort.bib')
