import logging
import hydra
from multiprocessing import Pool
from utils.simulate_throws import simulate_throws, simulate_maximum_load
from utils.handle_results import write_raw_results_to_json


@hydra.main(version_base=None, config_path="../config", config_name="throwing_config.yaml")
def main(cfg):
    logging.getLogger().setLevel(logging.DEBUG)

    logging.info("Starting the simulation")
    max_number_of_bins = cfg.max_number_of_bins
    step_size = cfg.step_size

    bin_count_range = list(range(1000, max_number_of_bins + step_size, step_size))

    k_runs = cfg.independent_runs
    standard_simulation = cfg.standard_simulation  # do we want to run the standard simulation?
    maximum_load_simulation = cfg.maximum_load_simulation  # do we want to run the maximum load simulation?

    results_directory = cfg.result_file_path

    standard_results = []
    maximum_load_results = []

    def run_simulations(num_bins):
        with Pool() as pool:
            results = pool.map(simulate_throws, [num_bins] * k_runs)
        return results

    def run_maximum_load_simulations(num_bins, d):
        with Pool() as pool:
            results = pool.starmap(simulate_maximum_load, [(num_bins, d)] * k_runs)
        return results

    for n in bin_count_range:
        logging.debug(f"Simulating for {n} bins")

        if standard_simulation:
            all_results_for_n = run_simulations(n)
            Bn_values = [int(result['Bn']) for result in all_results_for_n]
            Cn_values = [int(result['Cn']) for result in all_results_for_n]
            Dn_values = [int(result['Dn']) for result in all_results_for_n]
            Un_values = [int(result['Un']) for result in all_results_for_n]
            Dn_minus_Cn_values = [int(result['Dn - Cn']) for result in all_results_for_n]

            standard_results.append({
                'n': n,
                'Bn': Bn_values,
                'Cn': Cn_values,
                'Dn': Dn_values,
                'Un': Un_values,
                'Dn - Cn': Dn_minus_Cn_values
            })

        if maximum_load_simulation:
            max_load_results_d1 = run_maximum_load_simulations(n, 1)
            max_load_results_d2 = run_maximum_load_simulations(n, 2)
            max_load_d1_values = [int(result) for result in max_load_results_d1]
            max_load_d2_values = [int(result) for result in max_load_results_d2]

            maximum_load_results.append({
                'n': n,
                'max_load_d1': max_load_d1_values,
                'max_load_d2': max_load_d2_values
            })

    if standard_simulation:
        write_raw_results_to_json(standard_results, f"{results_directory}/standard_results.json")
    
    if maximum_load_simulation:
        write_raw_results_to_json(maximum_load_results, f"{results_directory}/maximum_load_results.json")

if __name__ == "__main__":
    main()
