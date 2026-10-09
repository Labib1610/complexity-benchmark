import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    tasks = []
    for _ in range(n):
        p1 = int(next(it)); p2 = int(next(it))
        tasks.append((p1, p2))
    # split groups
    inc = []  # p1 <= p2
    dec = []  # p1 > p2
    for p1, p2 in tasks:
        if p1 <= p2:
            inc.append((p1, p2))
        else:
            dec.append((p1, p2))
    # sort inc by p1 ascending
    inc.sort(key=lambda x: x[0])
    # sort dec by p2 descending
    dec.sort(key=lambda x: x[1], reverse=True)
    order = inc + dec

    charge = 0
    allocated_sum = 0
    total = 0
    for p1, p2 in order:
        alloc = p1 if charge >= p1 else charge
        allocated_sum += alloc
        charge = charge - alloc + p2
        total += p1 + p2 - alloc
    # total is the final accumulated cost
    print(total)

if __name__ == "__main__":
    solve()