import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)          # 0 = uncolored, 1 or 2 = assigned tier

    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1           # lexicographically smallest choice for the first node of a component
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]   # 1 -> 2, 2 -> 1
                        stack.append(v)
                    elif color[v] == color[u]:
                        sys.stdout.write("NO\n")
                        return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == "__main__":
    solve()