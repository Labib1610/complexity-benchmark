import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m = int(input_data[0]), int(input_data[1])
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

    colors = [0] * n

    def is_safe(node, color):
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True

    def backtrack(node):
        if node == n:
            return True
        for c in (1, 2, 3):
            if is_safe(node, c):
                colors[node] = c
                if backtrack(node + 1):
                    return True
                colors[node] = 0
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()