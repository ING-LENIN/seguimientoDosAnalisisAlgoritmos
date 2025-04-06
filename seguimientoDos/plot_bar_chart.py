import matplotlib.pyplot as plt

def plot_bar_chart(sorted_terms, execution_time, algorithm_name):
    terms, frequencies = zip(*sorted_terms)
    plt.figure(figsize=(12, 6))
    plt.bar(terms, frequencies, color='skyblue')
    plt.xlabel("Términos")
    plt.ylabel("Frecuencia")
    plt.title(f"{algorithm_name} - Tiempo: {execution_time:.6f} segundos")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()