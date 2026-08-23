import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n  # 0 unvisited, 1 or 2 assigned
    for i in range(n):
        if color[i] != 0:
            continue
        # start a new component; assign the smallest index in it color 1
        stack = [i]
        color[i] = 1
        while stack:
            u = stack.pop()
            cu = color[u]
            other = 3 - cu
            for w in adj[u]:
                if color[w] == 0:
                    color[w] = other
                    stack.append(w)
                elif color[w] == cu:
                    print("NO")
                    return

    print("YES")
    sys.stdout.write(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()