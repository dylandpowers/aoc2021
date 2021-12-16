import numpy


def get_risk_level_sum(lava):
    risk_level_sum = 0
    for i in range(len(lava)):
        for j in range(len(lava[i])):
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            surrounding = [(x, y) for (x, y) in neighbors
                           if 0 <= x < len(lava) and 0 <= y < len(lava[i])]
            if all([lava[i][j] < lava[x][y] for (x, y) in surrounding]):
                risk_level_sum += 1 + lava[i][j]
    return risk_level_sum


def three_largest_basins(lava):
    basin_sizes = []
    for i in range(len(lava)):
        for j in range(len(lava[i])):
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            surrounding = [(x, y) for (x, y) in neighbors
                           if 0 <= x < len(lava) and 0 <= y < len(lava[i])]
            if all([lava[i][j] < lava[x][y] for (x, y) in surrounding]):
                # when you find a low point, venture outward marking everything that is part of
                # basin
                basin_sizes.append(dfs_basin(lava, i, j, set()))

    sorted_sizes = sorted(basin_sizes)
    return numpy.prod(sorted_sizes[-3:])


def dfs_basin(lava, x, y, visited):
    if x < 0 or x >= len(lava) or y < 0 or y >= len(lava[0]) or (x, y) in visited or lava[x][y] == 9:
        return 0
    visited.add((x, y))
    return 1 + dfs_basin(lava, x - 1, y, visited) + dfs_basin(lava, x + 1, y, visited) + dfs_basin(lava, x, y - 1, visited) + dfs_basin(lava, x, y + 1, visited)


if __name__ == '__main__':
    data = []
    with open('inputs/day9.txt') as f:
        for line in f.readlines():
            data.append([int(c) for c in line.strip()])
    print(get_risk_level_sum(data))
    print(three_largest_basins(data))