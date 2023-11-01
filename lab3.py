import numpy as np


def transport_min_cost(supply, demand, costs):
    num_suppliers = len(supply)  # кількість постачальників
    num_demanders = len(demand)  # кількість споживачів

    result = np.zeros((num_suppliers, num_demanders))

    # Цикл з еревіркою, чи виконані потреби у постачальників та споживачів
    while np.sum(supply) > 0 and np.sum(demand) > 0:
        min_cost = np.inf
        min_i, min_j = -1, -1

        # Перебираємо всі комбінації постачальників та споживачів
        for i in range(num_suppliers):
            for j in range(num_demanders):
                # Перевірка чи у постачальника ще є товари і у споживача чи є потреби в товарі і найменшу вартість
                if supply[i] > 0 and demand[j] > 0 and costs[i, j] < min_cost:
                    # Оновлюємо найменшу вартість та зберігаємо індекси
                    min_cost = costs[i, j]
                    min_i, min_j = i, j
        # Знаходимо кількість товарів для переміщення
        amount = min(supply[min_i], demand[min_j])
        result[min_i, min_j] = amount
        # Оновлюємо запаси постачальника та потреби споживача
        supply[min_i] -= amount
        demand[min_j] -= amount

    return result


if __name__ == "__main__":
    # Ввід початкових даних
    supply = np.array([10, 20, 30])  # Постачальники
    demand = np.array([16, 12, 11, 10])  # Споживачі
    costs = np.array([[17, 16, 15, 14],
                      [12, 13, 11, 12],
                      [15, 18, 19, 17]])  # Вартість перевезення

    routes = transport_min_cost(supply, demand, costs)

    # Вивід результату
    print("Матриця розподілу постачання товарів : ")
    for route in routes:
        print(route)
    print()
    # Вартість доставки
    total = np.sum(routes * costs)
    print("Вартість : ", total)

    n = input()
