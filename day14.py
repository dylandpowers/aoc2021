from collections import Counter
from copy import deepcopy


def generate_polymer(original, insertion_rules, steps):
    polymer = original
    for _ in range(steps):
        next = ''
        for i in range(len(polymer) - 1):
            sub = polymer[i:i + 2]
            if sub in insertion_rules:
                next += sub[0] + insertion_rules[sub]
            else:
                next += sub[0]
        next += polymer[-1]
        polymer = next
    return polymer


def find_max_minus_min(polymer):
    c = Counter(polymer)
    return c.most_common()[0][1] - c.most_common()[-1][1]


def get_polymer_frequencies(original, insertion_rules, steps):
    """
    An alternative implementation for part 2, where we will only keep track of the frequencies

    Find characters along with followers

    """
    follows = {}
    for i in range(len(original) - 1):
        c = original[i]
        c_next = original[i + 1]
        if c not in follows:
            follows[c] = {}
        freqs = follows[c]
        if c_next not in freqs:
            freqs[c_next] = 0
        freqs[c_next] += 1
    # Make sure to take care of the last character
    last = original[-1]
    if last not in follows:
        follows[last] = {}
    follows[last]['EMPTY'] = 1

    for _ in range(steps):
        next_follows = {}
        for c in follows.keys():
            followers = follows[c]
            for follower in followers.keys():
                sub = c + follower
                if sub in insertion_rules:
                    # insertion_rules[sub] will now follow c
                    if c not in next_follows:
                        next_follows[c] = {}
                    d = next_follows[c]
                    if insertion_rules[sub] not in d:
                        d[insertion_rules[sub]] = 0
                    d[insertion_rules[sub]] += followers[follower]
                    # follower will not follow insertion_rules[sub]
                    if insertion_rules[sub] not in next_follows:
                        next_follows[insertion_rules[sub]] = {}
                    d2 = next_follows[insertion_rules[sub]]
                    if follower not in d2:
                        d2[follower] = 0
                    d2[follower] += followers[follower]
                else:
                    if c not in next_follows:
                        next_follows[c] = {}
                    next_follows[c][follower] = followers[follower]
        follows = next_follows

    frequencies = []
    for c in follows:
        total = 0
        for _, count in follows[c].items():
            total += count
        frequencies.append((c, total))
    max_freq = max(frequencies, key=lambda freq: freq[1])[1]
    min_freq = min(frequencies, key=lambda freq: freq[1])[1]

    return max_freq - min_freq


if __name__ == '__main__':
    with open('inputs/day14.txt') as f:
        template = f.readline().strip()
        f.readline()
        rules = {line.strip()[:2]: line.strip()[-1] for line in f.readlines()}
    # print(find_max_minus_min(generate_polymer(template, rules, 10)))
    print(get_polymer_frequencies(template, rules, 40))
