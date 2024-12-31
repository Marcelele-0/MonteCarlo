import hydra
from omegaconf import DictConfig
from src.experiments import run_experiments
from src.plotting import plot_results
import logging

@hydra.main(config_path="config", config_name="config")
def main(cfg: DictConfig):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    start_n = cfg.simulation.start_n
    max_n = cfg.simulation.max_n
    step_n = cfg.simulation.step_n
    n_values = range(start_n, max_n + 1, step_n)
    k = cfg.simulation.k
    output_dir = "plots"

    for p in cfg.simulation.p_values:
        logger.info(f"Running experiments for p = {p}")
        all_results = run_experiments(n_values, p, k, logger)
        plot_results(n_values, all_results, p, output_dir)

if __name__ == "__main__":
    main()
