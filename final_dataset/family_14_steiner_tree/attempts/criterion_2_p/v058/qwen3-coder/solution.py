import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    terminals = set()
    for _ in range(t):
        terminals.add(int(data[idx]))
        idx += 1
    
    # If there's only one terminal, no edges are needed
    if t <= 1:
        print(0)
        return
    
    # Build the tree
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Find the minimal subtree that connects all terminals
    # This is the Steiner tree problem on a tree, which can be solved by:
    # 1. Finding the subtree that contains all terminals
    # 2. The minimal way is to take the edges in the paths between all pairs of terminals
    # But on a tree, the minimal connected subgraph containing all terminals is the union of paths between them
    # Which is equivalent to: take the minimal subtree that contains all terminals
    
    # A simpler approach for tree: 
    # The answer is the sum of weights of edges in the minimal subtree containing all terminals
    # Algorithm:
    # 1. Root the tree at any node
    # 2. For each node, compute if it's needed (contains terminal or has needed children)
    # 3. Count edges accordingly
    
    # Let's root the tree at node 1
    parent = [-1] * (n + 1)
    children = defaultdict(list)
    edge_weight = {}
    
    # BFS to build rooted tree
    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                edge_weight[(u, v)] = w
                edge_weight[(v, u)] = w
                queue.append(v)
    
    # Now, for each node, determine if it's "needed"
    # A node is needed if:
    # - It contains a terminal, OR
    # - It has at least one needed child
    
    needed = [False] * (n + 1)
    # Mark terminals as needed
    for term in terminals:
        needed[term] = True
    
    # Post-order traversal to propagate needed status upwards
    def dfs(u):
        for v in children[u]:
            dfs(v)
            if needed[v]:
                needed[u] = True
    
    dfs(1)
    
    # Now, count the total weight of edges connecting needed nodes
    # An edge (u,v) where u is parent of v is included if v is needed
    total = 0
    for u in range(1, n + 1):
        for v in children[u]:
            if needed[v]:
                total += edge_weight[(u, v)]
    
    print(total)

if __name__ == "__main__":
    main()