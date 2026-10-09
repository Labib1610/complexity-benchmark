import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 2 * q + 1

    head = [-1] * n
    to = [0] * t
    nxt = [0] * t

    idx = 2
    for e in range(t):
        a = int(data[idx]); b = int(data[idx+1]); idx += 2
        to[e] = b
        nxt[e] = head[a]
        head[a] = e

    match = [0] * n
    for v in range(1, q+1):
        match[v] = 0
    for v in range(q+1, n):
        match[v] = 0

    parent = [0] * n
    base = list(range(n))
    queue = [0] * n
    in_queue = [False] * n
    in_blossom = [False] * n
    used = [False] * n

    for start in range(1, q+1):
        if match[start] != 0:
            continue

        for v in range(1, n):
            parent[v] = 0
            base[v] = v
            in_queue[v] = False
            in_blossom[v] = False
            used[v] = False

        qh = 0; qt = 0
        queue[qt] = start; qt += 1
        in_queue[start] = True
        parent[start] = start
        found = False

        while qh < qt and not found:
            v = queue[qh]; qh += 1
            e = head[v]
            while e != -1:
                w = to[e]
                e = nxt[e]
                if base[v] == base[w] or match[v] == w:
                    continue

                if parent[base[w]] == 0 and match[w] == 0 and w != start:
                    parent[base[w]] = v
                    cur = w
                    while cur != 0:
                        p = parent[cur]
                        pp = match[p]
                        match[cur] = p
                        match[p] = cur
                        cur = pp
                    found = True
                    break

                if parent[base[w]] == 0:
                    parent[base[w]] = v
                    u = match[w]
                    if u != 0 and not in_queue[base[u]]:
                        in_queue[base[u]] = True
                        queue[qt] = u; qt += 1
                    continue

                a = base[v]
                b = base[w]
                while a != b:
                    used[a] = True
                    used[b] = True
                    a = base[parent[match[a]]]
                    b = base[parent[match[b]]]

                new_base = base[v]
                a = base[v]
                while a != new_base:
                    in_blossom[a] = True
                    a = base[parent[match[a]]]
                a = base[w]
                while a != new_base:
                    in_blossom[a] = True
                    a = base[parent[match[a]]]

                for x in range(1, n):
                    if in_blossom[base[x]]:
                        base[x] = new_base
                        if not in_queue[base[x]] and parent[base[x]] != 0:
                            in_queue[base[x]] = True
                            queue[qt] = x; qt += 1

                for x in range(1, n):
                    in_blossom[x] = False
                    used[x] = False

            if found:
                break

    ok = True
    for v in range(1, q+1):
        if match[v] == 0:
            ok = False
            break

    out = []
    if ok:
        out.append("YES")
        for v in range(1, q+1):
            out.append(f"{v} {match[v]}")
    else:
        out.append("NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()