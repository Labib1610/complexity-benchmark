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

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # We need to check if the graph is bipartite.
    # If it is, we can assign values such that all edges are "good" (contribute 2.5).
    # If not, no assignment works.
    
    color = [-1] * n
    possible = True
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            queue = deque([i])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break

    if not possible:
        print("NO")
    else:
        print("YES")
        # The problem asks for the lexicographically smallest sequence.
        # Since 1 < 2, we want to maximize the number of 1s.
        # In a connected component, we can swap all 0s with 1s and vice versa.
        # We want to choose the assignment that has more 0s (mapped to 1).
        # If counts are equal, either works (lexicographically same count of 1s).
        
        # We need to track components to decide which coloring variant to use.
        visited_comp = [False] * n
        final_assignment = [0] * n
        
        for i in range(n):
            if not visited_comp[i]:
                # Find all nodes in this component
                component_nodes = []
                queue = deque([i])
                visited_comp[i] = True
                while queue:
                    u = queue.popleft()
                    component_nodes.append(u)
                    for v in adj[u]:
                        if not visited_comp[v]:
                            visited_comp[v] = True
                            queue.append(v)
                
                # Count nodes with color 0 and color 1 in this component
                count0 = 0
                count1 = 0
                for node in component_nodes:
                    if color[node] == 0:
                        count0 += 1
                    else:
                        count1 += 1
                
                # We want to maximize 1s in the output.
                # color 0 -> value 1
                # color 1 -> value 2
                # So if count0 >= count1, we keep the current mapping.
                # If count0 < count1, we flip: color 0 -> 2, color 1 -> 1.
                
                if count0 >= count1:
                    # Use current colors: 0->1, 1->2
                    for node in component_nodes:
                        final_assignment[node] = color[node] + 1
                else:
                    # Flip colors: 0->2, 1->1
                    for node in component_nodes:
                        final_assignment[node] = 2 - color[node]
                        
        print(*(final_assignment))

if __name__ == '__main__':
    solve()