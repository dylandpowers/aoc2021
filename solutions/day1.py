def num_increasing_depths():
    prev = -1
    ans = 0
    with open('../inputs/day1.txt') as f:
        for line in f.readlines():
            if prev == -1:
                prev = int(line)
                continue
            curr = int(line)
            if curr > prev:
                ans += 1
            prev = curr

    return ans

def num_increasing_windows():
    ans = 0
    with open('../inputs/day1.txt') as f:
        nums = [int(line) for line in f.readlines()]

    window = nums[0] + nums[1] + nums[2]

    for i in range(3, len(nums)):
        new_window = window - nums[i - 3] + nums[i]
        if new_window > window:
            ans += 1
        window = new_window

    return ans