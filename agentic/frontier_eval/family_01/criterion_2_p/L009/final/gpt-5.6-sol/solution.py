import sys

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n, m = values[0], values[1]

    graph = [[] for _ in range(n)]
    pos = 2
    for _ in range(m):
        u = values[pos] - 1
        v = values[pos + 1] - 1
        pos += 2
        graph[u].append(v)
        graph[v].append(u)

    del values

    color = bytearray(n)

    for start in range(n):
        if color[start]:
            continue

        color[start] = 1
        stack = [start]

        while stack:
            u = stack.pop()
            required = 3 - color[u]

            for v in graph[u]:
                if color[v] == 0:
                    color[v] = required
                    stack.append(v)
                elif color[v] != required:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)))
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()