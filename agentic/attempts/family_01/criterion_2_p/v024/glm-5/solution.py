import sys
from sys import setrecursionlimit

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
    
    color = [0] * (n + 1)
    NO = False
    
    for start in range(1, n + 1):
        if color[start] == 0:
            stack = [start]
            color[start] = 1
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        NO = True
                        break
                if NO:
                    break
        if NO:
            break
    
    if NO:
        sys.stdout.write("NO\n")
        return
    
    # Check if graph is bipartite with all edges crossing (i.e., no isolated vertices with choice)
    # Actually we need lexicographically smallest. For each vertex, if it's isolated (no edges),
    # we can set it to 1. But if it's connected, its color is forced by the component.
    # However, the initial coloring might not be lexicographically smallest because we can
    # flip entire components. We need to choose for each component whether to flip or not
    # to get lexicographically smallest sequence.
    
    # But wait: the problem says "lexicographically smallest sequence of channel assignments".
    # For each connected component, we have two possible colorings (original or flipped).
    # We need to choose for each component to minimize the overall sequence lexicographically.
    # Since components are processed in order of vertices, and we want lexicographically smallest,
    # we should process vertices from 1 to n, and for each unvisited vertex, try to assign 1
    # if possible (i.e., if flipping the component to make this vertex 1 doesn't conflict with
    # already fixed vertices). But since components are independent, we can decide per component.
    
    # Actually, the greedy approach: process vertices 1..n. For each unassigned vertex,
    # we want it to be 1. We do BFS/DFS to assign colors, starting with 1 for this vertex.
    # If we encounter a conflict (a neighbor already has the same color), we cannot use 1
    # for this vertex, so we must use 2. But wait, if the component is already partially
    # colored, we need to respect that.
    
    # Let me redo the coloring with lexicographic minimality in mind.
    color = [0] * (n + 1)
    NO = False
    
    for start in range(1, n + 1):
        if color[start] == 0:
            # Try to assign 1 to start
            # But we need to check if this is possible given already colored neighbors
            # Actually, if start is uncolored, all its neighbors are uncolored too
            # (since if a neighbor was colored, start would be colored too in BFS)
            # Wait, no. The graph might have multiple components, and we process in order.
            # So if start is uncolored, its entire component is uncolored.
            # So we can freely choose the coloring for this component.
            # To get lexicographically smallest, we want start to be 1.
            stack = [start]
            color[start] = 1
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        NO = True
                        break
                if NO:
                    break
        if NO:
            break
    
    if NO:
        sys.stdout.write("NO\n")
        return
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(color[i]) for i in range(1, n + 1)) + "\n")

solve()