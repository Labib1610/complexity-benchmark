import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [[] for _ in range(n)]

    idx = 2
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2

        if u == v:
            sys.stdout.write("NO\n")
            return

        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n

    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            stack = [i]

            while stack:
                u = stack.pop()
                cu = color[u]

                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = cu ^ 1
                        stack.append(v)
                    elif color[v] == cu:
                        sys.stdout.write("NO\n")
                        return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(c + 1) for c in color))
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()