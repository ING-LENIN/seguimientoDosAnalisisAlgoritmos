import os
import glob

def merge_bib_files(input_folder, output_file):
    """
    Lee todos los archivos .bib en la carpeta de entrada, extrae sus contenidos y
    los guarda en un único archivo de salida manteniendo el formato dado.
    """
    bib_files = glob.glob(os.path.join(input_folder, "*.bib"))
    
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write("@comment{Scopus\nEXPORT DATE: 09 October 2024}\n\n")  # Encabezado fijo
        
        for bib_file in bib_files:
            with open(bib_file, "r", encoding="utf-8") as infile:
                content = infile.read().strip()
                outfile.write(content + "\n\n")  # Agrega un salto de línea entre archivos
    
    print(f"Se han combinado {len(bib_files)} archivos en {output_file}")

# Ejemplo de uso
input_folder = r"C:\Users\Familia Cortes\Documents\CRISTIAN UNIVERSIDAD\SEMESTRE X\ALGORITMO\APOYO\PROYECTO FINAL\descargas"
output_file = r"C:\Users\Familia Cortes\Documents\CRISTIAN UNIVERSIDAD\SEMESTRE X\ALGORITMO\APOYO\PROYECTO FINAL\Resultados\todo_filtrado_final.bib"
merge_bib_files(input_folder, output_file)
