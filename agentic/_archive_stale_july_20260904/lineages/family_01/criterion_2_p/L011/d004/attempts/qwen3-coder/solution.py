import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    graph = defaultdict(list)
    
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # There are only two functions:
    # f1: identity (1->1, 2->2)  => x_i = f_i(1) = 1
    # f2: flip    (1->2, 2->1)  => x_i = f_i(1) = 2
    
    # For constraint f_u(f_v(1)) = 2:
    # If x_v = 1 (f_v is identity), then f_u(1) = 2 => x_u = 2
    # If x_v = 2 (f_v is flip),    then f_u(2) = 2 => f_u must be identity => x_u = 1
    
    # So for each edge (u,v), we have:
    # x_v = 1 => x_u = 2
    # x_v = 2 => x_u = 1
    # This is equivalent to x_u = 3 - x_v
    
    # This means in each connected component, if we fix one node's value,
    # all others are determined.
    
    # We can model this as a 2-SAT problem or bipartite checking.
    # Let's use graph coloring: each edge (u,v) requires x_u != x_v
    # But wait, let's re-examine the constraint.
    
    # f_u(f_v(1)) = 2
    # If f_v(1) = 1, then f_u(1) = 2 => x_u = 2
    # If f_v(1) = 2, then f_u(2) = 2 => f_u is identity => x_u = 1
    # So if x_v = 1, then x_u = 2
    #    if x_v = 2, then x_u = 1
    # This means x_u = 3 - x_v
    
    # So for every edge, the two endpoints must have different x values.
    # But not just different -- specifically, x_u = 3 - x_v
    # This is like a bipartite graph with specific assignment.
    
    # For each connected component, we can do a BFS/DFS.
    # Start with a node, assign it 1, then all neighbors must be 2,
    # their neighbors must be 1, etc.
    # If we ever try to assign a value different from what it already has, it's impossible.
    
    # To get lexicographically smallest, we process nodes in order 0 to n-1
    # and for each unvisited node, we assign it 1 (to minimize lex order).
    
    color = [-1] * n  # -1: unvisited, 1: color 1, 2: color 2
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            # Assign color 1 to get lex smallest
            queue = deque()
            queue.append(i)
            color[i] = 1
            visited[i] = True
            
            while queue:
                u = queue.popleft()
                c = color[u]
                for v in graph[u]:
                    if not visited[v]:
                        color[v] = 3 - c
                        visited[v] = True
                        queue.append(v)
                    else:
                        if color[v] != 3 - c:
                            print("NO")
                            return
    
    # If we reach here, a valid assignment exists
    print("YES")
    print(' '.join(str(color[i]) for i in range(n)))

if __name__ == "__main__":
    main()