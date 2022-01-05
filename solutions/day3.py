import copy
from collections import Counter


def get_power_consumption():
    with open('../inputs/day3.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    gamma, epsilon = '', ''
    for i in range(len(lines[0])):
        occ = Counter([line[i] for line in lines])
        most_common = occ.most_common()[0][0]
        gamma += most_common
        epsilon += ('1' if most_common == '0' else '0')

    return int(gamma, 2) * int(epsilon, 2)


def get_life_support_rating():
    with open('../inputs/day3.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    o_candidates, c_candidates = copy.deepcopy(lines), copy.deepcopy(lines)
    o, c = '', ''
    for i in range(len(lines[0])):
        if len(o_candidates) > 1:
            o_occ = Counter([line[i] for line in o_candidates]).most_common()
            most_common = o_occ[0][0] if o_occ[0][1] > o_occ[1][1] else '1'
            o_candidates = list(filter(lambda line: line[i] == most_common, o_candidates))
        if len(o_candidates) == 1:
            o = o_candidates[0]

        if len(c_candidates) > 1:
            c_occ = Counter([line[i] for line in c_candidates]).most_common()
            least_common = c_occ[1][0] if c_occ[0][1] > c_occ[1][1] else '0'
            c_candidates = list(filter(lambda line: line[i] == least_common, c_candidates))
        if len(c_candidates) == 1:
            c = c_candidates[0]

        if o and c:
            return int(o, 2) * int(c, 2)

    return None
