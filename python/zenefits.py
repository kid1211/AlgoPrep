# Given an array of meeting time intervals consisting of start and end times[[s1, e1], [s2, e2], ...](si < ei),
# find the start time and end times during which the most meeting rooms are occupied.

# Example 1:

# Input: [[5, 10], [0, 30], [15, 28], [8, 12], [16, 22]]
# Output: [[8, 10], [16, 22]](3 meeting rooms are occupied)

# Example 2:

# Input: [[7, 10], [10, 20]]
# Output: [[7, 20]](1 meeting room is occupied)

def meetingroom(intervals):
    ins = []
    for int in intervals:
        ins.append((int[0], 1))
        ins.append((int[1], -1))
    ins.sort()
    online, maxOnline = 0, 0
    res = []
    lastStart = None

    for pt, delta in ins:
        online += delta

        if online > maxOnline:
            lastStart = pt
            maxOnline = online
            res = []
        elif online < maxOnline:
            merge(res, lastStart, pt)
            lastStart = None
        else:
            lastStart = pt
    return res


def merge(res, start, end):
    if not start or start == end:
        return

    if res and res[-1][1] == start:
        res[-1][1] = end
    else:
        res.append([start, end])


if __name__ == "__main__":
    # res = meetingroom([[7, 10], [10, 20]])
    res = meetingroom([[5, 10], [0, 20], [15, 20], [8, 12], [16, 22]])
    print(res)
