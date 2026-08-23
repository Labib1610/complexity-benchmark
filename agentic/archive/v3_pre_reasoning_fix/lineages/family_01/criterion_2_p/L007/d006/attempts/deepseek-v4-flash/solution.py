import sys

def main():
    input = sys.stdin.buffer.readline

    first = input().split()
    if not first:
        return

    n = int(first[0])
    m = int(first[1])

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != 0:
            continue

        color[start] = 1
        stack = [start]

        while stack:
            u = stack.pop()
            cu = color[u]
            nc = 2 if cu == 1 else 1

            for v in adj[u]:
                if color[v] == 0:
                    color[v] = nc
                    stack.append(v)
                elif color[v] == cu:
                    print("NO")
                    return

    print("YES")
    print(" ".join(map(str, color[1:])))

if __name__ == "__main__":
    main()