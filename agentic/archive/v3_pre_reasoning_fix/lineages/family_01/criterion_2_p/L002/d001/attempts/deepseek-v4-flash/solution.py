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

    color = [-1] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue

        color[start] = 0
        stack = [start]

        while stack:
            u = stack.pop()
            cu = color[u]

            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - cu
                    stack.append(v)
                elif color[v] == cu:
                    print("NO")
                    return

    ans = ['1' if color[i] == 0 else '2' for i in range(1, n + 1)]
    print("YES")
    print(" ".join(ans))

if __name__ == "__main__":
    main()