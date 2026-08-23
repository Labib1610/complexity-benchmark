import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    idx = 0
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    idx += 2
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    # colors[i] stores the band assigned to transmitter i (1-based)
    colors = [0] * (n + 1)
    
    def is_valid(node, color):
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
        
        for color in [1, 2, 3]:
            if is_valid(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0
        
        return False
    
    if backtrack(1):
        print("YES")
        print(" ".join(str(colors[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()