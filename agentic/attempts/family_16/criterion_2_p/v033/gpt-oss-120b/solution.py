import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    a = []          # p1 <= p2
    b = []          # p1 >  p2
    for _ in range(n):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 <= p2:
            a.append((p1, p2))
        else:
            b.append((p1, p2))

    a.sort(key=lambda x: x[0])               # ascending p1
    b.sort(key=lambda x: -x[1])              # descending p2

    time1 = 0
    time2 = 0
    for p1, p2 in a:
        time1 += p1
        if time2 < time1:
            time2 = time1 + p2
        else:
            time2 += p2
    for p1, p2 in b:
        time1 += p1
        if time2 < time1:
            time2 = time1 + p2
        else:
            time2 += p2

    sys.stdout.write(str(time2))

if __name__ == "__main__":
    solve()