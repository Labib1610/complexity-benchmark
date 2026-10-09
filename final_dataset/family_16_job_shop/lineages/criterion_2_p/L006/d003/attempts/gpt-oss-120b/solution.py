import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    first = []
    second = []
    for _ in range(n):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 < p2:
            first.append((p1, p2))
        else:
            second.append((p1, p2))
    # Johnson's rule
    first.sort(key=lambda x: x[0])          # ascending p1
    second.sort(key=lambda x: -x[1])        # descending p2
    order = first + second

    time_entry = 0
    time_land = 0
    for p1, p2 in order:
        time_entry += p1
        if time_land < time_entry:
            time_land = time_entry
        time_land += p2
    print(time_land)

if __name__ == "__main__":
    solve()