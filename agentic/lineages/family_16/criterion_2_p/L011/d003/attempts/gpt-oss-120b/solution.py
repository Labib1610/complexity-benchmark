import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    left = []   # p1 <= p2
    right = []  # p1 > p2
    for _ in range(n):
        p1 = int(next(it)); p2 = int(next(it))
        if p1 <= p2:
            left.append((p1, p2))
        else:
            right.append((p1, p2))
    left.sort(key=lambda x: x[0])          # ascending p1
    right.sort(key=lambda x: x[1], reverse=True)  # descending p2
    seq = left + right

    time1 = 0
    time2 = 0
    for p1, p2 in seq:
        time1 += p1
        if time2 < time1:
            time2 = time1
        time2 += p2
    print(time2)

if __name__ == "__main__":
    solve()