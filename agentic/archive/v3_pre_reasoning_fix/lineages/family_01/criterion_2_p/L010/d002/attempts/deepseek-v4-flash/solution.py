import sys

def main():
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

        if u == v:
            sys.stdout.write("NO\n")
            return

        adj[u].append(v)
        adj[v].append(u)

    del data

    color = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            stack = [start]

            while stack:
                v = stack.pop()
                cv = color[v]
                nc = 3 - cv

                for to in adj[v]:
                    if color[to] == 0:
                        color[to] = nc
                        stack.append(to)
                    elif color[to] == cv:
                        sys.stdout.write("NO\n")
                        return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")


if __name__ == "__main__":
    main()