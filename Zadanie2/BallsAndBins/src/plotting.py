from utils.handle_results import *
import hydra


@hydra.main(version_base=None, config_path="../config", config_name="throwing_config.yaml")
def main(cfg):
    results_file = cfg.result_file_path

    results = load_results_from_json(results_file)

    Bn_results = {}
    Cn_results = {}
    Dn_results = {}
    Un_results = {}
    Dn_minus_Cn_results = {}

    for result in results:
        n = result['n']
        Bn_results[n] = result['Bn']
        Cn_results[n] = result['Cn']
        Dn_results[n] = result['Dn']
        Un_results[n] = result['Un']
        Dn_minus_Cn_results[n] = result['Dn - Cn']

    plot_and_save_results(Bn_results, 'Bn', 'results/plot/Bn.png')
    plot_and_save_results(Cn_results, 'Cn', 'results/plot/Cn.png')
    plot_and_save_results(Dn_results, 'Dn', 'results/plot/Dn.png')
    plot_and_save_results(Un_results, 'Un', 'results/plot/Un.png')
    plot_and_save_results(Dn_minus_Cn_results, 'Dn - Cn', 'results/plot/Dn_minus_Cn.png')
    plot_and_save_extra_Bn_results(Bn_results, 'Bn', 'results/plot/Bn_extra.png')
    plot_and_save_extra_Cn_results(Cn_results, 'Cn', 'results/plot/Cn_extra.png')
    plot_and_save_extra_Dn_results(Dn_results, 'Dn', 'results/plot/Dn_extra.png')
    plot_and_save_extra_Un_results(Un_results, 'Un', 'results/plot/Un_extra.png')
    plot_and_save_extra_Dn_Cn_results(Dn_results, Cn_results, 'Dn - Cn', 'results/plot/Dn_minus_Cn_extra.png')



if __name__ == "__main__":
    main()