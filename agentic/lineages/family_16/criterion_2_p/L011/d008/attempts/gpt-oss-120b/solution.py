import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    jobs = []
    for _ in range(n):
        x = int(next(it))
        y = int(next(it))
        jobs.append((x, y))

    # Johnson's rule
    first = []
    second = []
    for x, y in jobs:
        if x < y:
            first.append((x, y))
        else:
            second.append((x, y))
    first.sort(key=lambda p: p[0])          # increasing X
    second.sort(key=lambda p: -p[1])        # decreasing Y
    ordered = first + second

    time_struct = 0   # completion time on machine 1 (Structural)
    time_cargo = 0    # completion time on machine 2 (Cargo)
    for x, y in ordered:
        time_struct += x
        time_cargo = max(time_cargo, time_struct) + y

    sys.stdout.write(str(time_cargo))

if __name__ == "__main__":
    solve()