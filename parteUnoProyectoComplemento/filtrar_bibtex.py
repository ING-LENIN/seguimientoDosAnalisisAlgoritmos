import bibtexparser

# Ruta del archivo combinado y donde se guardará el archivo filtrado
input_file = r"C:\Users\USER\Documents\UNIVERSIDAD\ANALISIS ALGORITMOS\Bases de datos Algoritmos-20241009T184346Z-001\Bases de datos Algoritmos\todo.bib"
output_file = r"C:\Users\USER\Documents\UNIVERSIDAD\ANALISIS ALGORITMOS\Bases de datos Algoritmos-20241009T184346Z-001\Bases de datos Algoritmos\todo_filtrado.bib"

# Campos requeridos
required_fields = {"title", "journal", "url", "abstract", "author", "year", "volume", "pages"}

# Función para verificar si un registro tiene todos los campos requeridos
def has_required_fields(entry):
    return all(field in entry and entry[field].strip() for field in required_fields)

# Función para eliminar duplicados usando el campo 'title' como clave
def remove_duplicates(entries):
    seen_titles = set()
    unique_entries = []
    
    for entry in entries:
        # Usamos el título como clave, ignorando mayúsculas y espacios en blanco adicionales
        title_key = entry.get('title', '').strip().lower()
        
        if title_key and title_key not in seen_titles:
            unique_entries.append(entry)
            seen_titles.add(title_key)
    
    return unique_entries

# Leer el archivo bibtex original
with open(input_file, encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Filtrar los registros que cumplen con los campos requeridos
original_count = len(bib_database.entries)
filtered_entries = [entry for entry in bib_database.entries if has_required_fields(entry)]
filtered_entries = remove_duplicates(filtered_entries)
filtered_count = len(filtered_entries)
removed_count = original_count - filtered_count

# Guardar los registros filtrados y sin duplicados en un nuevo archivo bibtex
bib_database.entries = filtered_entries
with open(output_file, 'w', encoding='utf-8') as bibtex_file:
    bibtexparser.dump(bib_database, bibtex_file)

# Imprimir cuántos registros quedaron y cuántos fueron eliminados
print(f"Registros originales: {original_count}")
print(f"Registros después de eliminar los no válidos y duplicados: {filtered_count}")
print(f"Registros eliminados: {removed_count}")
