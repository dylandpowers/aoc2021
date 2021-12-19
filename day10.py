from collections import deque

ILLEGAL_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

COMPLETION_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def total_syntax_error_score(lines):
    score = 0
    for line in lines:
        stack = deque()
        for char in line:
            if char in PAIRS:
                stack.append(char)
            else:
                if not stack:
                    score += ILLEGAL_SCORES[char]
                    break

                top = stack.pop()
                if PAIRS[top] != char:
                    score += ILLEGAL_SCORES[char]
                    break

    return score


def middle_score(lines):
    scores = []
    for line in lines:
        stack = deque()
        corrupted = False
        for char in line:
            if char in PAIRS:
                stack.append(char)
            else:
                if not stack:
                    corrupted = True
                    break

                top = stack.pop()
                if PAIRS[top] != char:
                    corrupted = True
                    break
        if not corrupted:
            score = 0
            while stack:
                score *= 5
                score += COMPLETION_SCORES[PAIRS[stack.pop()]]
            scores.append(score)

    return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
    with open('inputs/day10.txt') as f:
        data = [line.strip() for line in f.readlines()]
    print(total_syntax_error_score(data))
    print(middle_score(data))
