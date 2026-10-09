import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    nL = int(data[0]); nR = int(data[1]); m = int(data[2])
    deg = [0] * (nL + nR + 2)
    offL = 1
    offR = nL + 1
    edges = []
    idx = 3
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        edges.append((u, v))
        deg[offL + u] += 1
        deg[offR + v] += 1
    delta = 0
    for d in deg:
        if d > delta:
            delta = d
    if delta == 0:
        out = ["YES"]
        out.append("")
        sys.stdout.write("\n".join(out))
        return
    # Build adjacency lists with edge indices
    head = [-1] * (nL + nR + 2)
    to = [0] * m
    nxt = [0] * m
    for i, (u, v) in enumerate(edges):
        a = offL + u
        b = offR + v
        to[i] = b
        nxt[i] = head[a]
        head[a] = i
        to[m + i] = a
        nxt[m + i] = head[b]
        head[b] = m + i
    color = [0] * m
    used = [0] * (delta + 2)
    for a in range(1, nL + nR + 2):
        e = head[a]
        while e != -1:
            ei = e if e < m else e - m
            c = color[ei]
            if c:
                used[c] = 1
            e = nxt[e]
        c = 1
        e = head[a]
        while e != -1:
            ei = e if e < m else e - m
            if color[ei] == 0:
                while used[c]:
                    c += 1
                color[ei] = c
                c += 1
            e = nxt[e]
        e = head[a]
        while e != -1:
            ei = e if e < m else e - m
            used[color[ei]] = 0
            e = nxt[e]
    out = ["YES"]
    out.append(" ".join(map(str, color)))
    sys.stdout.write("\n".join(out))

main()