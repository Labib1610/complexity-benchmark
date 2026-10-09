import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    jobs = []
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        jobs.append((a, b))
    # Johnson's rule
    left = []
    right = []
    for a, b in jobs:
        if a <= b:
            left.append((a, b))
        else:
            right.append((a, b))
    left.sort(key=lambda x: x[0])          # ascending A
    right.sort(key=lambda x: x[1], reverse=True)  # descending B
    seq = left + right

    up_time = 0
    down_time = 0
    for a, b in seq:
        up_time += a
        down_time = max(up_time, down_time) + b
    print(down_time)

if __name__ == "__main__":
    solve()