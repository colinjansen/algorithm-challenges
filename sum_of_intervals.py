def sum_of_intervals(input):
    offsets = {}
    output = 0
    d = 0
    n = 0

    for (a, b) in input:
        if a not in offsets: offsets[a] = 0
        if b not in offsets: offsets[b] = 0
        offsets[a] += 1
        offsets[b] -= 1

    for i in sorted(offsets):
        if d == 0: n = i
        d += offsets[i]
        if d == 0: output += i - n

    return output
