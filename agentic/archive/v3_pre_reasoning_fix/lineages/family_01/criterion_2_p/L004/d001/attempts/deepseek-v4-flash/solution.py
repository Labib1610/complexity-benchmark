import sys

def main():
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
        if u == v:
            sys.stdout.write("NO\n")
            return
        adj[u].append(v)
        adj[v].append(u)

    del data, it

    color = bytearray(n + 1)

    for start in range(1, n + 1):
        if color[start]:
            continue

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
    sys.stdout.write(" ".join(map(str, color[1:])))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()