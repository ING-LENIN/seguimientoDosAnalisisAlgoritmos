import time
import bibtexparser
import re
import matplotlib.pyplot as plt


# Leer el archivo bibtex
with open('todo_filtrado_final.bib', encoding='utf-8') as bibtext_file:
    bib_database = bibtexparser.load(bibtext_file)

entries = bib_database.entries
entries_with_pages = [entry for entry in entries if 'pages' in entry]  # Filtrar entradas que tengan 'pages'

# Función para extraer el número de páginas
def extract_pages(entry):
    pages = entry.get('pages', '')
    match = re.match(r'(\d+)-(\d+)', pages)  # Extraer el rango de páginas "start_page-end_page"
    if match:
        start_page = int(match.group(1))
        end_page = int(match.group(2))
        return end_page - start_page + 1  # Calcular el número de páginas
    return 0  # Si no hay información de páginas, devolver 0

# Obtener el número de páginas de las entradas
pages = [extract_pages(entry) for entry in entries_with_pages]

# Funciones de ordenamiento

def pigeonhole_sort(entries, pages):
    min_pages = min(pages)
    max_pages = max(pages)
    size = max_pages - min_pages + 1

    # Crear un array de pigeonholes vacío
    holes = [[] for _ in range(size)]

    # Colocar cada entrada en el pigeonhole adecuado
    for entry, page_count in zip(entries, pages):
        holes[page_count - min_pages].append(entry)

    # Construir el array ordenado
    sorted_entries = []
    for hole in holes:
        sorted_entries.extend(hole)

    return sorted_entries

def bucket_sort(entries, pages):
    max_pages = max(pages)
    size = len(entries)

    # Crear buckets vacíos
    buckets = [[] for _ in range(size)]

    # Distribuir las entradas en los buckets
    for i in range(size):
        index = pages[i] * size // (max_pages + 1)
        buckets[index].append((pages[i], entries[i]))

    # Ordenar los buckets y combinarlos
    sorted_entries = []
    for bucket in buckets:
        sorted_entries.extend(sorted(bucket, key=lambda x: x[0]))  # Ordenar por el número de páginas (x[0])

    sorted_entries = [entry for _, entry in sorted_entries]  # Obtener solo las entradas, no los números de páginas
    return sorted_entries

def quicksort_entries(entries, pages):
    if len(entries) <= 1:
        return entries
    
    pivot = pages[len(entries) // 2]
    
    left = [(p, e) for p, e in zip(pages, entries) if p < pivot]
    middle = [(p, e) for p, e in zip(pages, entries) if p == pivot]
    right = [(p, e) for p, e in zip(pages, entries) if p > pivot]

    return quicksort_entries([e for _, e in left], [p for p, _ in left]) + \
           [e for _, e in middle] + \
           quicksort_entries([e for _, e in right], [p for p, _ in right])

def heapify(entries, pages, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and pages[left] > pages[largest]:
        largest = left

    if right < n and pages[right] > pages[largest]:
        largest = right

    if largest != i:
        pages[i], pages[largest] = pages[largest], pages[i]
        entries[i], entries[largest] = entries[largest], entries[i]
        heapify(entries, pages, n, largest)

def heapsort(entries, pages):
    n = len(entries)

    # Crear el max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(entries, pages, n, i)

    # Extraer elementos del heap
    for i in range(n - 1, 0, -1):
        pages[i], pages[0] = pages[0], pages[i]
        entries[i], entries[0] = entries[0], entries[i]
        heapify(entries, pages, i, 0)

    return entries

# Aplicar quicksort y medir el tiempo
start = time.time()
sorted_entries_quicksort = quicksort_entries(entries_with_pages, pages)
time_quicksort = time.time() - start
print(f"quicksort took {time_quicksort:.6f} seconds")

# Aplicar bucket_sort y medir el tiempo
start = time.time()
sorted_entries_bucket = bucket_sort(entries_with_pages, pages)
time_bucket = time.time() - start
print(f"bucket_sort took {time_bucket:.6f} seconds")

# Aplicar pigeonhole_sort y medir el tiempo
start = time.time()
sorted_entries_pigeonhole = pigeonhole_sort(entries_with_pages, pages)
time_pigeonhole = time.time() - start
print(f"pigeonhole_sort took {time_pigeonhole:.6f} seconds")

# Aplicar heapsort y medir el tiempo
start = time.time()
sorted_entries_heap = heapsort(entries_with_pages, pages)
time_heap = time.time() - start
print(f"heapsort took {time_heap:.6f} seconds")


#########################################


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


# Leer el archivo bibtex
with open('todo_filtrado_final.bib', encoding='utf-8') as bibtext_file:
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

####################################################################3


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


# Leer el archivo bibtex
with open('todo_filtrado_final.bib', encoding='utf-8') as bibtext_file:
    bib_database = bibtexparser.load(bibtext_file)

entries = bib_database.entries

# Filtrar entradas que tienen el campo 'pages'
entries_with_pages = [entry for entry in entries if 'pages' in entry]

# Extraer los valores de 'pages'
def extract_pages(pages_str):
    match = re.match(r'(\d+)', pages_str)  # Extrae el primer número en 'pages'
    return int(match.group(1)) if match else 0

# Obtener las páginas de las entradas
pages = [extract_pages(entry['pages']) for entry in entries_with_pages]

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

# Ordenar las entradas utilizando Bitonic Sort por 'pages'
def sort_entries(entries, pages):
    n = len(pages)
    bitonic_sort(pages, 0, n, 1)  # 1 para orden ascendente

    sorted_entries = [None] * n
    for i in range(n):
        sorted_entries[i] = entries[pages.index(pages[i])]
    return sorted_entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_pages, pages)
time_bitonic_sort = time.time() - start

# Imprimir resultados
print(f"Bitonic sort took {time_bitonic_sort:.6f} seconds")
#print(f"Páginas ordenadas: {[entry['pages'] for entry in sorted_entries]}")

# Leer el archivo bibtex
with open('todo_filtrado_final.bib', encoding='utf-8') as bibtext_file:
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

# Función de búsqueda binaria
def binary_search(pages, page, high):
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if pages[mid] < page:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Función de Binary Insertion Sort
def binary_insertion_sort(pages, entries):
    for i in range(1, len(pages)):
        page = pages[i]
        entry = entries[i]
        
        # Encuentra la posición correcta para la página actual
        pos = binary_search(pages, page, i - 1)
        
        # Mueve los elementos hacia la derecha
        pages[pos + 1:i + 1] = pages[pos:i]
        entries[pos + 1:i + 1] = entries[pos:i]
        
        # Coloca la página actual en la posición correcta
        pages[pos] = page
        entries[pos] = entry

# Ordenar las entradas utilizando Binary Insertion Sort por 'pages'
def sort_entries(entries, pages):
    binary_insertion_sort(pages, entries)
    return entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_pages, pages)
time_binary_insertion_sort = time.time() - start

# Imprimir resultados
print(f"Binary insertion sort took {time_binary_insertion_sort:.6f} seconds")
#print(f"Páginas ordenadas: {[entry['pages'] for entry in sorted_entries]}")


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
plt.title("Comparación de tiempos de ejecución de la variable Page ")
plt.xticks(rotation=45)  # Rotar etiquetas para mejor visibilidad
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar la gráfica
plt.show()