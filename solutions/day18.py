import copy


def add_snailfish_numbers(lines):
    curr = lines[0]
    for i in range(1, len(lines)):
        next_number = ['['] + curr + lines[i] + [']']
        # process next_number
        curr = reduce(next_number)

    return magnitude(curr)


def reduce(snailfish_number):
    number = snailfish_number
    while True:
        explode = try_explode(number)
        if explode[1]:
            number = explode[0]
            continue

        split = try_split(number)
        if split[1]:
            number = split[0]
            continue
        break
    return number


def try_explode(snailfish_number):
    next_number = copy.deepcopy(snailfish_number)
    depth = 0
    seen = []
    for i in range(len(next_number)):
        item = next_number[i]
        if item == '[' and depth == 4:
            # Should explode
            first_number = next_number[i + 1]
            second_number = next_number[i + 2]

            # Add first number to the rightmost number in stack
            for j in range(len(seen) - 1, 0, -1):
                seen_item = seen[j]
                if type(seen_item) == int:
                    seen[j] += first_number
                    break

            # Add second number to leftmost number after it
            for j in range(i + 4, len(next_number)):
                next_item = next_number[j]
                if type(next_item) == int:
                    next_number[j] += second_number
                    break

            next_number = seen + [0] + next_number[i + 4:]
            return next_number, True
        else:
            if item == '[':
                depth += 1
            elif item == ']':
                depth -= 1
            seen.append(item)

    return next_number, False


def try_split(snailfish_number):
    next_number = copy.deepcopy(snailfish_number)
    for i in range(len(snailfish_number)):
        item = next_number[i]
        if type(item) == int and item >= 10:
            # Should split the number
            left = item // 2
            right = item - left
            new_pair = ['[', left, right, ']']
            next_number = next_number[:i] + new_pair + next_number[i + 1:]
            return next_number, True

    return next_number, False


def magnitude(snailfish_number):
    number = snailfish_number
    while True:
        for index in range(len(number)):
            if number[index] == '[' and number[index + 3] == ']':
                left = 3 * number[index + 1]
                right = 2 * number[index + 2]
                if len(number) == 4:
                    # Last step
                    return left + right
                number = number[:index] + [left + right] + number[index + 4:]
                break


def convert(raw_number):
    # we will store these numbers in an array so that we can modify them in place
    number = []
    curr = ''
    for c in raw_number:
        if c.isdigit():
            curr += c
        else:
            if curr:
                number.append(int(curr))
                curr = ''
            if c != ',':
                number.append(c)
    return number


def largest_magnitude(lines):
    converted = [convert(line) for line in lines]
    max_magnitude = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j:
                continue
            magnitude_sum = add_snailfish_numbers([converted[i], converted[j]])
            max_magnitude = max(magnitude_sum, max_magnitude)

    return max_magnitude

def main():
    with open('../inputs/day18.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    # print(add_snailfish_numbers(lines))
    print(largest_magnitude(lines))


if __name__ == '__main__':
    main()
