import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # To get lexicographically smallest assignment, we process nodes in order 0 to n-1.
    # When a node is unassigned, we tentatively assign it tier 1.
    # We then check if this creates a conflict with any already assigned neighbor.
    # If conflict, we switch to tier 2.
    # If still conflict, the assignment is impossible.
    # Since tier 1 is preferred, this greedy approach yields the lex-smallest valid assignment.
    
    tiers = [0] * n
    
    for i in range(n):
        if tiers[i] != 0:
            continue
        
        # Start BFS for the connected component containing i
        queue = deque([i])
        tiers[i] = 1
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if tiers[v] == 0:
                    # Neighbor unassigned: assign opposite tier to satisfy constraint
                    tiers[v] = 3 - tiers[u]
                    queue.append(v)
                else:
                    # Neighbor assigned: check if constraint is satisfied
                    if tiers[u] == tiers[v]:
                        print("NO")
                        return
    
    print("YES")
    print(*(tiers))

if __name__ == '__main__':
    solve()