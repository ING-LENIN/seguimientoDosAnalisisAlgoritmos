import bibtexparser
import re
import time

# Clase para representar un nodo del árbol
class Node:
    def __init__(self, key, entry):
        self.left = None
        self.right = None
        self.val = key
        self.entry = entry  # Almacena la entrada completa

# Función para extraer el año de una cadena
def extract_year(year_str):
    match = re.match(r'(\d+)', year_str)
    return int(match.group(1)) if match else None

# Inserción iterativa en el árbol binario
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
        else:  # Manejar duplicados
            if current.right is None:
                current.right = new_node
                break
            current = current.right

    return root

# Recorrido in-order para obtener los elementos en orden
def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.entry)  # Añadir la entrada completa al resultado
        inorder_traversal(root.right, result)

# Algoritmo de Tree Sort
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

# Leer el archivo BibTeX
def read_bibtex_file(file_path):
    with open(file_path, encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database.entries

# Ejecución principal
if __name__ == "__main__":
    bibtex_file_path = 'todo_filtrado_part7.bib'  # modificar el archivo BibTeX a analizar

    # Leer las entradas del archivo BibTeX
    entries_with_year = read_bibtex_file(bibtex_file_path)

    # Aplicar Tree Sort y medir el tiempo
    sorted_entries_tree, time_tree_sort = tree_sort(entries_with_year)
    
    # Mostrar el tiempo que tomó ordenar
    print(f"Tree Sort took {time_tree_sort:.6f} seconds")
    
