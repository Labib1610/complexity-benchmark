import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    adj = [[] for _ in range(n)]
    idx = 2

    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n

    for i in range(n):
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
    sys.stdout.write(" ".join(map(str, color)) + "\n")


if __name__ == "__main__":
    solve()