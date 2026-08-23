import sys

def main():
    input = sys.stdin.buffer.readline

    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n

    for start in range(n):
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
    sys.stdout.write(" ".join(map(str, color)) + "\n")


Need import sys. yes.

Could optimize with `out = []`, but no need Mendel.

Now final code block.