import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1
    
    # Kahn's algorithm to get topological order and detect cycles
    q = deque([i for i in range(1, n + 1) if indeg[i] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(topo) != n:
        print("NO")
        return
    
    # earliest term for each module based on prerequisites
    earliest = [1] * (n + 1)
    for u in topo:
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
    
    # Check if any earliest term exceeds T
    if max(earliest[1:]) > T:
        print("NO")
        return
    
    # Now assign terms greedily: process modules in topological order,
    # assign the smallest possible term >= earliest[u] that has capacity.
    # We'll keep track of how many modules assigned to each term.

    term_count = [0] * (T + 1)
    assignment = [0] * (n + 1)
    
    # To assign efficiently, we can use a DSU "next available term" structure.
    # parent[t] = next term to try if term t is full.

    parent = list(range(T + 2))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    for u in topo:
        # find the smallest term >= earliest[u] that has capacity
        t = find(earliest[u])
        if t > T:
            print("NO")
            return
        assignment[u] = t
        term_count[t] += 1
        if term_count[t] == M:
            # this term is now full, so union it with t+1
            parent[t] = find(t + 1)
    
    # After assignment, verify all prerequisites and capacity (should hold)
    for a in range(1, n + 1):
        for b in adj[a]:
            if assignment[a] >= assignment[b]:
                print("NO")
                return
    
    out = ["YES"] + [str(assignment[i]) for i in range(1, n + 1)]
    sys.stdout.write(" ".join(out))

if __name__ == "__main__":
    solve()