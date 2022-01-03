def highest_y_position(x_range, y_range):
    min_x, max_x = x_range
    min_y, max_y = y_range

    """
    Maximum x velocity is max_x since we can only fire to the right
    Minimum x velocity is 1 (is it? I think there is a formula for this)
    Minimum y velocity is min_y
    Maximum y velocity is abs(min_y)
    """
    max_y = 0
    for vx in range(1, max_x + 1):
        for vy in range(min_y, abs(min_y) + 1):
            result = try_launch(vx, vy, x_range, y_range)
            max_y = max(result, max_y)

    return max_y


def num_valid_velocities(x_range, y_range):
    min_x, max_x = x_range
    min_y, max_y = y_range

    """
    Maximum x velocity is max_x since we can only fire to the right
    Minimum x velocity is 1 (is it? I think there is a formula for this)
    Minimum y velocity is min_y
    Maximum y velocity is abs(min_y)
    """
    valid_velocities = 0
    for vx in range(1, max_x + 1):
        for vy in range(min_y, abs(min_y) + 1):
            result = try_launch(vx, vy, x_range, y_range)
            valid_velocities += result >= 0
    return valid_velocities


def try_launch(vx, vy, x_range, y_range):
    min_x, max_x = x_range
    min_y, max_y = y_range
    x = y = 0
    highest_y = 0

    while True:
        x += vx
        y += vy
        highest_y = max(y, highest_y)

        if min_x <= x <= max_x and min_y <= y <= max_y:
            return highest_y

        if (x > max_x or vx == 0) and y < min_y:
            return -1

        vx -= (vx > 0) - (vx < 0)
        vy -= 1


def main():
    with open('inputs/day17.txt') as f:
        line = f.readline().strip()
        x_start, x_end = line.index('x=') + 2, line.index(',')
        min_x = int(line[x_start:line.index('.', x_start)])
        max_x = int(line[line.index('..') + 2:x_end])

        y_start = line.index('y=') + 2
        min_y = int(line[y_start:line.index('.', y_start)])
        max_y = int(line[line.index('..', y_start) + 2:])

    print(highest_y_position((min_x, max_x), (min_y, max_y)))
    print(num_valid_velocities((min_x, max_x), (min_y, max_y)))


if __name__ == '__main__':
    main()
