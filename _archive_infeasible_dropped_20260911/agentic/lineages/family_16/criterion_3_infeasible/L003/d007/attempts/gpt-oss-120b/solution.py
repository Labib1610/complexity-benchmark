import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))

    sum_a = 0
    sum_b = 0
    bad_team = -1  # 1‑based index, -1 means none found yet

    for idx in range(1, j + 1):
        a = int(next(it))
        b = int(next(it))
        if bad_team == -1 and a + b > T:
            bad_team = idx
        sum_a += a
        sum_b += b

    out = []
    if bad_team != -1:
        out.append(f"JOB {bad_team}")
    elif sum_a > T:
        out.append("LOAD 1")
    else:
        out.append("LOAD 2")
    sys.stdout.write(out[0])

if __name__ == "__main__":
    solve()