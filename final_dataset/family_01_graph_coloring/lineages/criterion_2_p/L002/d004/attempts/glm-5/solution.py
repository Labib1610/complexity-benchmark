import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # For each node: 0 = unassigned, 1 = tier 1, 2 = tier 2
    assignment = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if assignment[start] != 0:
            continue
        
        # BFS to find connected component and check bipartiteness
        # We want lexicographically smallest, so try to assign tier 1 first
        queue = deque()
        queue.append(start)
        assignment[start] = 1
        component = [start]
        is_bipartite = True
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if assignment[v] == 0:
                    assignment[v] = 3 - assignment[u]  # 1->2, 2->1
                    queue.append(v)
                    component.append(v)
                elif assignment[v] == assignment[u]:
                    is_bipartite = False
        
        if not is_bipartite:
            print("NO")
            return
        
        # Check if we can flip the component to get lexicographically smaller
        # We need to check if flipping gives valid assignment
        # Flipping is valid if the component is bipartite (which we verified)
        # Compare current assignment vs flipped assignment for this component
        # We want the lexicographically smallest overall assignment
        
        # Current assignment for component
        # Flipped assignment: 1->2, 2->1
        # Compare lexicographically
        should_flip = False
        for node in component:
            if assignment[node] == 1:
                # Current is 1, flipped would be 2, so current is better
                break
            elif assignment[node] == 2:
                # Current is 2, flipped would be 1, so flipped is better
                should_flip = True
                break
        
        if should_flip:
            for node in component:
                assignment[node] = 3 - assignment[node]
    
    print("YES")
    print(' '.join(str(assignment[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()