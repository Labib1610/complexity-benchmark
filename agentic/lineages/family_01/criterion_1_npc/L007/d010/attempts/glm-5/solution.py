import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Precompute resonance scores
    # score[cu][cv] = trace(A_cu * A_cv^T)
    # A1 = [[0,1,0],[0,0,1],[1,0,0]]
    # A2 = [[0,0,1],[1,0,0],[0,1,0]]
    # A3 = [[1,0,0],[0,1,0],[0,0,1]]
    # A1^T = [[0,0,1],[1,0,0],[0,1,0]] = A2
    # A2^T = [[0,1,0],[0,0,1],[1,0,0]] = A1
    # A3^T = A3
    # A1 * A1^T = A1 * A2 = I, trace = 3
    # A1 * A2^T = A1 * A1 = [[0,0,1],[1,0,0],[0,1,0]], trace = 0
    # A1 * A3^T = A1 * A3 = A1, trace = 0
    # A2 * A2^T = A2 * A1 = I, trace = 3
    # A2 * A3^T = A2 * A3 = A2, trace = 0
    # A3 * A3^T = A3 * A3 = I, trace = 3
    # score[1][1] = 3, score[1][2] = 0, score[1][3] = 0
    # score[2][1] = 0, score[2][2] = 3, score[2][3] = 0
    # score[3][1] = 0, score[3][2] = 0, score[3][3] = 3
    
    # States: 0, 1, 2 (representing 1, 2, 3)
    # score[u][v] = 3 if u == v else 0
    # Sum of scores = 0 means no edge can have same states on endpoints.
    # This is a graph coloring problem with 3 colors.
    
    color = [-1] * n
    
    def is_safe(u, c):
        for v in adj[u]:
            if color[v] == c:
                return False
        return True
    
    # Find the smallest uncolored vertex
    # Since we want lexicographically smallest, we try colors 0, 1, 2 in order
    # and process vertices 0, 1, ..., n-1.
    
    def backtrack(idx):
        if idx == n:
            return True
        
        u = idx
        # Try colors 0, 1, 2 (representing states 1, 2, 3)
        for c in range(3):
            if is_safe(u, c):
                color[u] = c
                if backtrack(idx + 1):
                    return True
                color[u] = -1
        return False
    
    if backtrack(0):
        print("YES")
        # Convert 0, 1, 2 back to 1, 2, 3
        print(' '.join(str(x + 1) for x in color))
    else:
        print("NO")

if __name__ == '__main__':
    solve()