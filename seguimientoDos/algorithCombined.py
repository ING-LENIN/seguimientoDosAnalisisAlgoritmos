import os
import glob

def merge_bib_files(input_folder, output_file):
    """
    Lee todos los archivos .bib en la carpeta de entrada y los combina en un único archivo de salida.
    No se aplica ningún filtro ni criterio de selección.
    """
    # Encontrar todos los archivos .bib en la carpeta de entrada
    bib_files = glob.glob(os.path.join(input_folder, "*.bib"))
    
    # Abrir el archivo de salida para escribir el contenido combinado
    with open(output_file, "w", encoding="utf-8") as outfile:
        # Iterar sobre cada archivo .bib
        for bib_file in bib_files:
            try:
                with open(bib_file, "r", encoding="utf-8") as infile:
                    content = infile.read().strip()
                    if content:  # Asegurarse de que el archivo no esté vacío
                        outfile.write(content + "\n\n")  # Escribir el contenido con una línea en blanco entre archivos
            except Exception as e:
                print(f"Error al procesar el archivo {bib_file}: {e}")
    
    print(f"Se han combinado {len(bib_files)} archivos en {output_file}")

# Ejemplo de uso
input_folder = r"C:\Users\user\Documents\INGENIERIA DE SISTEMAS\SEMESTRE 10\ANALISIS DE ALGORITMOS\TAREA\descargas"
output_file = r"C:\Users\user\Documents\INGENIERIA DE SISTEMAS\SEMESTRE 10\ANALISIS DE ALGORITMOS\TAREA\complete.bib"

# Llamar a la función para combinar los archivos
merge_bib_files(input_folder, output_file)