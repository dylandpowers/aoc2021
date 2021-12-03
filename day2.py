def get_final_position():
    with open('inputs/day2.txt') as f:
        commands = [line for line in f.readlines()]

    horizontal, depth = 0, 0
    for command in commands:
        parts = command.split(" ")
        direction, amount = parts[0], int(parts[1])

        if direction == 'forward':
            horizontal += amount
        elif direction == 'up':
            depth -= amount
        else:
            depth += amount

    return horizontal * depth

def get_final_position_with_aim():
    with open('inputs/day2.txt') as f:
        commands = [line for line in f.readlines()]

    horizontal, depth, aim = 0, 0, 0
    for command in commands:
        parts = command.split(" ")
        direction, amount = parts[0], int(parts[1])

        if direction == 'forward':
            horizontal += amount
            depth += amount * aim
        elif direction == 'up':
            aim -= amount
        else:
            aim += amount

    return horizontal * depth