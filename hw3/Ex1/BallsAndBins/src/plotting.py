from utils.handle_results import *
import hydra
import json
import matplotlib.pyplot as plt
from ex3.plot_ln import plot_max_load_results


@hydra.main(version_base=None, config_path="../config", config_name="throwing_config.yaml")
def main(cfg):

    plot_max_load_results(f"{cfg.result_file_path}/maximum_load_results.json")



if __name__ == "__main__":
    main()