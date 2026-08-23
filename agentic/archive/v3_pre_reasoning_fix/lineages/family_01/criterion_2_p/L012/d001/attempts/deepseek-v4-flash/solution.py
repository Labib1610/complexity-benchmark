import sys

def solve():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    try:
        n = next(data)
    except StopIteration:
        return
    m = next(data)

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(data) - 1
        v = next(data) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n

    for start in range(n):
        if color[start] == 0:
            color[start] = 1
            stack = [start]

            while stack:
                u = stack.pop()
                need = 3 - color[u]

                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = need
                        stack.append(v)
                    elif color[v] != need:
                        sys.stdout.write("NO\n")
                        return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)))
    sys.stdout.write("\n")

if __name__ == "__main__":
    solve()