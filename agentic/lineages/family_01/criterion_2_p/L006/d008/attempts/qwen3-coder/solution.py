import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Analyze the constraint: 2pu² - 5pu*pv + 2pv² = 0
    # This can be factored as: (2pu - pv)(pu - 2pv) = 0
    # So either pu = 2pv or 2pu = pv
    # Since pu, pv ∈ {1,2}, the valid pairs are:
    # (1,2): 2*1 = 2 ✓
    # (2,1): 1 = 2*1 ✓
    # (1,1): 2*1 ≠ 1 and 1 ≠ 2*1 ✗
    # (2,2): 2*2 ≠ 2 and 2 ≠ 2*2 ✗
    # So adjacent nodes must have different values: one 1, one 2
    
    # This is a bipartite graph check
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    
    # Check if bipartite using BFS for each component
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
            
        queue = deque([start])
        color[start] = 1
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    color[neighbor] = 3 - current_color  # Flip color (1->2, 2->1)
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    print("NO")
                    return
    
    # If we reach here, a valid assignment exists
    # We want the lexicographically smallest assignment
    # That means we prefer color 1 over color 2 for earlier nodes
    # Our coloring already ensures this since we start with color 1
    
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:  # Isolated node, assign 1 (lexicographically smallest)
            result.append("1")
        else:
            result.append(str(color[i]))
    
    print("YES")
    print(" ".join(result))

solve()