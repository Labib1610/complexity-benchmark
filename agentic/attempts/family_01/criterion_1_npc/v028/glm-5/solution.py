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

    # Colors: 1, 2, 3
    color = [0] * n
    
    # Backtracking with pruning
    # We assign colors to vertices 0 to n-1 in order.
    # This naturally satisfies the lexicographical minimality requirement.
    
    def backtrack(k):
        if k == n:
            return True
        
        # Determine forbidden colors for vertex k based on assigned neighbors
        forbidden = [False] * 4
        for neighbor in adj[k]:
            if neighbor < k: # Neighbor already assigned
                c = color[neighbor]
                forbidden[c] = True
        
        # Try colors in increasing order: 1, 2, 3
        for c in range(1, 4):
            if not forbidden[c]:
                color[k] = c
                if backtrack(k + 1):
                    return True
                color[k] = 0 # Backtrack
        
        return False

    if backtrack(0):
        print("YES")
        print(*(color))
    else:
        print("NO")

if __name__ == '__main__':
    solve()