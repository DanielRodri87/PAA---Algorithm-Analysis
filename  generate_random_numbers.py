import numpy as np

SET_1 = 100000
SET_2 = 250000
SET_3 = 500000

def generate_random_files(file_name, size):
    numbers = np.random.randint(0, 1000000, size)
    np.savetxt(file_name, numbers, fmt="%d")
    print(f"Arquivo {file_name} gerado com {size} números.")

generate_random_files("set1.txt", SET_1)
generate_random_files("set2.txt", SET_2)
generate_random_files("set3.txt", SET_3)