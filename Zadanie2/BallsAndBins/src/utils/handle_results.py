import matplotlib.pyplot as plt
import numpy as np
import json
import os


def plot_and_save_results(results_dict, variable_name, output_filename=None):
    """
    Wyświetla wyniki dla danej zmiennej i zapisuje wykres do pliku PNG, jeśli podano nazwę pliku.

    Args:
        results_dict (dict): Słownik z wynikami symulacji, gdzie kluczami są wartości n, a wartościami listy wyników.
        variable_name (str): Nazwa zmiennej do wyświetlenia.
        output_filename (str, optional): Ścieżka do pliku PNG, do którego ma być zapisany wykres.
    """
    n_values = sorted(results_dict.keys())
    mean_values = [np.mean(results_dict[n]) for n in n_values]

    plt.figure(figsize=(20, 10))
    for n in n_values:
        plt.scatter([n] * len(results_dict[n]), results_dict[n], c='blue', label=f'Powtórzenia dla n={n}', alpha=0.6, s=2)

    plt.plot(n_values, mean_values, label=f'Średnia {variable_name}(n)', color='red', marker='o')

    plt.xlabel('n')
    plt.ylabel(variable_name)
    plt.title(f'Wyniki poszczególnych powtórzeń oraz średnia dla {variable_name}')
    plt.grid(True)

    if output_filename:
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        plt.savefig(output_filename, format='png')
        print(f'Wykres zapisano do pliku {output_filename}')


def plot_and_save_extra_Bn_results(results_dict, variable_name, output_filename=None):
    """
    Rysuje wykres b(n)/n oraz b(n)/sqrt(n) jako funkcji n na podstawie wyników zapisanych w pliku JSON.
    """
    n_values = sorted(results_dict.keys())

    Bn_over_n = [np.mean(results_dict[n]) / n for n in n_values]
    Bn_over_sqrt_n = [np.mean(results_dict[n]) / np.sqrt(n) for n in n_values]

    plt.figure(figsize=(20, 10))

    plt.subplot(2, 1, 1)
    plt.plot(n_values, Bn_over_n, label=f'{variable_name}(n)/n', color='blue', marker='o')
    plt.xlabel('n')
    plt.ylabel(f'{variable_name}(n)/n')
    plt.title(f'{variable_name}(n)/n jako funkcja n')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(n_values, Bn_over_sqrt_n, label=f'{variable_name}(n)/sqrt(n)', color='green', marker='o')
    plt.xlabel('n')
    plt.ylabel(f'{variable_name}(n)/sqrt(n)')
    plt.title(f'{variable_name}(n)/sqrt(n) jako funkcja n')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    if output_filename:
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        plt.savefig(output_filename, format='png')
        print(f'Wykres zapisano do pliku {output_filename}')


def plot_and_save_extra_Un_results(results_dict, variable_name, output_filename=None):
    """
    Rysuje wykres u(n)/n jako funkcji n na podstawie wyników zapisanych w pliku JSON.
    """
    n_values = sorted(results_dict.keys())

    Un_over_n = [np.mean(results_dict[n]) / n for n in n_values]

    plt.figure(figsize=(20, 10))

    plt.plot(n_values, Un_over_n, label=f'{variable_name}(n)/n', color='purple', marker='o')
    plt.xlabel('n')
    plt.ylabel(f'{variable_name}(n)/n')
    plt.title(f'{variable_name}(n)/n jako funkcja n')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    if output_filename:
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        plt.savefig(output_filename, format='png')
        print(f'Wykres zapisano do pliku {output_filename}')


def plot_and_save_extra_Cn_results(results_dict, variable_name, output_filename=None):
    """
    Rysuje wykres c(n)/n, c(n)/(n ln n) oraz c(n)/n^2 jako funkcji n na podstawie wyników zapisanych w pliku JSON.
    """
    n_values = sorted(results_dict.keys())

    Cn_over_n = [np.mean(results_dict[n]) / n for n in n_values]
    Cn_over_n_ln_n = [np.mean(results_dict[n]) / (n * np.log(n)) for n in n_values]
    Cn_over_n_squared = [np.mean(results_dict[n]) / (n ** 2) for n in n_values]

    plt.figure(figsize=(20, 15))

    plt.subplot(3, 1, 1)
    plt.plot(n_values, Cn_over_n, label=f'{variable_name}(n)/n', color='blue', marker='o')
    plt.xlabel('n')
    plt.ylabel(f'{variable_name}(n)/n')
    plt.title(f'{variable_name}(n)/n jako funkcja n')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(n_values, Cn_over_n_ln_n, label=f'{variable_name}(n)/(n ln n)', color='green', marker='o')
    plt.xlabel('n')
    plt.ylabel(f'{variable_name}(n)/(n ln n)')
    plt.title(f'{variable_name}(n)/(n ln n) jako funkcja n')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(n_values, Cn_over_n_squared, label=f'{variable_name}(n)/n^2', color='red', marker='o')
    plt.xlabel('n')
    plt.ylabel(f'{variable_name}(n)/n^2')
    plt.title(f'{variable_name}(n)/n^2 jako funkcja n')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    if output_filename:
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        plt.savefig(output_filename, format='png')
        print(f'Wykres zapisano do pliku {output_filename}')


def plot_and_save_extra_Dn_results(results_dict, variable_name, output_filename=None):
    """
    Rysuje wykres d(n)/n, d(n)/(n ln n) oraz d(n)/n^2 jako funkcji n na podstawie wyników zapisanych w pliku JSON.
    """
    n_values = sorted(results_dict.keys())

    Dn_over_n = [np.mean(results_dict[n]) / n for n in n_values]
    Dn_over_n_ln_n = [np.mean(results_dict[n]) / (n * np.log(n)) for n in n_values]
    Dn_over_n_squared = [np.mean(results_dict[n]) / (n ** 2) for n in n_values]

    plt.figure(figsize=(20, 15))

    plt.subplot(3, 1, 1)
    plt.plot(n_values, Dn_over_n, label=f'{variable_name}(n)/n', color='blue', marker='o')
    plt.xlabel('n')
    plt.ylabel(f'{variable_name}(n)/n')
    plt.title(f'{variable_name}(n)/n jako funkcja n')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(n_values, Dn_over_n_ln_n, label=f'{variable_name}(n)/(n ln n)', color='green', marker='o')
    plt.xlabel('n')
    plt.ylabel(f'{variable_name}(n)/(n ln n)')
    plt.title(f'{variable_name}(n)/(n ln n) jako funkcja n')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(n_values, Dn_over_n_squared, label=f'{variable_name}(n)/n^2', color='red', marker='o')
    plt.xlabel('n')
    plt.ylabel(f'{variable_name}(n)/n^2')
    plt.title(f'{variable_name}(n)/n^2 jako funkcja n')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    if output_filename:
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        plt.savefig(output_filename, format='png')
        print(f'Wykres zapisano do pliku {output_filename}')


def plot_and_save_extra_Dn_Cn_results(results_dict_D, results_dict_C, variable_name, output_filename=None):
    """
    Rysuje wykres (d(n) - c(n))/n, (d(n) - c(n))/(n ln n) oraz (d(n) - c(n))/(n ln ln n) jako funkcji n na podstawie wyników zapisanych w pliku JSON.
    """
    n_values = sorted(results_dict_D.keys())

    Dn_minus_Cn_over_n = [(np.mean(results_dict_D[n]) - np.mean(results_dict_C[n])) / n for n in n_values]
    Dn_minus_Cn_over_n_ln_n = [(np.mean(results_dict_D[n]) - np.mean(results_dict_C[n])) / (n * np.log(n)) for n in n_values]
    Dn_minus_Cn_over_n_ln_ln_n = [(np.mean(results_dict_D[n]) - np.mean(results_dict_C[n])) / (n * np.log(np.log(n))) for n in n_values]

    plt.figure(figsize=(20, 15))

    plt.subplot(3, 1, 1)
    plt.plot(n_values, Dn_minus_Cn_over_n, label=f'({variable_name}_D(n) - {variable_name}_C(n))/n', color='blue', marker='o')
    plt.xlabel('n')
    plt.ylabel(f'({variable_name}_D(n) - {variable_name}_C(n))/n')
    plt.title(f'({variable_name}_D(n) - {variable_name}_C(n))/n jako funkcja n')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(n_values, Dn_minus_Cn_over_n_ln_n, label=f'({variable_name}_D(n) - {variable_name}_C(n))/(n ln n)', color='green', marker='o')
    plt.xlabel('n')
    plt.ylabel(f'({variable_name}_D(n) - {variable_name}_C(n))/(n ln n)')
    plt.title(f'({variable_name}_D(n) - {variable_name}_C(n))/(n ln n) jako funkcja n')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(n_values, Dn_minus_Cn_over_n_ln_ln_n, label=f'({variable_name}_D(n) - {variable_name}_C(n))/(n ln ln n)', color='red', marker='o')
    plt.xlabel('n')
    plt.ylabel(f'({variable_name}_D(n) - {variable_name}_C(n))/(n ln ln n)')
    plt.title(f'({variable_name}_D(n) - {variable_name}_C(n))/(n ln ln n) jako funkcja n')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    if output_filename:
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        plt.savefig(output_filename, format='png')
        print(f'Wykres zapisano do pliku {output_filename}')


def load_results_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def write_raw_results_to_json(results, filename):
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)
