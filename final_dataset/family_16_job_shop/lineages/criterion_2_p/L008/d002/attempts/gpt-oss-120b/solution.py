import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    front = []   # p1 <= p2
    back = []    # p1 > p2
    for _ in range(n):
        p1 = int(next(it)); p2 = int(next(it))
        if p1 <= p2:
            front.append((p1, p2))
        else:
            back.append((p1, p2))
    front.sort(key=lambda x: x[0])          # ascending p1
    back.sort(key=lambda x: x[1], reverse=True)  # descending p2
    seq = front + back

    t1 = 0  # finish time on Radar (machine 1)
    t2 = 0  # finish time on Sampling (machine 2)
    for p1, p2 in seq:
        t1 += p1
        if t2 < t1:
            t2 = t1
        t2 += p2
    print(t2)

if __name__ == "__main__":
    solve()