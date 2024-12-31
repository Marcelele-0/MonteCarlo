# Symulacja Modelu Komunikacji z Zakłóceniami

## Opis

Projekt symuluje uproszczony model komunikacji w sieci o topologii gwiazdy, składającej się z \( n+1 \) węzłów. Centralna stacja (węzeł 0) rozsyła informację do wszystkich pozostałych węzłów. Każdy węzeł odbiera wiadomość z prawdopodobieństwem \( p \). Symulacja ma na celu zbadanie minimalnej liczby rund \( T_n \) potrzebnej do rozesłania informacji do wszystkich węzłów dla różnych wartości \( n \) i \( p \).

## Struktura Projektu

```
MonteCarlo/
├── config/
│   └── config.yaml          # Plik konfiguracyjny Hydra
├── logs/                    # Katalog na logi
├── src/
│   ├── simulation.py        # Logika symulacji
│   ├── experiments.py       # Uruchamianie eksperymentów
│   └── plotting.py          # Generowanie wykresów
├── main.py                  # Główny skrypt uruchamiający symulację
└── environment.yml          # Plik konfiguracyjny Conda
```

## Instalacja

1. Utwórz środowisko Conda:
   ```sh
   conda env create -f environment.yml
   conda activate MonteCarlo
   ```

2. Zainstaluj wymagane pakiety:
   ```sh
   pip install -r requirements.txt
   ```

## Uruchomienie Symulacji

1. Uruchom główny skrypt:
   ```sh
   python main.py
   ```

2. Skrypt uruchomi symulację dla różnych wartości \( n \) i \( p \), a następnie wygeneruje wykresy przedstawiające wyniki.

## Konfiguracja

Plik `config/config.yaml` zawiera parametry symulacji:
- `start_n`: początkowa wartość \( n \)
- `max_n`: maksymalna wartość \( n \)
- `step_n`: krok zwiększania wartości \( n \)
- `k`: liczba niezależnych powtórzeń dla każdej wartości \( n \)
- `p_values`: lista wartości prawdopodobieństwa \( p \)

Przykład konfiguracji:
```yaml
simulation:
  start_n: 100
  max_n: 10000
  step_n: 100
  k: 50
  p_values: [0.5, 0.1]
```

## Logowanie

Skrypt wykorzystuje moduł `logging` do logowania postępu symulacji.
## Wykresy

Wyniki symulacji są przedstawiane na wykresach, które pokazują średnią liczbę rund \( T_n \) potrzebną do rozesłania informacji do wszystkich węzłów dla różnych wartości \( n \) i \( p \).

```
```