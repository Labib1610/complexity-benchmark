import sys
from collections import defaultdict, deque

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # First, check if every edge satisfies the trace condition
    # A1 = [[1,2],[0,1]], A2 = [[1,0],[2,1]]
    # We need trace(A_s_u * A_s_v) = 6
    
    # Let's compute all possible traces:
    # A1 * A1 = [[1,2],[0,1]] * [[1,2],[0,1]] = [[1,4],[0,1]] -> trace = 2
    # A1 * A2 = [[1,2],[0,1]] * [[1,0],[2,1]] = [[5,2],[2,1]] -> trace = 6
    # A2 * A1 = [[1,0],[2,1]] * [[1,2],[0,1]] = [[1,2],[2,5]] -> trace = 6
    # A2 * A2 = [[1,0],[2,1]] * [[1,0],[2,1]] = [[1,0],[4,1]] -> trace = 2
    
    # So two nodes can be connected only if they have different shift codes.
    # This is a bipartite graph check.
    
    color = [-1] * (n + 1)
    visited = [False] * (n + 1)
    
    def is_bipartite():
        for start in range(1, n + 1):
            if not visited[start]:
                queue = deque([start])
                color[start] = 0
                visited[start] = True
                while queue:
                    u = queue.popleft()
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            color[v] = 1 - color[u]
                            queue.append(v)
                        elif color[v] == color[u]:
                            return False
        return True
    
    if not is_bipartite():
        print("NO")
        return
    
    # Now we need to check the harmonic buildup condition:
    # In every simple cycle, # of 1's = # of 2's.
    # Since the graph is bipartite, all cycles are of even length.
    # For this to hold, every cycle must have equal number from both parts.
    # This is true if and only if every connected component is bipartite and 
    # the two parts have equal size.
    
    visited_check = [False] * (n + 1)
    
    def check_balanced_bipartition():
        for start in range(1, n + 1):
            if not visited_check[start]:
                part0 = []
                part1 = []
                queue = deque([start])
                color[start] = 0
                visited_check[start] = True
                part0.append(start)
                
                while queue:
                    u = queue.popleft()
                    for v in adj[u]:
                        if not visited_check[v]:
                            visited_check[v] = True
                            color[v] = 1 - color[u]
                            if color[v] == 0:
                                part0.append(v)
                            else:
                                part1.append(v)
                            queue.append(v)
                        # Since we already checked bipartition, no conflicts here
                        
                if len(part0) != len(part1):
                    return False
        return True
    
    # We need to re-do the bipartition check with size tracking
    color = [-1] * (n + 1)
    visited_check = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if not visited_check[start]:
            part0 = []
            part1 = []
            queue = deque([start])
            color[start] = 0
            visited_check[start] = True
            part0.append(start)
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited_check[v]:
                        visited_check[v] = True
                        color[v] = 1 - color[u]
                        if color[v] == 0:
                            part0.append(v)
                        else:
                            part1.append(v)
                        queue.append(v)
                    # Since we already know it's bipartite, no need to check conflict
            
            if len(part0) != len(part1):
                print("NO")
                return
    
    # If we reach here, a valid assignment exists.
    # Assign shift codes based on the bipartition.
    # To minimize structural weight, we want smaller values (1) towards the beginning.
    # So we should assign 1 to the nodes that would appear earlier in the sequence.
    # But since we want a valid assignment, we just need to follow the bipartition.
    # Let's assign 1 to color 0 and 2 to color 1.
    
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 0:
            assignment[i] = 1
        else:
            assignment[i] = 2
    
    print("YES")
    print(" ".join(map(str, assignment[1:])))

solve()