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

    color = [0] * n

    for start in range(n):
        if color[start] != 0:
            continue

        color[start] = 1
        stack = [start]

        while stack:
            u = stack.pop()
            expected = 3 - color[u]

            for v in adj[u]:
                if color[v] == 0:
                    color[v] = expected
                    stack.append(v)
                elif color[v] != expected:
                    print("NO")
                    return

    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    main()