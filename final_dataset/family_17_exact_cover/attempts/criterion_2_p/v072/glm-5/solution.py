import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 2 * q

    head = [-1] * (n + 1)
    to = [0] * t
    nxt = [0] * t
    idx = 0
    for i in range(t):
        a = int(data[2 + 2 * i])
        b = int(data[3 + 2 * i])
        to[idx] = b
        nxt[idx] = head[a]
        head[a] = idx
        idx += 1

    matchL = [0] * (q + 1)
    matchR = [0] * (n + 1)
    visited = [0] * (q + 1)
    timestamp = 0

    def augment(u):
        e = head[u]
        while e != -1:
            v = to[e]
            if visited[v] != timestamp:
                visited[v] = timestamp
                if matchR[v] == 0 or augment(matchR[v]):
                    matchL[u] = v
                    matchR[v] = u
                    return True
            e = nxt[e]
        return False

    ok = True
    for u in range(1, q + 1):
        timestamp += 1
        if not augment(u):
            ok = False
            break

    out = []
    if ok:
        out.append("YES")
        for u in range(1, q + 1):
            out.append(f"{u} {matchL[u]}")
    else:
        out.append("NO")

    sys.stdout.write("\n".join(out) + "\n")

solve()