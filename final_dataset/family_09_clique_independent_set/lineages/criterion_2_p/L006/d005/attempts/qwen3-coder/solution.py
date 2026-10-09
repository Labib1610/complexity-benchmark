import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, k, edges

def build_graph(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def bipartite_check(n, graph):
    # Color nodes with 0 or 1. -1 means unvisited
    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            queue = deque([i])
            color[i] = 0
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 1 - current_color
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        return None, None  # Not bipartite
    # Partition into two sets
    set0 = [i for i in range(1, n + 1) if color[i] == 0]
    set1 = [i for i in range(1, n + 1) if color[i] == 1]
    return set0, set1

def solve():
    n, m, k, edges = read_input()
    graph = build_graph(n, edges)
    
    # Check if the graph is bipartite
    set0, set1 = bipartite_check(n, graph)
    
    if set0 is None:
        # This should not happen according to problem statement
        print("NO")
        return
    
    # Try to take exactly k nodes
    # We can take nodes from either set0 or set1 since they are independent sets
    if len(set0) >= k:
        print("YES")
        print(' '.join(map(str, set0[:k])))
    elif len(set1) >= k:
        print("YES")
        print(' '.join(map(str, set1[:k])))
    else:
        # Try combining optimal selection
        # Since we want EXACTLY k, and sets are independent, 
        # we can only take from one set or the other, or check if we can take all and still have space
        # But since sets are independent, we can't combine them arbitrarily
        
        # Actually, let's think differently:
        # The maximum independent set in a bipartite graph can be found,
        # but we need exactly k nodes that form an independent set.
        
        # In a bipartite graph, the maximum independent set size is |set0| + |set1| = n
        # But we want exactly k nodes that are independent.
        
        # Since both set0 and set1 are independent sets, we can take up to min(len(set0), k) from set0
        # and up to min(len(set1), k) from set1, but we can't mix them.
        
        # Wait, that's wrong. We can take nodes from set0 OR set1, but not both together 
        # because every edge goes between set0 and set1.
        
        # So we can take at most max(|set0|, |set1|) nodes in an independent set.
        # For exactly k, we need to check if k <= max(|set0|, |set1|).
        
        # But actually, we can take any subset of set0 or set1 as long as it's independent within itself.
        # Since set0 and set1 are independent sets by definition of bipartition,
        # we just need k <= max(|set0|, |set1|). But we also need to be able to select exactly k.
        
        # Let's reframe: we can take any number of nodes from set0 (up to |set0|) 
        # and any number of nodes from set1 (up to |set1|), but no edges within each set.
        # But wait, that's not right either. The constraint is that NO two adjacent nodes can both be selected.
        # Since the graph is bipartite, set0 and set1 have no internal edges, so we can take any subset of set0
        # and any subset of set1, as long as there are no edges between selected nodes from different sets.
        # But since ALL edges go between set0 and set1, we can take nodes ONLY from set0 OR set1.
        
        # Therefore, we can select exactly k nodes if and only if k <= |set0| or k <= |set1|.
        
        if k <= len(set0):
            print("YES")
            print(' '.join(map(str, set0[:k])))
        elif k <= len(set1):
            print("YES")
            print(' '.join(map(str, set1[:k])))
        else:
            print("NO")

solve()