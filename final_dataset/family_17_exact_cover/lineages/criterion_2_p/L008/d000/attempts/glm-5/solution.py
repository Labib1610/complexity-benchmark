import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    mentors = list(range(1, q + 1))
    apprentices = list(range(q + 1, 2 * q + 1))
    adj = [[] for _ in range(q + 1)]
    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx + 1])
        idx += 2
        adj[a].append(b)

    pair_m = [0] * (q + 1)
    pair_a = [0] * (2 * q + 1)
    visited = [0] * (2 * q + 1)
    tag = 0

    for u in mentors:
        tag += 1
        stack = list(adj[u])
        found = False
        while stack:
            v = stack.pop()
            if visited[v] == tag:
                continue
            visited[v] = tag
            w = pair_a[v]
            if w == 0:
                pair_a[v] = u
                pair_m[u] = v
                found = True
                break
            else:
                for nxt in adj[w]:
                    if visited[nxt] != tag:
                        stack.append(nxt)
        if not found:
            sys.stdout.write("NO\n")
            return

    out = ["YES"]
    for u in mentors:
        out.append(f"{u} {pair_m[u]}")
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()