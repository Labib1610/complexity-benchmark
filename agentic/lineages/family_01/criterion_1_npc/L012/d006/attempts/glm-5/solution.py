import sys

def solve():
    data = sys.stdin.read().strip().split()
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
    
    # We need to find a valid 3-coloring where adjacent vertices have different colors.
    # Minimize the hash sum c_i * 2^{2n - 2i}.
    # This is equivalent to lexicographically minimizing the color sequence (c_1, c_2, ..., c_n).
    
    color = [0] * n
    
    def dfs(u):
        for v in adj[u]:
            if color[v] == 0:
                # Try colors 1, 2, 3 in order
                for c in range(1, 4):
                    if c != color[u]:
                        color[v] = c
                        if dfs(v):
                            return True
                        color[v] = 0
                return False
            elif color[v] == color[u]:
                return False
        return True

    possible = False
    # Try starting colors 1, 2, 3 for the first vertex
    for start_color in range(1, 4):
        color = [0] * n
        color[0] = start_color
        if dfs(0):
            possible = True
            break
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, color)))

if __name__ == '__main__':
    solve()