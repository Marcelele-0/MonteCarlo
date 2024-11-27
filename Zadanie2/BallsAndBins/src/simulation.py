import logging
import hydra
from multiprocessing import Pool
from utils.simulate_throws import simulate_throws
from utils.handle_results import write_raw_results_to_json


@hydra.main(version_base=None, config_path="../config", config_name="throwing_config.yaml")
def main(cfg):
    logging.getLogger().setLevel(logging.DEBUG)

    logging.info("Starting the simulation")
    max_number_of_bins = cfg.max_number_of_bins
    step_size = cfg.step_size

    bin_count_range = list(range(1000, max_number_of_bins + step_size, step_size))

    k_runs = cfg.independent_runs

    results_directory = cfg.result_file_path

    results = []

    def run_simulations(num_bins):
        with Pool() as pool:
            results = pool.map(simulate_throws, [num_bins] * k_runs)
        return results

    for n in bin_count_range:
        logging.debug(f"Simulating for {n} bins")

        all_results_for_n = run_simulations(n)

        # Konwertowanie wartości int32 na zwykły int
        Bn_values = [int(result['Bn']) for result in all_results_for_n]
        Cn_values = [int(result['Cn']) for result in all_results_for_n]
        Dn_values = [int(result['Dn']) for result in all_results_for_n]
        Un_values = [int(result['Un']) for result in all_results_for_n]
        Dn_minus_Cn_values = [int(result['Dn - Cn']) for result in all_results_for_n]

        # Zbieramy wszystkie wyniki dla danego n w jednym słowniku
        results.append({
            'n': n,
            'Bn': Bn_values,
            'Cn': Cn_values,
            'Dn': Dn_values,
            'Un': Un_values,
            'Dn - Cn': Dn_minus_Cn_values
        })
    
        write_raw_results_to_json(results, results_directory)

if __name__ == "__main__":
    main()
