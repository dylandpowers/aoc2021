def get_minimum_fuel():
    with open('../inputs/day7.txt') as f:
        positions = [int(x.strip()) for x in f.readline().split(',')]
    return min([sum(abs(x - i) for x in positions) for i in range(max(positions))])


def get_minimum_fuel_two():
    with open('../inputs/day7.txt') as f:
        positions = [int(x.strip()) for x in f.readline().split(',')]

    distances = {0: 0}
    for i in range(1, max(positions) - min(positions) + 1):
        distances[i] = distances[i - 1] + i

    return min([sum(distances[abs(x - i)] for x in positions) for i in range(max(positions))])


if __name__ == '__main__':
    print(get_minimum_fuel())
    print(get_minimum_fuel_two())
