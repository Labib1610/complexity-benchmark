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
        a = int(next(it))
        b = int(next(it))
        if a <= b:
            first.append((a, b))
        else:
            second.append((a, b))
    first.sort(key=lambda x: x[0])          # ascending a
    second.sort(key=lambda x: -x[1])        # descending b
    order = first + second

    time_solver = 0
    time_tracer = 0
    for a, b in order:
        time_solver += a
        if time_tracer < time_solver:
            time_tracer = time_solver
        time_tracer += b
    print(time_tracer)

if __name__ == "__main__":
    solve()