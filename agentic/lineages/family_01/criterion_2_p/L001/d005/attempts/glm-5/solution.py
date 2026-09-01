import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    degrees = [0] * (n + 1)
    
    edges = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
        edges.append((u, v))

    # Check if the graph is bipartite using BFS
    color = [0] * (n + 1)
    is_bipartite = True
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            queue = deque([i])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break

    if not is_bipartite:
        print("NO")
        return

    # If bipartite, we need to find the lexicographically smallest valid configuration.
    # Valid configurations are exactly the proper 2-colorings.
    # Lexicographically smallest means we want to assign 1 to the smallest indexed monomers possible.
    # This is equivalent to finding the lexicographically smallest proper coloring.
    
    # We use a greedy approach with a priority queue (min-heap).
    # We assign colors to monomers in increasing order of index.
    # For the current monomer, we try to assign color 1 if possible, else color 2.
    # A color is possible if no already-colored neighbor has that color.
    
    final_colors = [0] * (n + 1)
    # Min-heap stores monomers to be colored, prioritized by index.
    # We push all monomers initially, but we can also push as we discover.
    # However, since we must process in order 1 to n, a simple loop is better.
    
    # Let's stick to the loop 1 to n.
    # For each monomer i, check neighbors j < i.
    # If any neighbor j has final_colors[j] == 1, i cannot be 1.
    # If any neighbor j has final_colors[j] == 2, i cannot be 2.
    # Since the graph is bipartite, it's impossible for i to have neighbors with both 1 and 2
    # (that would imply an odd cycle).
    # So i will have either:
    # 1. No colored neighbors -> assign 1.
    # 2. Neighbors with color 1 -> assign 2.
    # 3. Neighbors with color 2 -> assign 1.
    # This greedy strategy works because:
    # - If we assign 1, we satisfy the "smallest lexicographical" preference.
    # - If we assign 2, it's because 1 was forbidden by a smaller index neighbor.
    #   Any valid coloring must respect the constraint from that neighbor.
    # - Bipartiteness ensures we never get stuck (no conflict from two smaller neighbors).
    
    for i in range(1, n + 1):
        # Check colors of neighbors with index < i
        # Since we only need to know if color 1 or 2 is taken, we can check.
        # Optimization: only check neighbors. 
        # In dense graphs, degree sum is large, but total work is O(M).
        has_1_neighbor = False
        has_2_neighbor = False
        for neighbor in adj[i]:
            if neighbor < i:
                if final_colors[neighbor] == 1:
                    has_1_neighbor = True
                elif final_colors[neighbor] == 2:
                    has_2_neighbor = True
        
        if has_1_neighbor and has_2_neighbor:
            # This case implies an odd cycle involving i and smaller nodes.
            # But we already checked bipartiteness, so this should not happen.
            print("NO")
            return
        
        if has_1_neighbor:
            final_colors[i] = 2
        else:
            final_colors[i] = 1
            
    # Verify the solution (optional but safe)
    # The problem asks for a valid configuration.
    # With the greedy strategy on a bipartite graph, the result is always a valid coloring.
    # The sum of squared differences will be m.
    
    print("YES")
    print(*(final_colors[1:]))

if __name__ == '__main__':
    solve()