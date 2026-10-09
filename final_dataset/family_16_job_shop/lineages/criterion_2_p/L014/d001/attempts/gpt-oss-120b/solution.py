import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    front = []  # p1 <= p2
    back = []   # p1 > p2
    for _ in range(n):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 <= p2:
            front.append((p1, p2))
        else:
            back.append((p1, p2))
    front.sort(key=lambda x: x[0])          # increasing p1
    back.sort(key=lambda x: x[1], reverse=True)  # decreasing p2
    seq = front + back

    oven_time = 0
    icing_time = 0
    for p1, p2 in seq:
        oven_time += p1
        icing_time = (oven_time if oven_time > icing_time else icing_time) + p2
    sys.stdout.write(str(icing_time))

if __name__ == "__main__":
    solve()