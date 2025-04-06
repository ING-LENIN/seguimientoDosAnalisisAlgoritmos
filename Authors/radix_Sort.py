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
    return author_str.strip()

# Obtener los autores de las entradas
authors = [extract_author(entry['author']) for entry in entries_with_author]

# Función para realizar Counting Sort basado en el carácter específico
def counting_sort_for_radix(authors, entries, exp):
    n = len(authors)
    output_authors = [''] * n
    output_entries = [None] * n
    count = [0] * 512  # Aumentar el tamaño del conteo

    # Contar las ocurrencias de cada carácter
    for i in range(n):
        index = ord(authors[i][exp]) if exp < len(authors[i]) else 0
        if index < len(count):
            count[index] += 1
        else:
            # Si el índice está fuera de rango, asignar a la última posición
            count[-1] += 1

    # Cambiar count[i] para que contenga la posición de este carácter en output
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Construir el array de salida
    for i in range(n - 1, -1, -1):
        index = ord(authors[i][exp]) if exp < len(authors[i]) else 0
        if index < len(count):
            output_authors[count[index] - 1] = authors[i]
            output_entries[count[index] - 1] = entries[i]
            count[index] -= 1
        else:
            # Asignar a la última posición si está fuera de rango
            output_authors[count[-1] - 1] = authors[i]
            output_entries[count[-1] - 1] = entries[i]
            count[-1] -= 1

    # Copiar el array de salida a authors y entries
    for i in range(n):
        authors[i] = output_authors[i]
        entries[i] = output_entries[i]

# Función principal de Radix Sort para cadenas
def radix_sort(authors, entries):
    max_length = max(len(author) for author in authors)

    # Aplicar Counting Sort para cada carácter
    for exp in range(max_length - 1, -1, -1):
        counting_sort_for_radix(authors, entries, exp)

# Ordenar las entradas utilizando Radix Sort
def sort_entries(entries, authors):
    radix_sort(authors, entries)
    return entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_author, authors)
time_radix_sort = time.time() - start

# Imprimir resultados
print(f"Radix sort took {time_radix_sort:.6f} seconds")
#print(f"Autores ordenados: {[entry['author'] for entry in sorted_entries]}")

# Guardar resultados en un nuevo archivo
save_sorted_entries(sorted_entries, 'todo_radix_sort_by_author.bib')
