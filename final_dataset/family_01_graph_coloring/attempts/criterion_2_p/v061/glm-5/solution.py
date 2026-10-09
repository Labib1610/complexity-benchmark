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
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # We want the lexicographically smallest assignment.
    # Since values are 1 or 2, we prefer 1.
    # We process components in order of smallest vertex index.
    # For each component, we try to assign the smallest vertex 1.
    # If that fails (odd cycle), we try assigning it 2.
    # If that also fails, it's impossible.
    
    color = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Found a new component, start BFS
            queue = [i]
            color[i] = 1 # Tentatively assign 1
            
            # We need to check if assigning 1 to i is valid.
            # It is valid if the component is bipartite.
            # If not, we flip all colors in the component.
            # If still not bipartite, answer is NO.
            
            # To manage this, we collect all nodes in the component
            # during the BFS.
            component_nodes = []
            is_bipartite = True
            
            # BFS queue pointer
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                component_nodes.append(u)
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
            
            if not is_bipartite:
                # Try flipping colors
                for node in component_nodes:
                    color[node] = 3 - color[node]
                
                # Check bipartiteness again
                # Since we just flipped, we can just check edges
                # or re-verify. Re-verifying is safer/cleaner.
                is_bipartite_flipped = True
                for u_check in component_nodes:
                    for v_check in adj[u_check]:
                        if color[u_check] == color[v_check]:
                            is_bipartite_flipped = False
                            break
                    if not is_bipartite_flipped:
                        break
                
                if not is_bipartite_flipped:
                    possible = False
                    break
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(*(color[1:n+1]))

if __name__ == '__main__':
    solve()