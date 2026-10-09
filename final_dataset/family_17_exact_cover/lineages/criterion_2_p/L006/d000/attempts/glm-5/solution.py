import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        adj[a].append(b)

    matchL = [0] * (q + 1)
    matchR = [0] * (2 * q + 1)
    seen = [0] * (2 * q + 1)
    cur = 0

    def try_kuhn(v):
        nonlocal cur
        for to in adj[v]:
            if seen[to] == cur:
                continue
            seen[to] = cur
            if matchR[to] == 0 or try_kuhn(matchR[to]):
                matchL[v] = to
                matchR[to] = v
                return True
        return False

    for v in range(1, q + 1):
        cur += 1
        if not try_kuhn(v):
            sys.stdout.write("NO\n")
            return

    out = ["YES"]
    for v in range(1, q + 1):
        out.append(f"{v} {matchL[v]}")
    sys.stdout.write("\n".join(out) + "\n")

solve()