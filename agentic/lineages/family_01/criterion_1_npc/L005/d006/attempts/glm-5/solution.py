import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    adj = [set() for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u].add(v)
        adj[v].add(u)
    
    # Determinant of [[1, a, a^2], [1, b, b^2], [1, 4, 16]] is (a-b)(a-4)(b-4).
    # For a, b in {1,2,3}, it's zero iff a == b.
    # So adjacent vertices must have different colors.
    # This is 3-coloring with lexicographically smallest solution.
    
    color = [0] * n
    possible = True
    
    def dfs(v):
        nonlocal possible
        for nb in adj[v]:
            if color[nb] == color[v]:
                possible = False
                return
            if color[nb] == 0:
                for c in range(1, 4):
                    if c != color[v]:
                        color[nb] = c
                        dfs(nb)
                        if not possible:
                            return
                        break
                if color[nb] == 0:
                    possible = False
                    return
    
    for i in range(n):
        if color[i] == 0:
            color[i] = 1
            dfs(i)
            if not possible:
                break
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, color)))

solve()