import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # We need to 3-color the graph. We'll try all possibilities in lexicographical order.
    # Since we want the lexicographically smallest assignment, we can do backtracking DFS
    # assigning colors 1,2,3 in order and taking the first valid one.
    
    color = [0] * (n + 1)  # color[i] will be 0,1,2,3; 0 means unassigned
    
    def is_valid(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
        for c in range(1, 4):
            if is_valid(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        return False
    
    if backtrack(1):
        print("YES")
        print(" ".join(str(color[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    main()