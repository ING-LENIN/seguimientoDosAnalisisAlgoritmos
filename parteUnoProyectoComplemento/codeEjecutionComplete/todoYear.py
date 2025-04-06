import matplotlib.pyplot as plt
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
    bibtex_file_path = 'todo_filtrado_final.bib'  # modificar el archivo BibTeX a analizar

    # Leer las entradas del archivo BibTeX
    entries_with_year = read_bibtex_file(bibtex_file_path)

    # Aplicar Tree Sort y medir el tiempo
    sorted_entries_tree, time_tree_sort = tree_sort(entries_with_year)
    
    # Mostrar el tiempo que tomó ordenar
    print(f"Tree Sort took {time_tree_sort:.6f} seconds")

#######################################################################################
    

# Leer el archivo BibTeX utilizando la codificación UTF-8
with open('todo_filtrado_final.bib', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

entries = bib_database.entries
entries_with_year = [entry for entry in entries if 'year' in entry]


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




##########################################################

# Extraer los años utilizando una expresión regular
def extract_year(year_str):
    match = re.match(r'(\d+)', year_str)
    return int(match.group(1)) if match else None

# Obtener los años de las entradas
years = [extract_year(entry['year']) for entry in entries_with_year]

# Funciones de ordenamiento (se mantienen igual)
def pigeonhole_sort(entries, years):
    min_year = min(years)
    max_year = max(years)
    size = max_year - min_year + 1

    # Crear el array pigeonholes vacío
    holes = [[] for _ in range(size)]

    # Colocar cada entrada en el pigeonhole adecuado
    for entry, year in zip(entries, years):
        holes[year - min_year].append(entry)

    # Construir el array ordenado
    sorted_entries = []
    for hole in holes:
        sorted_entries.extend(hole)

    return sorted_entries

def bucket_sort(years):
    max_year = max(years)
    min_year = min(years)
    size = max_year - min_year + 1
    buckets = [[] for _ in range(size)]
    
    for year in years:
        index = year - min_year
        buckets[index].append(year)
    
    sorted_years = []
    for bucket in buckets:
        sorted_years.extend(sorted(bucket))  # Solo ordenar los años dentro del bucket
    return sorted_years


def quicksort(entries, years):
    if len(entries) <= 1:
        return entries
    pivot = years[len(entries) // 2]
    
    left = [e for e, y in zip(entries, years) if y < pivot]
    middle = [e for e, y in zip(entries, years) if y == pivot]
    right = [e for e, y in zip(entries, years) if y > pivot]
    
    return quicksort(left, [y for y in years if y < pivot]) + middle + quicksort(right, [y for y in years if y > pivot])

def heapify(entries, years, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and years[left] > years[largest]:
        largest = left

    if right < n and years[right] > years[largest]:
        largest = right

    if largest != i:
        years[i], years[largest] = years[largest], years[i]
        entries[i], entries[largest] = entries[largest], entries[i]
        heapify(entries, years, n, largest)

def heapsort(entries, years):
    n = len(entries)

    # Crear el max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(entries, years, n, i)

    # Extraer elementos del heap
    for i in range(n - 1, 0, -1):
        years[i], years[0] = years[0], years[i]
        entries[i], entries[0] = entries[0], entries[i]
        heapify(entries, years, i, 0)

    return entries

# Aplicar quicksort y medir el tiempo
start = time.time()
sorted_entries_quicksort = quicksort(entries_with_year, years)
time_quicksort = time.time() - start
print(f"quicksort took {time_quicksort:.6f} seconds")

# Aplicar bucket_sort y medir el tiempo
start = time.time()
sorted_entries_bucket = bucket_sort(years)
time_bucket = time.time() - start
print(f"bucket_sort took {time_bucket:.6f} seconds")

# Aplicar pigeonhole_sort y medir el tiempo
start = time.time()
sorted_entries_pigeonhole = pigeonhole_sort(entries_with_year, years)
time_pigeonhole = time.time() - start
print(f"pigeonhole_sort took {time_pigeonhole:.6f} seconds")

# Aplicar heapsort y medir el tiempo
start = time.time()
sorted_entries_heap = heapsort(entries_with_year, years)
time_heap = time.time() - start
print(f"heapsort took {time_heap:.6f} seconds")


######################################

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

#######################################################3


# Extraer los años utilizando una expresión regular
def extract_year(year_str):
    match = re.match(r'(\d+)', year_str)
    return int(match.group(1)) if match else None

# Obtener los años de las entradas
years = [extract_year(entry['year']) for entry in entries_with_year]

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
def sort_entries(entries, years):
    n = len(years)
    bitonic_sort(years, 0, n, 1)  # 1 para orden ascendente

    sorted_entries = [None] * n
    for i in range(n):
        sorted_entries[i] = entries[years.index(years[i])]
    return sorted_entries

# Guardar las entradas ordenadas en un nuevo archivo
def save_sorted_entries(sorted_entries, filename):
    with open(filename, 'w', encoding='utf-8') as bibtext_file:
        bib_database.entries = sorted_entries
        bibtexparser.dump(bib_database, bibtext_file)

# Medir el tiempo de ejecución
start = time.time()
sorted_entries = sort_entries(entries_with_year, years)
time_bitonic_sort = time.time() - start

# Imprimir resultados
print(f"Bitonic sort took {time_bitonic_sort:.6f} seconds")
#print(f"Años ordenados: {[entry['year'] for entry in sorted_entries]}")



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

######################################


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
plt.title("Comparación de tiempos de ejecución de la variable Year ")
plt.xticks(rotation=45)  # Rotar etiquetas para mejor visibilidad
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar la gráfica
plt.show()