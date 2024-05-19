import heapq
from typing import List


def minimize_cost(cables: List[int]) -> int:
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)
        connection_cost = shortest1 + shortest2
        total_cost += connection_cost
        heapq.heappush(cables, connection_cost)

    return total_cost


if __name__ == "__main__":
    while True:
        try:
            cables = list(map(int, input("Enter the lengths of the cables: ").split()))
            break
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
    print("Cables", cables)
    min_cost = minimize_cost(cables)
    print("Mim costs", min_cost)
