import sys
from collections import deque, defaultdict

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        indeg[b] += 1
    
    # Kahn's algorithm with capacity constraint
    # We'll assign phases greedily: process nodes in topological order,
    # but at each phase we can only schedule up to M nodes whose dependencies are satisfied.
    
    phase = [0] * n
    ready = []
    # ready will store (earliest_possible_phase, node)
    # We'll use a min-heap by earliest possible phase, but since we process phase by phase,
    # we can just keep a queue of ready nodes.
    
    # Initialize ready nodes (indeg 0)
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    current_phase = 1
    scheduled = 0
    
    # We'll process in phases
    while scheduled < n:
        if current_phase > T:
            print("NO")
            return
        
        # Nodes we can schedule in this phase
        can_schedule = []
        # Take up to M nodes from q
        count = 0
        temp = deque()
        while q and count < M:
            u = q.popleft()
            phase[u] = current_phase
            scheduled += 1
            count += 1
            # After scheduling u, reduce indegree of its neighbors
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    temp.append(v)
        # If we couldn't schedule any node this phase, it's a deadlock
        if count == 0:
            print("NO")
            return
        # Move newly ready nodes to q for next phases
        q.extend(temp)
        current_phase += 1
    
    # Check if all phases <= T
    if max(phase) > T:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(p) for p in phase))

if __name__ == "__main__":
    solve()