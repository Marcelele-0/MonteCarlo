import json
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_max_load_results(results_file, output_filenames=None):
    os.makedirs(os.path.dirname(results_file), exist_ok=True)
    with open(results_file, 'r') as file:
        data = json.load(file)

    n_values = [entry['n'] for entry in data]
    max_load_d1_values = [entry['max_load_d1'] for entry in data]
    max_load_d2_values = [entry['max_load_d2'] for entry in data]
    mean_load_d1 = [np.mean(entry['max_load_d1']) for entry in data]
    mean_load_d2 = [np.mean(entry['max_load_d2']) for entry in data]

    # Wykres maksymalnych obciążeń dla d=1
    plt.figure(figsize=(10, 6))
    for i, n in enumerate(n_values):
        plt.scatter([n] * len(max_load_d1_values[i]), max_load_d1_values[i], color='blue', alpha=0.5)
    plt.plot(n_values, mean_load_d1, label='Średnia (d=1)', color='red', marker='o')
    plt.xlabel('Liczba kubełków (n)')
    plt.ylabel('Maksymalne obciążenie')
    plt.title('Maksymalne obciążenie vs liczba kubełków (d=1)')
    plt.legend()
    plt.grid(True)

    if output_filenames:
        os.makedirs(os.path.dirname(output_filenames[0]), exist_ok=True)
        plt.savefig(output_filenames[0], format='png')
        print(f'Wykres maksymalnych obciążeń (d=1) zapisano do pliku {output_filenames[0]}')

    plt.show()

    # Wykres maksymalnych obciążeń dla d=2
    plt.figure(figsize=(10, 6))
    for i, n in enumerate(n_values):
        plt.scatter([n] * len(max_load_d2_values[i]), max_load_d2_values[i], color='green', alpha=0.5)
    plt.plot(n_values, mean_load_d2, label='Średnia (d=2)', color='orange', marker='o')
    plt.xlabel('Liczba kubełków (n)')
    plt.ylabel('Maksymalne obciążenie')
    plt.title('Maksymalne obciążenie vs liczba kubełków (d=2)')
    plt.legend()
    plt.grid(True)

    if output_filenames:
        os.makedirs(os.path.dirname(output_filenames[1]), exist_ok=True)
        plt.savefig(output_filenames[1], format='png')
        print(f'Wykres maksymalnych obciążeń (d=2) zapisano do pliku {output_filenames[1]}')

    plt.show()

    # Obliczenia dla funkcji f1(n) i f2(n)
    f1_values = [np.log(n) / np.log(np.log(n)) for n in n_values]
    f2_values = [np.log(np.log(n)) / np.log(2) for n in n_values]

    # Wykres l(1)n vs f1(n) i f2(n)
    plt.figure(figsize=(10, 6))
    plt.plot(f1_values, mean_load_d1, label='l(1)n vs f1(n)', color='blue', marker='o')
    plt.plot(f2_values, mean_load_d1, label='l(1)n vs f2(n)', color='red', marker='x')
    plt.xlabel('f1(n) i f2(n)')
    plt.ylabel('Średnie obciążenie (d=1)')
    plt.title('Średnie obciążenie (d=1) vs f1(n) i f2(n)')
    plt.legend()
    plt.grid(True)

    if output_filenames:
        extra_output_filename = output_filenames[0].replace('max_load_plot', 'extra_plot_d1')
        os.makedirs(os.path.dirname(extra_output_filename), exist_ok=True)
        plt.savefig(extra_output_filename, format='png')
        print(f'Wykres l(1)n vs f1(n) i f2(n) zapisano do pliku {extra_output_filename}')

    plt.show()

    # Wykres l(2)n vs f1(n) i f2(n)
    plt.figure(figsize=(10, 6))
    plt.plot(f1_values, mean_load_d2, label='l(2)n vs f1(n)', color='green', marker='o')
    plt.plot(f2_values, mean_load_d2, label='l(2)n vs f2(n)', color='orange', marker='x')
    plt.xlabel('f1(n) i f2(n)')
    plt.ylabel('Średnie obciążenie (d=2)')
    plt.title('Średnie obciążenie (d=2) vs f1(n) i f2(n)')
    plt.legend()
    plt.grid(True)

    if output_filenames:
        extra_output_filename = output_filenames[1].replace('mean_load_plot', 'extra_plot_d2')
        os.makedirs(os.path.dirname(extra_output_filename), exist_ok=True)
        plt.savefig(extra_output_filename, format='png')
        print(f'Wykres l(2)n vs f1(n) i f2(n) zapisano do pliku {extra_output_filename}')

    plt.show()
