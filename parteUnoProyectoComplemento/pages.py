import bibtexparser
import time
import re

# Leer el archivo BibTeX utilizando la codificación UTF-8
with open('todo_filtrado_part7.bib', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

entries = bib_database.entries
entries_with_pages = [entry for entry in entries if 'pages' in entry]  # Filtrar entradas que tengan 'pages'

# Función para extraer el número de páginas
def extract_pages(entry):
    pages_str = entry.get('pages', '')
    if '-' in pages_str:
        try:
            return int(pages_str.split('-')[1])  # Retornar la última página del rango
        except ValueError:
            return 0  # Retornar 0 si no se puede convertir
    elif pages_str.isdigit():
        return int(pages_str)  # Retornar si es un número simple
    return 0  # Retornar 0 si no se puede extraer el número de páginas

def timsort(entries):
    start_time = time.time()
    # Filtrar solo las entradas con un número de páginas válidas
    valid_entries = [entry for entry in entries if extract_pages(entry) > 0]
    
    sorted_entries = sorted(valid_entries, key=extract_pages)
    end_time = time.time()
    return sorted_entries, end_time - start_time

def comb_sort(arr):
    start_time = time.time()

    # Filtrar solo las entradas con un número de páginas válidas
    valid_entries = [entry for entry in arr if extract_pages(entry) > 0]
    
    gap = len(valid_entries)
    shrink = 1.3
    sorted_flag = False

    while not sorted_flag:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_flag = True

        i = 0
        while i + gap < len(valid_entries):
            if extract_pages(valid_entries[i]) > extract_pages(valid_entries[i + gap]):
                valid_entries[i], valid_entries[i + gap] = valid_entries[i + gap], valid_entries[i]
                sorted_flag = False
            i += 1

    end_time = time.time()
    return valid_entries, end_time - start_time

def selection_sort(arr):
    start_time = time.time()

    # Filtrar solo las entradas con un número de páginas válidas
    valid_entries = [entry for entry in arr if extract_pages(entry) > 0]

    for i in range(len(valid_entries)):
        min_idx = i
        for j in range(i + 1, len(valid_entries)):
            if extract_pages(valid_entries[j]) < extract_pages(valid_entries[min_idx]):
                min_idx = j

        # Intercambiar la posición del mínimo encontrado con la posición actual
        valid_entries[i], valid_entries[min_idx] = valid_entries[min_idx], valid_entries[i]
    
    end_time = time.time()
    return valid_entries, end_time - start_time

class Node:
    def __init__(self, key, entry):
        self.left = None
        self.right = None
        self.val = key
        self.entry = entry

def insert_iterative(root, key, entry):
    new_node = Node(key, entry)
    if root is None:
        return new_node

    current = root
    while True:
        if key < current.val:
            if current.left is None:
                current.left = new_node
                break
            current = current.left
        else:  # Cambiado a else para manejar duplicados
            if current.right is None:
                current.right = new_node
                break
            current = current.right

    return root

def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.entry)  # Añadir la entrada completa al resultado
        inorder_traversal(root.right, result)

def tree_sort(entries):
    start_time = time.time()

    # Filtrar solo las entradas con un número de páginas válidas
    valid_entries = [entry for entry in entries if extract_pages(entry) > 0]

    root = None
    # Insertar cada entrada en el árbol (iterativo)
    for entry in valid_entries:
        pages = extract_pages(entry)
        root = insert_iterative(root, pages, entry)

    # Realizar un recorrido in-order para obtener el orden correcto
    sorted_entries = []
    inorder_traversal(root, sorted_entries)

    end_time = time.time()
    return sorted_entries, end_time - start_time

# Aplicar Selection Sort y medir el tiempo
sorted_entries_selection, time_selection_sort = selection_sort(entries_with_pages)
print(f"Selection Sort took {time_selection_sort:.6f} seconds")

# Aplicar TimSort y medir el tiempo
sorted_entries_timsort, time_timsort = timsort(entries_with_pages)
print(f"TimSort took {time_timsort:.6f} seconds")

# Aplicar Comb Sort y medir el tiempo
sorted_entries_comb, time_comb_sort = comb_sort(entries_with_pages)
print(f"Comb Sort took {time_comb_sort:.6f} seconds")

# Aplicar Tree Sort y medir el tiempo
sorted_entries_tree, time_tree_sort = tree_sort(entries_with_pages)
print(f"Tree Sort took {time_tree_sort:.6f} seconds")
