def num_fish_80_days():
    with open('../inputs/day6.txt') as f:
        fish = [int(x.strip()) for x in f.readline().split(',')]

    for i in range(80):
        new_fish = []
        for age in fish:
            if age == 0:
                new_fish.append(6)
                new_fish.append(8)
            else:
                new_fish.append(age - 1)
        fish = new_fish
    return len(fish)


def num_fish_256_days():
    with open('../inputs/day6.txt') as f:
        fish = [int(x.strip()) for x in f.readline().split(',')]

    # dp[i] is the number of fish that will be creating a new fish on day i
    dp = [0] * 256
    total = 0
    for age in fish:
        dp[age] += 1
        total += 1

    for i in range(256):
        total += dp[i]
        if i < 249:
            dp[i + 7] += dp[i]
        if i < 247:
            dp[i + 9] += dp[i]
    print(dp)
    return total


