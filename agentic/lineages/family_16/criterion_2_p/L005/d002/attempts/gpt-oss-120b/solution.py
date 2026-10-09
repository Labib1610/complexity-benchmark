import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    it = iter(data[1:])
    early = []   # a <= b
    late = []    # a > b
    for a, b in zip(it, it):
        if a <= b:
            early.append((a, b))
        else:
            late.append((a, b))

    early.sort(key=lambda x: x[0])          # increasing a
    late.sort(key=lambda x: -x[1])          # decreasing b
    order = early + late

    alpha_time = 0
    beta_time = 0
    for a, b in order:
        alpha_time += a                     # finish of Alpha
        beta_time = max(alpha_time, beta_time) + b
    print(beta_time)

if __name__ == "__main__":
    solve()