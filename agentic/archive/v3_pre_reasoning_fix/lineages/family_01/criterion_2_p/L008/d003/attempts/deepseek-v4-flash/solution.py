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

    color = bytearray(n + 1)

    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            stack = [start]

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
    sys.stdout.write(" ".join(map(str, color[1:])))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()