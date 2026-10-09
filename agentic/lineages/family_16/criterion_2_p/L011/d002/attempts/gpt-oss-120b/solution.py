import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    early = []   # p1 <= p2
    late = []    # p1 > p2
    for _ in range(n):
        p1 = int(next(it)); p2 = int(next(it))
        if p1 <= p2:
            early.append((p1, p2))
        else:
            late.append((p1, p2))
    # sort early by increasing p1, late by decreasing p2
    early.sort(key=lambda x: x[0])
    late.sort(key=lambda x: -x[1])
    order = early + late

    time1 = 0   # completion time on Main Stage
    time2 = 0   # completion time on Review Room
    for p1, p2 in order:
        time1 += p1
        time2 = max(time2, time1) + p2
    print(time2)

if __name__ == "__main__":
    solve()