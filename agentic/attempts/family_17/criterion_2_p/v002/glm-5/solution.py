import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 2 * q

    head = [-1] * (n + 1)
    to = [0] * (t + 1)
    nxt = [0] * (t + 1)
    idx = 0
    for i in range(t):
        a = int(data[2 + 2 * i])
        b = int(data[3 + 2 * i])
        idx += 1
        to[idx] = b
        nxt[idx] = head[a]
        head[a] = idx

    match = [0] * (n + 1)
    visited = [0] * (n + 1)
    timestamp = 0

    def try_kuhn(v):
        nonlocal timestamp
        timestamp += 1
        stack = [(v, head[v])]
        path = []
        while stack:
            node, e = stack[-1]
            if e == -1:
                stack.pop()
                if path:
                    path.pop()
                continue
            u = to[e]
            stack[-1] = (node, nxt[e])
            if visited[u] != timestamp:
                visited[u] = timestamp
                path.append(u)
                if match[u] == 0:
                    for w in path:
                        match[w] = node
                        match[node] = w
                        node = match[node]
                    return True
                stack.append((match[u], head[match[u]]))
        return False

    for v in range(1, q + 1):
        if match[v] == 0:
            if not try_kuhn(v):
                sys.stdout.write("NO\n")
                return

    out = ["YES"]
    for v in range(1, q + 1):
        out.append(f"{v} {match[v]}")
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()