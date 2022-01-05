UNIQUE_LENGTHS = {2, 4, 3, 7}
LENGTH_TO_DIGIT = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}


def get_unique_output_segments():
    patterns_to_output = {}
    with open('../inputs/day8.txt') as f:
        for line in f.readlines():
            patterns = tuple([p.strip() for p in line[:line.index('|') - 1].split(' ')])
            output = [s.strip() for s in line[line.index('|') + 2:].split(' ')]
            patterns_to_output[patterns] = output

    num_unique_signals = 0
    for arr in list(patterns_to_output.values()):
        num_unique_signals += len(list(filter(lambda o: len(o) in UNIQUE_LENGTHS, arr)))

    return num_unique_signals


def find_by_segment_count(patterns, count):
    return list(filter(lambda pattern: len(pattern) == count, patterns))


def find_one(patterns):
    return find_by_segment_count(patterns, 2)[0]


def find_four(patterns):
    return find_by_segment_count(patterns, 4)[0]


def find_seven(patterns):
    return find_by_segment_count(patterns, 3)[0]


def find_eight(patterns):
    return find_by_segment_count(patterns, 7)[0]


# Shoutout to https://github.com/Farbfetzen/Advent_of_Code/blob/main/python/2021/day08.py
# for the help here :)
def sum_output_values():
    data = []
    with open('../inputs/day8.txt') as f:
        for line in f.readlines():
            patterns = [frozenset(p.strip()) for p in line[:line.index('|') - 1].split(' ')]
            output = [frozenset(s.strip()) for s in line[line.index('|') + 2:].split(' ')]
            data.append((patterns, output))

    output_sum = 0
    for patterns, output in data:
        # 6 segments: 0, 6, 9
        # 5 segments: 2, 3, 5
        # 2, 5, and 6 must not contain both segments of 1
        # 0, 2, 3, 5, 6 must all be disjoint from 4
        # 2, 5, 6 must all be disjoint from 7
        # Can't infer anything from 8
        candidates = [[] for _ in range(10)]
        for pattern in patterns:
            for digit in LENGTH_TO_DIGIT[len(pattern)]:
                candidates[digit].append(pattern)

        one = candidates[1][0]
        four = candidates[4][0]

        # 2, 5, and 6 must not share both segments of 1
        # after this we will have found 6 due to its unique number of segments here
        for i in (2, 5, 6):
            candidates[i] = [c for c in candidates[i] if not one.issubset(c)]

        # 3 and 1 must share 2
        candidates[3] = [c for c in candidates[3] if len(c.intersection(one)) == 2]

        # 5 and 4 must have intersection length 3
        candidates[5] = [c for c in candidates[5] if len(c.intersection(four)) == 3]

        # 2 and 4 must have intersection length 2
        candidates[2] = [c for c in candidates[2] if len(c.intersection(four)) == 2]

        # 1 and 3 must have intersection length 2
        candidates[1] = [c for c in candidates[1] if len(c.intersection(one)) == 2]

        # 9 and 4 must have intersection length 4
        candidates[9] = [c for c in candidates[9] if len(c.intersection(four)) == 4]

        # 0 should share 2 with 1 and 3 with 4
        candidates[0] = [c for c in candidates[0] if len(c.intersection(one)) == 2
                         and len(c.intersection(four)) == 3]

        mappings = {c[0]: i for i, c in enumerate(candidates)}

        output_str = ''.join([str(mappings[o]) for o in output])
        output_sum += int(output_str)

    return output_sum


if __name__ == '__main__':
    print(get_unique_output_segments())
    print(sum_output_values())


