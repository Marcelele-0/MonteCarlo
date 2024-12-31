import hydra
from omegaconf import DictConfig
import matplotlib.pyplot as plt
import json
import logging
from multiprocessing import Pool
from src.insertion_sort import insertion_sort
from src.generate_data import generate_random_permutation
from src.stats import save_statistics

log = logging.getLogger(__name__)

def run_single_experiment(n):
    A = generate_random_permutation(n)
    comparisons, swaps = insertion_sort(A)
    return {"n": n, "comparisons": comparisons, "swaps": swaps}

@hydra.main(config_path="conf", config_name="config")
def run_experiments(cfg: DictConfig):
    results = []
    ns = range(cfg.experiment.start, cfg.experiment.end + 1, cfg.experiment.step)
    total_tasks = len(ns) * cfg.experiment.repetitions

    with Pool() as pool:
        for i, result in enumerate(pool.imap_unordered(run_single_experiment, [n for n in ns for _ in range(cfg.experiment.repetitions)])):
            results.append(result)
            if (i + 1) % 10 == 0 or (i + 1) == total_tasks:
                log.info(f"Progress: {i + 1}/{total_tasks} tasks completed")

    save_statistics(cfg.experiment.output_file, results)
    plot_results(cfg.experiment.output_file)

def plot_results(filename):
    with open(filename, mode='r') as file:
        data = json.load(file)

    grouped_data = {}
    for entry in data:
        n = entry["n"]
        comparisons = entry["comparisons"]
        swaps = entry["swaps"]
        if n not in grouped_data:
            grouped_data[n] = {"comparisons": [], "swaps": []}
        grouped_data[n]["comparisons"].append(comparisons)
        grouped_data[n]["swaps"].append(swaps)

    ns = sorted(grouped_data.keys())
    avg_comparisons = [sum(grouped_data[n]["comparisons"]) / len(grouped_data[n]["comparisons"]) for n in ns]
    avg_swaps = [sum(grouped_data[n]["swaps"]) / len(grouped_data[n]["swaps"]) for n in ns]

    # Przygotowanie danych do analiz ilorazowych
    comparisons_n = [c / n for c, n in zip(avg_comparisons, ns)]
    comparisons_n2 = [c / (n ** 2) for c, n in zip(avg_comparisons, ns)]
    swaps_n = [s / n for s, n in zip(avg_swaps, ns)]
    swaps_n2 = [s / (n ** 2) for s, n in zip(avg_swaps, ns)]

    plt.figure(figsize=(16, 12))

    # (a) Liczba porównań i średnia liczba porównań
    plt.subplot(3, 2, 1)
    for n in ns:
        plt.scatter([n] * len(grouped_data[n]["comparisons"]), grouped_data[n]["comparisons"], alpha=0.3)
    plt.plot(ns, avg_comparisons, label="Średnia liczba porównań", color='red')
    plt.xlabel("n")
    plt.ylabel("Liczba porównań")
    plt.title("Liczba porównań i średnia liczba porównań")
    plt.legend()

    # (b) Liczba przestawień i średnia liczba przestawień
    plt.subplot(3, 2, 2)
    for n in ns:
        plt.scatter([n] * len(grouped_data[n]["swaps"]), grouped_data[n]["swaps"], alpha=0.3)
    plt.plot(ns, avg_swaps, label="Średnia liczba przestawień", color='blue')
    plt.xlabel("n")
    plt.ylabel("Liczba przestawień")
    plt.title("Liczba przestawień i średnia liczba przestawień")
    plt.legend()

    # (c) Iloraz cmp(n) / n oraz cmp(n) / n^2
    plt.subplot(3, 2, 3)
    plt.plot(ns, comparisons_n, label="cmp(n)/n", color='green')
    plt.plot(ns, comparisons_n2, label="cmp(n)/n^2", color='o range')
    plt.xlabel("n")
    plt.ylabel("Iloraz")
    plt.title("Iloraz cmp(n)/n oraz cmp(n)/n^2")
    plt.legend()

    # (d) Iloraz s(n) / n oraz s(n) / n^2
    plt.subplot(3, 2, 4)
    plt.plot(ns, swaps_n, label="s(n)/n", color='purple')
    plt.plot(ns, swaps_n2, label="s(n)/n^2", color='brown')
    plt.xlabel("n")
    plt.ylabel("Iloraz")
    plt.title("Iloraz s(n)/n oraz s(n)/n^2")
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_experiments()
