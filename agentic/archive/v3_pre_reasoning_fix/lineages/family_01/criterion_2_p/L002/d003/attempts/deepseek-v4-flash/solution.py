import sys

def main():
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

    color = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue

        color[start] = 0
        stack = [start]

        while stack:
            u = stack.pop()
            expected = 1 - color[u]

            for v in adj[u]:
                if color[v] == -1:
                    color[v] = expected
                    stack.append(v)
                elif color[v] != expected:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(c + 1) for c in color))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()