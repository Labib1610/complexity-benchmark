import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]

    idx = 2
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)

    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            stack = [i]

            while stack:
                u = stack.pop()
                cu = color[u]

                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - cu
                        stack.append(v)
                    elif color[v] == cu:
                        sys.stdout.write("NO\n")
                        return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")


if __name__ == "__main__":
    solve()