import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # We need to find a valid 3-coloring.
    # We use a recursive backtracking search with pruning.
    # The graph is small (n <= 40), so this is feasible.
    
    colors = [0] * n  # 0: uncolored, 1-3: colors
    
    # Optimization: order vertices by degree descending to fail faster
    order = list(range(n))
    order.sort(key=lambda x: len(adj[x]), reverse=True)
    
    # Map from position in recursion to vertex index
    # We fill colors[vertex] but iterate through 'order'
    
    def backtrack(k):
        if k == n:
            return True
        
        u = order[k]
        
        # Determine available colors for u
        # Neighbors might not be colored yet, but we check those that are.
        # Since we process in order, we only need to check against already colored neighbors.
        used = set()
        for v in adj[u]:
            if colors[v] != 0:
                used.add(colors[v])
        
        for c in range(1, 4):
            if c not in used:
                colors[u] = c
                if backtrack(k + 1):
                    return True
                colors[u] = 0
        
        return False

    if backtrack(0):
        print("YES")
        # The colors array is filled according to vertex indices 0..n-1
        print(*(colors))
    else:
        print("NO")

if __name__ == '__main__':
    solve()