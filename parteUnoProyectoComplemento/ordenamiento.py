import os

def split_bib_file(input_file, output_folder):
    """Divide el archivo .bib en mitades sucesivas y guarda cada una en archivos separados sin saltos de línea adicionales."""
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    total_lines = len(lines)
    if total_lines == 0:
        print("No se encontraron líneas en el archivo .bib. Verifique su contenido.")
        return
    
    filenames = []
    current_lines = lines
    part = 1
    
    while len(current_lines) > 1:
        mid = len(current_lines) // 2
        filename = os.path.join(output_folder, f"todo_filtrado_part{part}.bib")
        with open(filename, "w", encoding="utf-8") as file:
            file.writelines(current_lines[:mid])
        print(f"Archivo creado: {filename} con {mid} líneas")
        filenames.append(filename)
        current_lines = current_lines[mid:]
        part += 1
    
    if current_lines:
        filename = os.path.join(output_folder, f"todo_filtrado_part{part}.bib")
        with open(filename, "w", encoding="utf-8") as file:
            file.writelines(current_lines)
        print(f"Archivo creado: {filename} con {len(current_lines)} líneas")
        filenames.append(filename)

# Definir rutas
resultado_file = r"D:\Z.MIO\X\ALGORITMOS\SEGUIMIENTO\archivos\todo_filtrado_final.bib"
output_folder = r"D:\Z.MIO\X\ALGORITMOS\SEGUIMIENTO\divididos"

# Dividir el archivo en mitades sucesivas sin saltos de línea adicionales
split_bib_file(resultado_file, output_folder)
