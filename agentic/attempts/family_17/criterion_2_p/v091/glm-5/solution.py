import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    adj = [[] for _ in range(q + 1)]
    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx + 1])
        idx += 2
        adj[a].append(b)
    
    match_to = [0] * (2 * q + 1)
    match_from = [0] * (q + 1)
    
    def try_kuhn(v):
        if used[v]:
            return False
        used[v] = True
        for to in adj[v]:
            if match_to[to] == 0 or try_kuhn(match_to[to]):
                match_to[to] = v
                match_from[v] = to
                return True
        return False
    
    used = [False] * (q + 1)
    for v in range(1, q + 1):
        used = [False] * (q + 1)
        if not try_kuhn(v):
            print("NO")
            return
    
    out = ["YES"]
    for v in range(1, q + 1):
        out.append(f"{v} {match_from[v]}")
    sys.stdout.write("\n".join(out))

solve()