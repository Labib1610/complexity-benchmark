import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    jobs = []
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx + 1]); idx += 2
        jobs.append((p1, p2))

    # Johnson's rule: jobs with p1 <= p2 first (ascending by p1), then the rest
    # (descending by p2). This ordering minimises the two-machine finish time.
    first = sorted((x for x in jobs if x[0] <= x[1]), key=lambda x: x[0])
    second = sorted((x for x in jobs if x[0] > x[1]), key=lambda x: -x[1])
    order = first + second

    t1 = 0
    t2 = 0
    for p1, p2 in order:
        t1 += p1
        t2 = (t2 if t2 > t1 else t1) + p2

    print(t2)


main()
