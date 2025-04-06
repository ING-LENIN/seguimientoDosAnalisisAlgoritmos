import os

# Ruta absoluta del directorio donde están tus archivos bibtex
bibtex_dir = r'C:\Users\USER\Documents\UNIVERSIDAD\ANALISIS ALGORITMOS\Bases de datos Algoritmos-20241009T184346Z-001\Bases de datos Algoritmos\Todos'
# Ruta absoluta del archivo de salida
output_file = r'C:\Users\USER\Documents\UNIVERSIDAD\ANALISIS ALGORITMOS\Bases de datos Algoritmos-20241009T184346Z-001\Bases de datos Algoritmos\todo.bib'

# Abrir archivo de salida en modo de escritura y especificar codificación
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Iterar sobre todos los archivos del directorio
    for filename in os.listdir(bibtex_dir):
        # Procesar solo archivos con extensión .bib
        if filename.endswith(".bib"):
            # Leer archivo con codificación UTF-8
            with open(os.path.join(bibtex_dir, filename), 'r', encoding='utf-8') as infile:
                # Escribir contenido de cada archivo bib en el archivo de salida
                outfile.write(infile.read())
                outfile.write('\n\n')  # Añadir separación entre registros
