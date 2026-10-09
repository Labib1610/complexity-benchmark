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
    
    essential = set()
    for _ in range(t):
        essential.add(int(data[idx]))
        idx += 1
        
    edges = []
    graph = defaultdict(list)
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((u,v,w))
        graph[u].append((v,w))
        graph[v].append((u,w))
        
    # If there's only one or zero essential node, cost is 0
    if len(essential) <= 1:
        print(0)
        return
        
    # Since the graph is a tree (m = n-1 and connected), we can find the minimal subtree
    # that connects all essential nodes. This is the Steiner tree problem on a tree.
    # We can solve this efficiently by doing a DFS and computing the minimal cost
    # to connect all essential nodes in each subtree.
    
    # Root the tree arbitrarily, say at node 1
    root = 1
    
    # Build parent/children relationships via BFS
    parent = [-1] * (n+1)
    children = defaultdict(list)
    visited = [False] * (n+1)
    queue = deque([root])
    visited[root] = True
    
    while queue:
        u = queue.popleft()
        for v, w in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append((v,w))
                queue.append(v)
                
    # For each node, we compute:
    # - whether the subtree contains any essential node
    # - the minimal cost to connect all essential nodes in this subtree
    # This is done via a post-order traversal (DFS)
    
    # To avoid recursion depth issues, we'll do iterative post-order DFS
    # We need a stack that also tells us when we're returning from a node
    
    # First, build a post-order traversal
    stack = [root]
    order = []
    visited_dfs = [False] * (n+1)
    
    while stack:
        u = stack.pop()
        if visited_dfs[u]:
            continue
        visited_dfs[u] = True
        order.append(u)
        for v, w in children[u]:
            if not visited_dfs[v]:
                stack.append(v)
                
    order.reverse()  # Now it's post-order
    
    # Now process in post-order
    # For each node v, store:
    # has_essential[v]: whether subtree of v contains any essential node
    # min_cost[v]: minimal cost to connect all essential nodes in subtree of v
    has_essential = [False] * (n+1)
    min_cost = [0] * (n+1)
    
    # Initialize leaves
    for u in order:
        if u in essential:
            has_essential[u] = True
            
    # Process each node in post-order
    for u in order:
        # For each child, if the child's subtree has essential nodes,
        # we must include the edge to that child
        cost = 0
        has = has_essential[u]
        for v, w in children[u]:
            if has_essential[v]:
                cost += min_cost[v] + w
                has = True
        min_cost[u] = cost
        has_essential[u] = has
        
    print(min_cost[root])

if __name__ == "__main__":
    main()