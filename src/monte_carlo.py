import logging
import hydra
from omegaconf import DictConfig
import numpy as np
from utils.calculate_M import calculate_M
from utils.calculate_C import calculate_C_parallel, get_numeric_function
from utils.approximate_integral import approximate_integral, approximate_pi
from utils.manage_results import visualize_results, visualize_results_Pi

# Set up logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

@hydra.main(version_base=None, config_path="../configs", config_name="monte_carlo_config.yaml")
def main(cfg: DictConfig):
    # Ensure Hydra does not override the logging configuration
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info("Starting Monte Carlo simulation...")

    for function in cfg.monte_carlo_config.functions:
        if function["key"] == "Pi":
            logging.debug("Calculating for Pi function")
            try:
                n_max = cfg.monte_carlo_config.n_max
                n_step = cfg.monte_carlo_config.n_step
                n_values = list(range(n_step, n_max + 1, n_step))
                # Dictionaries to store results for both k1 and k2
                integral_results_k1 = {n: [] for n in n_values}
                integral_results_k2 = {n: [] for n in n_values}
                save_path = "results/monte_carlo"
                integral_mean_k1 = {}
                integral_mean_k2 = {}

                k1, k2 = cfg.monte_carlo_config.k_1, cfg.monte_carlo_config.k_2

                for n in n_values:
                    logging.debug(f"Calculating n = {n}")
                    for _ in range(k1):
                        approx = approximate_pi(n)
                        integral_results_k1[n].append(approx)
                    
                    for _ in range(k2):
                        approx = approximate_pi(n)
                        integral_results_k2[n].append(approx)

                # Calculate mean values
                for n in n_values:
                    integral_mean_k1[n] = np.mean(integral_results_k1[n])
                    integral_mean_k2[n] = np.mean(integral_results_k2[n])


                # Temporarily set logging level to WARNING to suppress logging
                previous_logging_level = logging.getLogger().getEffectiveLevel()
                logging.getLogger().setLevel(logging.WARNING)

                # Visualize results
                visualize_results_Pi(
                    integral_results_k1,
                    integral_mean_k1,
                    integral_results_k2,
                    integral_mean_k2,
                    save_path=save_path,  
                    function=function,
                    k1=k1,
                    k2=k2
                )

                # Restore previous logging level
                logging.getLogger().setLevel(previous_logging_level)


            except Exception as e:
                logging.critical(f"Error calculating for {function['key']}: {e}")

        else:
            try:
                function_config = function
                # Przygotowanie funkcji numerycznej i obliczenie stałej M
                numeric_function = get_numeric_function(function_config['fn'])
                M = calculate_M(function_config)
                a, b = function_config['a'], function_config['b']

                # Słowniki do przechowywania wyników
                integral_results_k1 = {n: [] for n in n_values}
                integral_results_k2 = {n: [] for n in n_values}
                integral_mean_k1 = {}
                integral_mean_k2 = {}

                # Obliczanie dla każdego n i dla obu wartości k
                for n in n_values:
                    logging.info(f"Obliczenia dla n = {n}")

                    # Obliczenia dla k1
                    integral_results_k1[n] = calculate_C_parallel(n, numeric_function, M, a, b, k1)
                    integral_mean_k1[n] = np.mean(integral_results_k1[n])

                    # Obliczenia dla k2
                    integral_results_k2[n] = calculate_C_parallel(n, numeric_function, M, a, b, k2)
                    integral_mean_k2[n] = np.mean(integral_results_k2[n])

                # Wizualizacja wyników
                visualize_results(
                    integral_results_k1, integral_mean_k1,
                    integral_results_k2, integral_mean_k2,
                    save_path=save_path, function=function_config,
                    k1=k1, k2=k2
                )
            except Exception as e:
                logging.critical(f"Error calculating for {function['key']}: {e}")

if __name__ == "__main__":
    main()
