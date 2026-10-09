import sys
from collections import defaultdict, deque

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
    
    # For each edge (u,v), I_u ∪ I_v must have length exactly 2
    # The intervals are [0,1] (right endpoint 1) and [1,2] (right endpoint 2)
    # Union possibilities:
    # [0,1] ∪ [1,2] = [0,2] (length 2)  -> valid
    # [0,1] ∪ [0,1] = [0,1] (length 1)  -> invalid
    # [1,2] ∪ [1,2] = [1,2] (length 1)  -> invalid
    # So u and v must have different assignments
    
    # This is a 2-coloring (bipartite) problem
    # Color 0 represents right endpoint 1 ([0,1])
    # Color 1 represents right endpoint 2 ([1,2])
    
    color = [-1] * (n + 1)
    
    # Check if the graph is bipartite
    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # If bipartite, construct the lexicographically smallest solution
    # We want to minimize the sequence of right endpoints
    # Right endpoint is 1 if color is 0, 2 if color is 1
    # To get lex smallest, we should try to assign color 0 (right endpt 1) as much as possible,
    # starting from node 1 onwards.
    # But since the coloring is already determined by components, we just use the coloring.
    # The coloring we did ensures that within each component, the assignment is consistent.
    # To make it lex smallest overall, when we first color a component, we should choose
    # the color of the first node in that component to be 0 if possible.
    # However, our BFS above already starts with color 0, so it's fine.
    
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()