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
        adj[u].append(v)
        adj[v].append(u)

    del data

    color = [-1] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue

        color[start] = 0
        stack = [start]

        while stack:
            v = stack.pop()
            cv = color[v]
            nc = cv ^ 1

            for to in adj[v]:
                if color[to] == -1:
                    color[to] = nc
                    stack.append(to)
                elif color[to] == cv:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join("1" if color[i] == 0 else "2" for i in range(1, n + 1)))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()