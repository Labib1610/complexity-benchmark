import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    # Bipartite matching: left side 1..q (satellites), right side q+1..2q (sectors)
    # We map right side to 0..q-1 by subtracting q+1
    head = [-1] * (q + 1)
    to = [0] * t
    nxt = [0] * t
    for i in range(t):
        a = int(next(it))
        b = int(next(it))
        to[i] = b - (q + 1)
        nxt[i] = head[a]
        head[a] = i
    
    match_l = [0] * (q + 1)  # match_l[a] = sector index (0-based) matched to satellite a
    match_r = [-1] * q       # match_r[sector_index] = satellite matched to this sector
    # We use match_l[a] = sector+1, so 0 means unmatched
    
    def try_kuhn(v, visited):
        e = head[v]
        while e != -1:
            u = to[e]
            if not visited[u]:
                visited[u] = True
                if match_r[u] == -1 or try_kuhn(match_r[u], visited):
                    match_l[v] = u + 1
                    match_r[u] = v
                    return True
            e = nxt[e]
        return False
    
    result = True
    for v in range(1, q + 1):
        visited = [False] * q
        if not try_kuhn(v, visited):
            result = False
            break
    
    out = []
    if result:
        out.append("YES")
        for v in range(1, q + 1):
            sector = match_l[v] - 1 + (q + 1)
            out.append(f"{v} {sector}")
    else:
        out.append("NO")
    
    sys.stdout.write("\n".join(out))

solve()