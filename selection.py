import time
import matplotlib.pyplot as plt

SET_1 = 10000
SET_2 = 25000
SET_3 = 50000

def selection_sort(arr):
    """Implementação correta do Selection Sort"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def generate_ascending(set_size):
    """Gera lista ordenada ascendentemente"""
    return list(range(1, set_size + 1))

def generate_descending(set_size):
    """Gera lista ordenada descendentemente"""
    return list(range(set_size, 0, -1))

def generate_random(set_size):
    """Lê lista aleatória do arquivo correspondente"""
    if set_size == SET_1:
        filename = "set1.txt"
    elif set_size == SET_2:
        filename = "set2.txt"
    elif set_size == SET_3:
        filename = "set3.txt"
    else:
        raise ValueError("Tamanho de conjunto inválido")
    
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f]

def measure_performance():
    """Mede o desempenho e gera gráfico"""
    set_sizes = [SET_1, SET_2, SET_3]
    generators = [
        ("Crescente", generate_ascending),
        ("Decrescente", generate_descending),
        ("Aleatório", generate_random)
    ]
    
    results = {name: [] for name, _ in generators}
    
    for size in set_sizes:
        print(f"\nTestando para tamanho: {size}")
        for name, generator in generators:
            dataset = generator(size)
            
            # Medir tempo com cópia para não alterar o dataset original
            start = time.perf_counter()
            selection_sort(dataset.copy())
            elapsed = time.perf_counter() - start
            
            results[name].append(elapsed)
            print(f"{name}: {elapsed:.3f}s")
        
    print(results["Decrescente"])

    # Plotar resultados
    plt.figure(figsize=(10, 6))
    for name in results:
        plt.plot(set_sizes, results[name], marker='o', label=name)
    
    plt.xlabel("Tamanho do Conjunto")
    plt.ylabel("Tempo de Execução (s)")
    plt.title("Desempenho do Selection Sort")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    measure_performance()