from tabulate import tabulate

def print_table(sorted_terms):
    print("\nFrecuencia de los términos")
    print(tabulate(sorted_terms, headers=["Término", "Frecuencia"], tablefmt="grid"))