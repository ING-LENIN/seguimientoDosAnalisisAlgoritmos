import time
import bibtexparser
import matplotlib.pyplot as plt
import re

# Leer el archivo bibtex
with open('todo_filtrado_final.bib', encoding='utf-8') as bibtext_file:
    bib_database = bibtexparser.load(bibtext_file)

entries = bib_database.entries
entries_with_author = [entry for entry in entries if 'author' in entry]  # Filtrar entradas que tengan 'author'

# Función para extraer el autor (asumiendo que solo tomamos el primer autor)
def extract_author(entry):
    authors = entry.get('author', '')
    return authors.split(' and ')[0]  # Retornar el primer autor, asumiendo que se separan por 'and'

# Obtener los autores de las entradas
authors = [extract_author(entry) for entry in entries_with_author]

# Funciones de ordenamiento
def pigeonhole_sort(entries, authors):
    # Crear un diccionario para almacenar las entradas por autor
    author_dict = {}
    
    for entry, author in zip(entries, authors):
        if author not in author_dict:
            author_dict[author] = []
        author_dict[author].append(entry)

    # Construir el array ordenado
    sorted_entries = []
    for author in sorted(author_dict.keys()):  # Ordenar las claves (autores)
        sorted_entries.extend(author_dict[author])

    return sorted_entries

def bucket_sort(authors):
    buckets = {}

    for author in authors:
        if author:  # Verificar que el autor no esté vacío
            key = author[0]  # Tomamos la primera letra del autor como clave
            if key not in buckets:
                buckets[key] = []
            buckets[key].append(author)

    sorted_authors = []
    for key in sorted(buckets.keys()):
        sorted_authors.extend(sorted(buckets[key]))  # Solo ordenar los autores dentro del bucket
    return sorted_authors

def quicksort_authors(entries, authors):
    if len(entries) <= 1:
        return entries
    pivot = authors[len(entries) // 2]
    
    left = [e for e, a in zip(entries, authors) if a < pivot]
    middle = [e for e, a in zip(entries, authors) if a == pivot]
    right = [e for e, a in zip(entries, authors) if a > pivot]
    
    return quicksort_authors(left, [a for a in authors if a < pivot]) + middle + quicksort_authors(right, [a for a in authors if a > pivot])

def heapify(entries, authors, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and authors[left] > authors[largest]:
        largest = left

    if right < n and authors[right] > authors[largest]:
        largest = right

    if largest != i:
        authors[i], authors[largest] = authors[largest], authors[i]
        entries[i], entries[largest] = entries[largest], entries[i]
        heapify(entries, authors, n, largest)

def heapsort(entries, authors):
    n = len(entries)

    # Crear el max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(entries, authors, n, i)

    # Extraer elementos del heap
    for i in range(n - 1, 0, -1):
        authors[i], authors[0] = authors[0], authors[i]
        entries[i], entries[0] = entries[0], entries[i]
        heapify(entries, authors, i, 0)

    return entries

# Aplicar quicksort y medir el tiempo
start = time.time()
sorted_entries_quicksort = quicksort_authors(entries_with_author, authors)
time_quicksort = time.time() - start
print(f"quicksort took {time_quicksort:.6f} seconds")

# Aplicar bucket_sort y medir el tiempo
start = time.time()
sorted_authors_bucket = bucket_sort(authors)  # Solo ordenar autores aquí
time_bucket = time.time() - start
print(f"bucket_sort took {time_bucket:.6f} seconds")

# Aplicar pigeonhole_sort y medir el tiempo
start = time.time()
sorted_entries_pigeonhole = pigeonhole_sort(entries_with_author, authors)
time_pigeonhole = time.time() - start
print(f"pigeonhole_sort took {time_pigeonhole:.6f} seconds")

# Aplicar heapsort y medir el tiempo
start = time.time()
sorted_entries_heap = heapsort(entries_with_author, authors)
time_heap = time.time() - start
print(f"heapsort took {time_heap:.6f} seconds")



################################################
# Leer el archivo BibTeX utilizando la codificación UTF-8
with open('todo_filtrado_final.bib', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

entries = bib_database.entries
entries_with_author = [entry for entry in entries if 'author' in entry]  # Filtrar entradas que tengan 'author'

# Función para extraer el autor (asumiendo que solo tomamos el primer autor)
def extract_author(entry):
    authors = entry.get('author', '')
    return authors.split(' and ')[0]  # Retornar el primer autor, asumiendo que se separan por 'and'

def timsort(entries):
    start_time = time.time()
    # Filtrar solo las entradas con autores válidos
    valid_entries = [entry for entry in entries if extract_author(entry)]
    
    sorted_entries = sorted(valid_entries, key=extract_author)
    end_time = time.time()
    return sorted_entries, end_time - start_time

def comb_sort(arr):
    start_time = time.time()

    # Filtrar solo las entradas con autores válidos
    valid_entries = [entry for entry in arr if extract_author(entry)]
    
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
            if extract_author(valid_entries[i]) > extract_author(valid_entries[i + gap]):
                valid_entries[i], valid_entries[i + gap] = valid_entries[i + gap], valid_entries[i]
                sorted_flag = False
            i += 1

    end_time = time.time()
    return valid_entries, end_time - start_time

def selection_sort(arr):
    start_time = time.time()

    # Filtrar solo las entradas con autores válidos
    valid_entries = [entry for entry in arr if extract_author(entry)]

    for i in range(len(valid_entries)):
        min_idx = i
        for j in range(i + 1, len(valid_entries)):
            if extract_author(valid_entries[j]) < extract_author(valid_entries[min_idx]):
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

    # Filtrar solo las entradas con autores válidos
    valid_entries = [entry for entry in entries if extract_author(entry)]

    root = None
    # Insertar cada entrada en el árbol (iterativo)
    for entry in valid_entries:
        author = extract_author(entry)
        root = insert_iterative(root, author, entry)

    # Realizar un recorrido in-order para obtener el orden correcto
    sorted_entries = []
    inorder_traversal(root, sorted_entries)

    end_time = time.time()
    return sorted_entries, end_time - start_time

# Aplicar Selection Sort y medir el tiempo
sorted_entries_selection, time_selection_sort = selection_sort(entries_with_author)
print(f"Selection Sort took {time_selection_sort:.6f} seconds")

# Aplicar TimSort y medir el tiempo
sorted_entries_timsort, time_timsort = timsort(entries_with_author)
print(f"TimSort took {time_timsort:.6f} seconds")

# Aplicar Comb Sort y medir el tiempo
sorted_entries_comb, time_comb_sort = comb_sort(entries_with_author)
print(f"Comb Sort took {time_comb_sort:.6f} seconds")

# Aplicar Tree Sort y medir el tiempo
sorted_entries_tree, time_tree_sort = tree_sort(entries_with_author)
print(f"Tree Sort took {time_tree_sort:.6f} seconds")


#######################################################

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

###########################33


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

########################33


# Extraer autores
def extract_author(author_str):
    # Aquí puedes ajustar la forma en que extraes los autores si es necesario
    return author_str

# Obtener los autores de las entradas
authors = [extract_author(entry['author']) for entry in entries_with_author]

# Funciones de Bitonic Sort
def compare_and_swap(arr, i, j, dire):
    if (dire == 1 and arr[i] > arr[j]) or (dire == 0 and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]

def bitonic_merge(arr, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compare_and_swap(arr, i, i + k, dire)
        bitonic_merge(arr, low, k, dire)
        bitonic_merge(arr, low + k, k, dire)

def bitonic_sort(arr, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        bitonic_sort(arr, low, k, 1)  # Ascendente
        bitonic_sort(arr, low + k, k, 0)  # Descendente
        bitonic_merge(arr, low, cnt, dire)

# Ordenar las entradas utilizando Bitonic Sort
def sort_entries(entries, authors):
    n = len(authors)
    bitonic_sort(authors, 0, n, 1)  # 1 para orden ascendente

    sorted_entries = [None] * n
    for i in range(n):
        sorted_entries[i] = entries[authors.index(authors[i])]
    return sorted_entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_author, authors)
time_bitonic_sort = time.time() - start

# Imprimir resultados
print(f"Bitonic sort took {time_bitonic_sort:.6f} seconds")
#print(f"Autores ordenados: {[entry['author'] for entry in sorted_entries]}")


###############################3

# Extraer autores
def extract_author(author_str):
    # Aquí puedes ajustar la forma en que extraes los autores si es necesario
    return author_str

# Obtener los autores de las entradas
authors = [extract_author(entry['author']) for entry in entries_with_author]

# Función de búsqueda binaria
def binary_search(authors, author, high):
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if authors[mid] < author:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Función de Binary Insertion Sort
def binary_insertion_sort(authors, entries):
    for i in range(1, len(authors)):
        author = authors[i]
        entry = entries[i]
        
        # Encuentra la posición correcta para el autor actual
        pos = binary_search(authors, author, i - 1)
        
        # Mueve los elementos hacia la derecha
        authors[pos + 1:i + 1] = authors[pos:i]
        entries[pos + 1:i + 1] = entries[pos:i]
        
        # Coloca el autor actual en la posición correcta
        authors[pos] = author
        entries[pos] = entry

# Ordenar las entradas utilizando Binary Insertion Sort
def sort_entries(entries, authors):
    binary_insertion_sort(authors, entries)
    return entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_author, authors)
time_binary_insertion_sort = time.time() - start

# Imprimir resultados
print(f"Binary insertion sort took {time_binary_insertion_sort:.6f} seconds")
#print(f"Autores ordenados: {[entry['author'] for entry in sorted_entries]}")







#----------------Mostrar el grafico-------------------------------------------#

# Nombres de los algoritmos (completa los faltantes)
sorting_algorithms = [
    "QuickSort", "Bucket Sort", "Pigeonhole Sort", "HeapSort",
    "Selection Sort", "TimSort", "Comb Sort", "Tree Sort",
    "Merge Sort", "Bubble Sort", "Insertion Sort", "Radix Sort"
]

# Tiempos de ejecución obtenidos de tu código (completa los faltantes)
execution_times = [
    time_quicksort, time_bucket, time_pigeonhole, time_heap,
    time_selection_sort, time_timsort, time_comb_sort, time_tree_sort,
    time_bitonic_sort, time_gnome_sort, time_binary_insertion_sort, time_radix_sort
]

# Crear la gráfica de barras
plt.figure(figsize=(12, 6))
plt.bar(sorting_algorithms, execution_times, color='skyblue')

# Agregar etiquetas y títulos
plt.xlabel("Algoritmos de Ordenamiento")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de tiempos de ejecución de la variable Author ")
plt.xticks(rotation=45)  # Rotar etiquetas para mejor visibilidad
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar la gráfica
plt.show()