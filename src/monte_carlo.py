import hydra
from omegaconf import DictConfig
import numpy as np
from utils.calculate_M import calculate_M
from utils.calculate_C import calculate_C_list
from utils.approximate_integral import approximate_integral
from utils.manage_results import visualize_results

@hydra.main(version_base=None, config_path="../configs", config_name="monte_carlo_config.yaml")
def main(cfg: DictConfig):
    for function in cfg.monte_carlo_config.functions:
        try:
            n_max = cfg.monte_carlo_config.n_max
            n_step = cfg.monte_carlo_config.n_step
            n_values = list(range(n_step, n_max + 1, n_step))
            k1, k2 = cfg.monte_carlo_config.k_1, cfg.monte_carlo_config.k_2
            save_path = "results/monte_carlo"

            # Calculate M
            M = calculate_M(function)
            M_numeric = float(M)
            print(f'Calculated M for {function["key"]}: M = {M_numeric}')

            # Dictionaries to store results for both k1 and k2
            integral_results_k1 = {n: [] for n in n_values}
            integral_results_k2 = {n: [] for n in n_values}

            for n in n_values:
                # Calculations for k1
                for _ in range(k1):
                    C_k1 = calculate_C_list(function, M_numeric, 1, [n])[0]
                    approximation_k1 = approximate_integral(float(C_k1), function, M_numeric, n)
                    integral_results_k1[n].append(float(approximation_k1))

                # Calculations for k2
                for _ in range(k2):
                    C_k2 = calculate_C_list(function, M_numeric, 1, [n])[0]
                    approximation_k2 = approximate_integral(float(C_k2), function, M_numeric, n)
                    integral_results_k2[n].append(float(approximation_k2))

            # Mean values for both k1 and k2
            integral_mean_k1 = {n: float(np.mean(integral_results_k1[n])) for n in n_values}
            integral_mean_k2 = {n: float(np.mean(integral_results_k2[n])) for n in n_values}

            # Call visualize_results with results for both k1 and k2
            visualize_results(integral_results_k1, integral_mean_k1, integral_results_k2, integral_mean_k2, function, save_path, k1, k2)

        except Exception as e:
            print(f"Error calculating for {function['key']}: {e}")

if __name__ == "__main__":
    main()
