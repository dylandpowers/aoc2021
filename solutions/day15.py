import heapq
from copy import deepcopy


def calculate_lowest_risk(risk_levels):
    m, n = len(risk_levels), len(risk_levels[0])
    visited = set()
    heap = []
    costs = {(0, 0): 0}

    # top left has cost 0
    heapq.heappush(heap, (0, (0, 0)))

    while heap:
        dist, (x, y) = heapq.heappop(heap)
        visited.add((x, y))

        for (i, j) in neighbors4(x, y, m, n):
            if (i, j) in visited:
                continue
            cost_to_enter = risk_levels[i][j]

            if (i, j) not in costs or cost_to_enter + dist < costs[(i, j)]:
                costs[(i, j)] = cost_to_enter + dist
                if i == m - 1 and j == n - 1:
                    return cost_to_enter + dist
                heapq.heappush(heap, (cost_to_enter + dist, (i, j)))

    return None


def calculate_lowest_risk_repeated(risk_levels):
    expanded_risk_levels = deepcopy(risk_levels)

    # To the right
    for i in range(len(risk_levels)):
        for j in range(len(risk_levels[0]), len(risk_levels[0]) * 5):
            prev = expanded_risk_levels[i][j - len(risk_levels[0])]
            new_val = 1 if prev == 9 else prev + 1
            expanded_risk_levels[i].append(new_val)

    # Downward
    for i in range(len(risk_levels), len(risk_levels) * 5):
        expanded_risk_levels.append([])
        for j in range(len(risk_levels[0])):
            prev = expanded_risk_levels[i - len(risk_levels)][j]
            new_val = 1 if prev == 9 else prev + 1
            expanded_risk_levels[i].append(new_val)

    # Fill out the rest
    for i in range(len(risk_levels), len(risk_levels) * 5):
        for j in range(len(risk_levels[0]), len(risk_levels[0]) * 5):
            prev = expanded_risk_levels[i - len(risk_levels)][j]
            new_val = 1 if prev == 9 else prev + 1
            expanded_risk_levels[i].append(new_val)

    return calculate_lowest_risk(expanded_risk_levels)


def neighbors4(i, j, m, n):
    candidates = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    return [(x, y) for (x, y) in candidates if 0 <= x < m and 0 <= y < n]


def main():
    with open('../inputs/day15.txt') as f:
        risk_levels = [[int(x) for x in line.strip()] for line in f.readlines()]
    # print(calculate_lowest_risk(risk_levels))
    print(calculate_lowest_risk_repeated(risk_levels))


if __name__ == '__main__':
    main()
