#para crear el archivo basura
import os
import glob

def merge_bib_files(input_folder, output_file, unused_file):
    """
    Lee todos los archivos .bib en la carpeta de entrada, extrae sus contenidos y
    los guarda en un único archivo de salida manteniendo el formato dado.
    También almacena los datos no utilizados en otro archivo.
    """
    bib_files = glob.glob(os.path.join(input_folder, "*.bib"))
    
    with open(output_file, "w", encoding="utf-8") as outfile, open(unused_file, "w", encoding="utf-8") as unused_outfile:
        outfile.write("@comment{Scopus\nEXPORT DATE: 09 October 2024}\n\n")  # Encabezado fijo
        unused_outfile.write("@comment{Archivos no utilizados}\n\n")
        
        for bib_file in bib_files:
            with open(bib_file, "r", encoding="utf-8") as infile:
                content = infile.read().strip()
                if "@ARTICLE" in content or "@article" in content:  # Criterio de selección
                    outfile.write(content + "\n\n")  # Guardar en archivo principal
                else:
                    unused_outfile.write(content + "\n\n")  # Guardar en archivo de basura
    
    print(f"Se han combinado {len(bib_files)} archivos en {output_file}")
    print(f"Los datos no utilizados se guardaron en {unused_file}")

# Ejemplo de uso
input_folder = r"D:\Z.MIO\X\ALGORITMOS\SEGUIMIENTO\descargas"
output_file = r"D:\Z.MIO\X\ALGORITMOS\SEGUIMIENTO\archivos\todo_filtrado_final.bib"
unused_file = r"D:\Z.MIO\X\ALGORITMOS\SEGUIMIENTO\archivos\archivos_no_utilizados.bib"
merge_bib_files(input_folder, output_file, unused_file)
