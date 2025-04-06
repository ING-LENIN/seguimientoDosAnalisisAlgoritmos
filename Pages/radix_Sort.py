import time
import bibtexparser
import re

# Leer el archivo bibtex
with open('todo_filtrado_part7.bib', encoding='utf-8') as bibtext_file:
    bib_database = bibtexparser.load(bibtext_file)

entries = bib_database.entries

# Filtrar entradas que tienen el campo 'pages'
entries_with_pages = [entry for entry in entries if 'pages' in entry]

# Extraer páginas
def extract_pages(pages_str):
    # Extraer el primer número de 'pages' como cadena
    match = re.match(r'(\d+)', pages_str)
    return match.group(1) if match else '0'

# Obtener las páginas de las entradas
pages = [extract_pages(entry['pages']) for entry in entries_with_pages]

# Función para realizar Counting Sort basado en el carácter específico
def counting_sort_for_radix(pages, entries, exp):
    n = len(pages)
    output_pages = [''] * n
    output_entries = [None] * n
    count = [0] * 512  # Aumentar el tamaño del conteo para cubrir más caracteres

    # Contar las ocurrencias de cada carácter
    for i in range(n):
        index = ord(pages[i][exp]) if exp < len(pages[i]) else 0
        if index < len(count):
            count[index] += 1
        else:
            count[-1] += 1

    # Cambiar count[i] para que contenga la posición de este carácter en output
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Construir el array de salida
    for i in range(n - 1, -1, -1):
        index = ord(pages[i][exp]) if exp < len(pages[i]) else 0
        if index < len(count):
            output_pages[count[index] - 1] = pages[i]
            output_entries[count[index] - 1] = entries[i]
            count[index] -= 1
        else:
            output_pages[count[-1] - 1] = pages[i]
            output_entries[count[-1] - 1] = entries[i]
            count[-1] -= 1

    # Copiar el array de salida a pages y entries
    for i in range(n):
        pages[i] = output_pages[i]
        entries[i] = output_entries[i]

# Función principal de Radix Sort para cadenas de páginas
def radix_sort(pages, entries):
    max_length = max(len(page) for page in pages)

    # Aplicar Counting Sort para cada carácter, comenzando por el menos significativo
    for exp in range(max_length - 1, -1, -1):
        counting_sort_for_radix(pages, entries, exp)

# Ordenar las entradas utilizando Radix Sort por 'pages'
def sort_entries(entries, pages):
    radix_sort(pages, entries)
    return entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_pages, pages)
time_radix_sort = time.time() - start

# Imprimir resultados
print(f"Radix sort took {time_radix_sort:.6f} seconds")
#print(f"Páginas ordenadas: {[entry['pages'] for entry in sorted_entries]}")

# Guardar resultados en un nuevo archivo
save_sorted_entries(sorted_entries, 'ie_radix_sort_by_pages.bib')
