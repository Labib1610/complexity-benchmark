import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m = map(int, input_data[:2])
    edges = []
    idx = 2
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    color = [0] * n

    def is_safe(node, c):
        for nb in adj[node]:
            if color[nb] == c:
                return False
        return True

    def backtrack(pos):
        if pos == n:
            return True
        for c in range(1, 4):
            if is_safe(pos, c):
                color[pos] = c
                if backtrack(pos + 1):
                    return True
                color[pos] = 0
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(str(x) for x in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()