from collections import defaultdict, deque
import sys

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
    adj = [[] for _ in range(n+1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # We need to assign values from {1,2,3} to each node such that for every edge (u,v):
    # (c_u + 2*c_v) mod 3 != 0
    # Since the formula is symmetric in the sense that (c_u + 2*c_v) mod 3 = 0 iff (c_v + 2*c_u) mod 3 = 0,
    # we can treat this as an undirected graph constraint.
    
    # Let's analyze when (a + 2*b) mod 3 = 0 for a,b in {1,2,3}
    # All combinations:
    # (1,1): 1+2=3 -> 0
    # (1,2): 1+4=5 -> 2
    # (1,3): 1+6=7 -> 1
    # (2,1): 2+2=4 -> 1
    # (2,2): 2+4=6 -> 0
    # (2,3): 2+6=8 -> 2
    # (3,1): 3+2=5 -> 2
    # (3,2): 3+4=7 -> 1
    # (3,3): 3+6=9 -> 0
    # So forbidden pairs are: (1,1), (2,2), (3,3)
    # That means adjacent nodes cannot have the same value.
    # This is a graph 3-coloring problem where colors are 1,2,3.
    
    # Build adjacency list
    graph = [[] for _ in range(n+1)]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Try all assignments using backtracking with early termination for lex smallest
    # But since n<=40, full backtrack may be too slow.
    # However, since it's a 3-coloring problem, and constraints might make it tractable,
    # let's try a greedy approach with backtracking optimized for lex order.
    
    # Use a more efficient approach: since we want the lex smallest, we can use BFS/DFS
    # with state: (current node, current assignment)
    # But even better: model this as a 3-coloring problem with constraint propagation.
    
    # Let's implement a backtracking solution with pruning and lex order.
    color = [0] * (n+1)  # 0 means unassigned
    
    def is_valid(u, c):
        for v in graph[u]:
            if color[v] == c:
                return False
        return True
    
    def solve(node):
        if node > n:
            return True
        for c in [1,2,3]:
            if is_valid(node, c):
                color[node] = c
                if solve(node+1):
                    return True
                color[node] = 0
        return False
    
    # Check if solution exists
    if solve(1):
        print("YES")
        print(' '.join(map(str, color[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    main()