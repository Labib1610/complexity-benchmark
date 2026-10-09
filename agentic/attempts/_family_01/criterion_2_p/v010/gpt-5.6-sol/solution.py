import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    graph = [[] for _ in range(n + 1)]
    pos = 2
    for _ in range(m):
        u, v = data[pos], data[pos + 1]
        pos += 2
        graph[u].append(v)
        graph[v].append(u)

    color = bytearray(n + 1)

    for start in range(1, n + 1):
        if color[start]:
            continue

        color[start] = 1
        stack = [start]

        while stack:
            u = stack.pop()
            expected = 3 - color[u]

            for v in graph[u]:
                if color[v] == 0:
                    color[v] = expected
                    stack.append(v)
                elif color[v] != expected:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == "__main__":
    main()