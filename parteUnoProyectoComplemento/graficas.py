import matplotlib.pyplot as plt

# grafica years
tiemposYears = [0.060358, 1.105020, 241.40654, 2.1275638, 0.005067, 0.002505, 0.103138, 
           0.193129, 1.587914, 35.890394, 4.188949, 0.022962]

metodosYears = [
    "TimSort", "Comb Sort", "Selection Sort", "Tree Sort", 
    "Pigeonhole Sort", "BucketSort", "QuickSort", "HeapSort", 
    "Bitonic Sort", "Gnome Sort", "Binary Insertion Sort", "RadixSort"
]

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.barh(metodosYears, tiemposYears, color='skyblue')
plt.xlabel('Tiempo de Ejecución (segundos)')
plt.title('Tiempos de Ejecución de Métodos de Ordenamiento (variable years)')
plt.gca().invert_yaxis() 
plt.tight_layout()
plt.show()

# Grafica Author
metodosAuthor = [
    "TimSort", "Comb Sort", "Selection Sort", "Tree Sort", "Pigeonhole Sort", 
    "BucketSort", "QuickSort", "HeapSort", "Bitonic Sort", "Gnome Sort", 
    "Binary Insertion Sort", "RadixSort"
]

tiemposAuthor = [0.031254, 0.877224, 135.786038, 0.065637, 0.533359, 0.038301, 
                  0.505299, 0.295858, 2.112978, 34.471899, 2.052423, 21.255575]

plt.figure(figsize=(10,6))
plt.barh(metodosAuthor, tiemposAuthor, color='lightcoral')
plt.xlabel('Tiempo de Ejecución (segundos)')
plt.title('Comparación de Tiempos de Ejecución por Método de Ordenamiento (Authors)')
plt.gca().invert_yaxis()
plt.show()


# Grafica Pages
metodosPages = [
    "TimSort", "Comb Sort", "Selection Sort", "Tree Sort", "Pigeonhole Sort", 
    "BucketSort", "QuickSort", "HeapSort", "Bitonic Sort", "Gnome Sort", 
    "Binary Insertion Sort", "RadixSort"
]

tiempoPages = [0.016239, 0.186602, 12.443721, 0.028088, 0.007045, 0.050623, 
                   0.412107, 0.071310, 0.940975, 18.663934, 1.107059, 0.265684]

# Crear la nueva gráfica
plt.figure(figsize=(10,6))
plt.barh(metodosPages, tiempoPages, color='lightgreen')
plt.xlabel('Tiempo de Ejecución (segundos)')
plt.title('Comparación de Tiempos de Ejecución por Método de Ordenamiento (Pages)')
plt.gca().invert_yaxis()  
plt.show()
