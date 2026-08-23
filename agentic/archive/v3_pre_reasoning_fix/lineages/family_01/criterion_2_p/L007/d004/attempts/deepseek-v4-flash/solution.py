import sys

def main():
    input = sys.stdin.buffer.readline
    first = input().split()
    if not first:
        return

    n, m = map(int, first)
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            if not adj[start]:
                continue

            stack = [start]
            while stack:
                u = stack.pop()
                need = 3 - color[u]

                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = need
                        stack.append(v)
                    elif color[v] != need:
                        sys.stdout.write("NO\n")
                        return

    sys.stdout.write("YES\n" + " ".join(map(str, color[1:])) + "\n")

if __name__ == "__main__":
    main()