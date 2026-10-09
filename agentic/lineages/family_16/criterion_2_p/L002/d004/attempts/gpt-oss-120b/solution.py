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

    L = 0
    F = 0
    for p1, p2 in seq:
        L += p1
        if F < L:
            F = L + p2
        else:
            F = F + p2
    print(F)

if __name__ == "__main__":
    solve()