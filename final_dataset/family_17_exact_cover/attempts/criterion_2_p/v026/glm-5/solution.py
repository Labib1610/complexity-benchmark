import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 2 * q
    head = [-1] * (n + 1)
    to = [0] * (2 * t)
    nxt = [0] * (2 * t)
    edge_cnt = 0

    def add_edge(u, v):
        nonlocal edge_cnt
        to[edge_cnt] = v
        nxt[edge_cnt] = head[u]
        head[u] = edge_cnt
        edge_cnt += 1

    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        add_edge(a, b)
        add_edge(b, a)

    match = [0] * (n + 1)
    used = [0] * (n + 1)
    timestamp = 0

    def dfs(u):
        nonlocal timestamp
        e = head[u]
        while e != -1:
            v = to[e]
            if used[v] != timestamp:
                used[v] = timestamp
                if match[v] == 0 or dfs(match[v]):
                    match[v] = u
                    match[u] = v
                    return True
            e = nxt[e]
        return False

    result = 0
    for u in range(1, q + 1):
        if match[u] == 0:
            timestamp += 1
            if dfs(u):
                result += 1
            else:
                break

    if result == q:
        out = ["YES"]
        for u in range(1, q + 1):
            out.append(f"{u} {match[u]}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    main()