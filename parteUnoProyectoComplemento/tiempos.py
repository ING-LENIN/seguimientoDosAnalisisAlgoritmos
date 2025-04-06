import bibtexparser
import time

# Leer el archivo BibTeX utilizando la codificación UTF-8
with open('todo_filtrado_part7.bib', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

entries = bib_database.entries
entries_with_year = [entry for entry in entries if 'year' in entry]
import re

def extract_year(year_str):
    # Usar una expresión regular para extraer solo la parte numérica del año
    match = re.match(r'(\d+)', year_str)
    return int(match.group(1)) if match else None

def timsort(entries):
    start_time = time.time()
    # Filtrar solo las entradas con años válidos
    valid_entries = [entry for entry in entries if extract_year(entry['year']) is not None]
    
    sorted_entries = sorted(valid_entries, key=lambda x: extract_year(x['year']))
    end_time = time.time()
    return sorted_entries, end_time - start_time

def comb_sort(arr):
    start_time = time.time()

    # Filtrar solo las entradas con años válidos
    valid_entries = [entry for entry in arr if extract_year(entry['year']) is not None]
    
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
            if extract_year(valid_entries[i]['year']) > extract_year(valid_entries[i + gap]['year']):
                valid_entries[i], valid_entries[i + gap] = valid_entries[i + gap], valid_entries[i]
                sorted_flag = False
            i += 1

    end_time = time.time()
    return valid_entries, end_time - start_time
def selection_sort(arr):
    start_time = time.time()

    # Filtrar solo las entradas con años válidos
    valid_entries = [entry for entry in arr if extract_year(entry['year']) is not None]

    for i in range(len(valid_entries)):
        min_idx = i
        for j in range(i+1, len(valid_entries)):
            if extract_year(valid_entries[j]['year']) < extract_year(valid_entries[min_idx]['year']):
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

    # Filtrar solo las entradas con años válidos
    valid_entries = [entry for entry in entries if extract_year(entry['year']) is not None]

    root = None
    # Insertar cada entrada en el árbol (iterativo)
    for entry in valid_entries:
        year = extract_year(entry['year'])
        root = insert_iterative(root, year, entry)

    # Realizar un recorrido in-order para obtener el orden correcto
    sorted_entries = []
    inorder_traversal(root, sorted_entries)

    end_time = time.time()
    return sorted_entries, end_time - start_time

# Aplicar Selection Sort y medir el tiempo
sorted_entries_selection, time_selection_sort = selection_sort(entries_with_year)
print(f"Selection Sort took {time_selection_sort:.6f} seconds")


# Aplicar TimSort y medir el tiempo
sorted_entries_timsort, time_timsort = timsort(entries_with_year)
print(f"TimSort took {time_timsort:.6f} seconds")

# Aplicar Comb Sort y medir el tiempo
sorted_entries_comb, time_comb_sort = comb_sort(entries_with_year)
print(f"Comb Sort took {time_comb_sort:.6f} seconds")
