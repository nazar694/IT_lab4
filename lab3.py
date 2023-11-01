from __future__ import annotations

import numpy as np


def transport_min_cost(supply, demand, costs):
    num_suppliers = len(supply)
    num_demanders = len(demand)

    result = np.zeros((num_suppliers, num_demanders))

    while np.sum(supply) > 0 and np.sum(demand) > 0:
        min_cost = np.inf
        min_i, min_j = -1, -1

        for i in range(num_suppliers):
            for j in range(num_demanders):
                if supply[i] > 0 and demand[j] > 0 and costs[i, j] < min_cost:
                    min_cost = costs[i, j]
                    min_i, min_j = i, j
        amount = min(supply[min_i], demand[min_j])
        result[min_i, min_j] = amount
        supply[min_i] -= amount
        demand[min_j] -= amount

    return result


if __name__ == "__main__":
    supply = np.array([10, 20, 30])
    demand = np.array([16, 12, 11, 10])
    costs = np.array([[17, 16, 15, 14],
                      [12, 13, 11, 12],
                      [15, 18, 19, 17]])

    routes = transport_min_cost(supply, demand, costs)

    print("Matrix : ")
    for route in routes:
        print(route)
    print()
    total = np.sum(routes * costs)
    print("Cost : ", total)

    n = input()
