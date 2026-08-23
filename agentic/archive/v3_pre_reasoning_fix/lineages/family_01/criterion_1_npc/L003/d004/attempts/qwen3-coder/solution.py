from itertools import product

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        edges.append((u, v))
        idx += 2

    # We need to assign stages 1,2,3 to each node such that for every edge (u,v):
    # stage[u] * stage[v] is not a perfect square.
    
    # Precompute which pairs of stages are forbidden (i.e., their product is a perfect square)
    forbidden = [[False]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            prod = (i+1)*(j+1)
            # Check if prod is a perfect square
            if int(prod**0.5)**2 == prod:
                forbidden[i][j] = True

    # We'll try all possible assignments in lexicographical order using backtracking
    # But since n <= 40 and stages are only 3 options, brute-force is not feasible
    # However, since stages are only 3, we can model this as a graph coloring problem
    # where the "colors" are stages and adjacent nodes must not have stages whose product is a square.
    
    # Let's model the constraints:
    # Forbidden pairs: (1,1), (2,2), (3,3), (1,4) but 4 is not a stage
    # Actually stages are 1,2,3
    # 1*1=1 = 1^2 -> forbidden
    # 2*2=4 = 2^2 -> forbidden
    # 3*3=9 = 3^2 -> forbidden
    # 1*2=2, 1*3=3, 2*3=6 -> not squares -> allowed
    
    # So two nodes connected by an edge cannot have the same stage.
    # This is exactly graph coloring with 3 colors where adjacent nodes must have different colors.
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # We need to 3-color the graph such that no two adjacent nodes have the same color
    # This is the classic graph coloring problem.
    
    # Use backtracking with early termination to find the lexicographically smallest coloring
    color = [-1] * n  # -1 means unassigned
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        for c in range(1, 4):  # stages 1, 2, 3
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    main()