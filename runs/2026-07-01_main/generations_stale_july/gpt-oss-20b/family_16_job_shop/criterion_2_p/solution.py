import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    jobs = []
    idx = 1
    for _ in range(n):
        p1 = data[idx]
        p2 = data[idx + 1]
        idx += 2
        jobs.append((p1, p2))

    group_a = []
    group_b = []
    for p1, p2 in jobs:
        if p1 <= p2:
            group_a.append((p1, p2))
        else:
            group_b.append((p1, p2))

    group_a.sort(key=lambda x: x[0])          # ascending p1
    group_b.sort(key=lambda x: -x[1])         # descending p2

    order = group_a + group_b

    time1 = 0
    time2 = 0
    for p1, p2 in order:
        time1 += p1
        if time2 < time1:
            time2 = time1
        time2 += p2

    print(time2)

if __name__ == "__main__":
    main()