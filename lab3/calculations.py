import numpy as np


def calculate_calls(lines_count, time, alpha, betta, capacity, check, max_count):
    t = 0
    i = 0
    lines = [[] for _ in range(lines_count)]
    calls = [(0, - (np.log(1 - np.random.random()) / betta))]
    while t <= time:
        t -= (np.log(1 - np.random.random()) / alpha)
        calls.append((t, -(np.log(1 - np.random.random()) / betta)))
        i += 1
    calls = calls[:len(calls) - 1]
    #print(calls)
    missed = 0
    queue = 0
    for call in calls:
        queue = queue_len(lines, call)
        if queue == capacity and len(lines) < max_count and check:
            lines.append([])
        elif queue >= capacity:
            missed += 1
            continue
        min_t = np.inf
        ind = 0
        for i in range(len(lines)):
            if len(lines[i]) > 0 and lines[i][-1][1] < min_t:
                min_t = lines[i][-1][1]
                ind = i
            if len(lines[i]) == 0 and min_t > call[0]:
                ind = i
                break
        if len(lines[ind]) == 0 or lines[ind][-1][1] < call[0]:
            lines[ind].append((call[0], call[0] + call[1]))
        else:
            temp = lines[ind][-1][1]
            lines[ind].append((temp, temp + call[1]))
    return lines, len(calls), missed, queue, busy_lines(lines)


def queue_len(lines, call):
    length = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][-j-1][0] > call[0]:
                length += 1
            else:
                break
    return length


def busy_lines(lines):
    count = 0
    for i in lines:
        if len(i):
            count += 1
    return count

