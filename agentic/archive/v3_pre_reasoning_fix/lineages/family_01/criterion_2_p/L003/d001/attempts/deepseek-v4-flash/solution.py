import sys

def main():
    input = sys.stdin.buffer.readline

    first = input().split()
    if not first:
        return

    n, m = map(int, first)
    adj = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n

    for i in range(n):
        if color[i] != -1:
            continue

        color[i] = 0
        stack = [i]

        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    stack.append(v)
                elif color[v] == color[u]:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(c + 1) for c in color) + "\n")


if __name__ == "__main__":
    main()