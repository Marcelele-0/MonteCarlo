import numpy as np
import json

def simulate_throws(num_bins):
    """
    Simulate the process of throwing balls into bins and track the following metrics:
    - Bn: the time of the first collision
    - Un: the number of empty bins after n balls are thrown
    - Cn: the minimal number of throws until all bins contain at least one ball
    - Dn: the minimal number of throws until all bins contain at least two balls

    Args:
    num_bins (int): number of bins to place balls in

    Returns:
    dict: A dictionary with calculated Bn, Un, Cn, Dn, and Dn - Cn values
    """
    Bn = Cn = Dn = total_balls_thrown = 0
    urns = np.zeros(num_bins, dtype=int)
    first_collision = False
    all_filled_once = False
    all_filled_twice = False
    Un_calculated = False

    while not all_filled_twice:
        total_balls_thrown += 1
        urn_index = np.random.randint(0, num_bins)
        urns[urn_index] += 1

        # Calculate Un (number of empty bins after n balls are thrown)
        if not Un_calculated and total_balls_thrown == num_bins:
            Un = np.sum(urns == 0)
            Un_calculated = True

        # Check Bn (moment of first collision)
        if not first_collision and urns[urn_index] == 2:
            Bn = total_balls_thrown
            first_collision = True

        # Check Cn (all bins filled at least once)
        if not all_filled_once and np.all(urns > 0):
            Cn = total_balls_thrown
            all_filled_once = True

        # Check Dn (all bins filled at least twice)
        if not all_filled_twice and np.all(urns > 1):
            Dn = total_balls_thrown
            all_filled_twice = True

    return {
        'Bn': Bn,
        'Un': Un,
        'Cn': Cn,
        'Dn': Dn,
        'Dn - Cn': Dn - Cn
    }

def simulate_maximum_load(num_bins, d):
    """
    Simulate the process of throwing balls into bins and track the maximum load of the bins

    Args:
    num_bins (int): number of bins to place balls in
    d (int): number of choices for each ball (1 or 2)

    Returns:
    int: The maximum load of any bin after all balls are thrown
    """
    urns = np.zeros(num_bins, dtype=int)

    for _ in range(num_bins):
        if d == 1:
            urn_index = np.random.randint(0, num_bins)
        elif d == 2:
            urn_indices = np.random.randint(0, num_bins, size=2)
            # np.argmin chooses the first occurrence in case of ties
            urn_index = urn_indices[np.argmin(urns[urn_indices])]
        urns[urn_index] += 1

    return np.max(urns)