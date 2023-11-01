from lab3 import transport_min_cost

import numpy as np


def test_correct(self):
    # Ввід початкових даних
    supply = np.array([10, 20, 30])  # Постачальники
    demand = np.array([16, 12, 11, 10])  # Споживачі
    costs = np.array([[17, 16, 15, 14],
                      [12, 13, 11, 12],
                      [15, 18, 19, 17]])  # Вартість перевезення
    routes = transport_min_cost(supply, demand, costs)
    # Вартість доставки
    total = np.sum(routes * costs)
    assert total == 690


def test_failed(self):
    # Ввід початкових даних
    supply = np.array([15, 25, 35])  # Постачальники
    demand = np.array([16, 12, 11, 10])  # Споживачі
    costs = np.array([[17, 16, 15, 14],
                      [12, 13, 11, 12],
                      [15, 18, 19, 17]])  # Вартість перевезення
    routes = transport_min_cost(supply, demand, costs)
    # Вартість доставки
    total = np.sum(routes * costs)
    assert total == 690


