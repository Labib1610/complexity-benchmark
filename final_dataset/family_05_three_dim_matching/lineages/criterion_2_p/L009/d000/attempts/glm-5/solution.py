import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    idx = 2
    adj = [[] for _ in range(k + 1)]
    for _ in range(t):
        e = int(data[idx]); d = int(data[idx+1]); i = int(data[idx+2])
        idx += 3
        adj[e].append(i)

    match_to_e = [0] * (k + 1)
    visited = [0] * (k + 1)
    stamp = 0

    def try_kuhn(e):
        nonlocal stamp
        for i in adj[e]:
            if visited[i] != stamp:
                visited[i] = stamp
                if match_to_e[i] == 0 or try_kuhn(match_to_e[i]):
                    match_to_e[i] = e
                    return True
        return False

    matched = 0
    for e in range(1, k + 1):
        stamp += 1
        if try_kuhn(e):
            matched += 1

    if matched != k:
        sys.stdout.write("NO\n")
        return

    out = ["YES"]
    for i in range(1, k + 1):
        e = match_to_e[i]
        out.append(f"{e} {e} {i}")
    sys.stdout.write("\n".join(out) + "\n")

solve()