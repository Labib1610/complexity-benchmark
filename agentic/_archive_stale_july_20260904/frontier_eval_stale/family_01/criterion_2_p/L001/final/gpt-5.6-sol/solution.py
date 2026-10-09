import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    graph = [[] for _ in range(n)]

    p = 2
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * n

    for start in range(n):
        if color[start] != 0:
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
    sys.stdout.write(" ".join(map(str, color)))

if __name__ == "__main__":
    main()