import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))

    A = []          # p1 <= p2
    B = []          # p1 >  p2
    for _ in range(n):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 <= p2:
            A.append((p1, p2))
        else:
            B.append((p1, p2))

    A.sort(key=lambda x: x[0])          # increasing p1
    B.sort(key=lambda x: -x[1])         # decreasing p2

    time1 = 0
    time2 = 0
    for p1, p2 in A:
        time1 += p1
        time2 = max(time2, time1) + p2
    for p1, p2 in B:
        time1 += p1
        time2 = max(time2, time1) + p2

    sys.stdout.write(str(time2))

if __name__ == "__main__":
    solve()