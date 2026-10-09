import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # The condition for a tether to be balanced:
    # For nodes u and v with values s_u and s_v (either 1 or 2):
    # (s_u XOR s_v) > (s_u AND s_v)
    # Let's compute this for all pairs in {1,2}:
    # 1 XOR 1 = 0, 1 AND 1 = 1 => 0 > 1? No
    # 1 XOR 2 = 3, 1 AND 2 = 0 => 3 > 0? Yes
    # 2 XOR 1 = 3, 2 AND 1 = 0 => 3 > 0? Yes
    # 2 XOR 2 = 0, 2 AND 2 = 2 => 0 > 2? No
    # So the only allowed pairs are (1,2) and (2,1). That means adjacent nodes must have different values.
    # This is a classic 2-coloring (bipartite check) problem.
    
    # We need to check if the graph is bipartite.
    # If it is, we assign colors such that the sequence is lexicographically smallest.
    # Color 0 will represent value 1, Color 1 will represent value 2.
    
    color = [-1] * (n + 1)
    result = [0] * (n + 1)  # 0 means unassigned, 1 and 2 are the values
    
    # Check each component
    for start in range(1, n + 1):
        if color[start] == -1:
            # BFS to color the component
            queue = deque()
            queue.append(start)
            color[start] = 0
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # If bipartite, construct the lexicographically smallest assignment
    # For each node, we prefer 1 over 2 if possible.
    # Since color 0 -> value 1, color 1 -> value 2,
    # and we want lexicographically smallest, we should try to assign color 0 to early nodes.
    # But actually, since we're just assigning based on the bipartition,
    # and we want the lex smallest sequence, we can just go in order from 1 to n.
    # For each node, if it's color 0, assign 1; if color 1, assign 2.
    # But wait, we might have freedom in how we assign the initial color.
    # In our BFS, we started with color 0 for the first node in each component.
    # To get the lex smallest, we should decide for each component whether to flip the coloring.
    
    # Let's re-do the coloring with optimization for lex smallest.
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if not visited[start]:
            # Collect all nodes in this component
            component = []
            queue = deque()
            queue.append(start)
            visited[start] = True
            component.append(start)
            color[start] = 0
            
            bipartite = True
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        component.append(v)
                        color[v] = color[u] ^ 1
                        queue.append(v)
                    elif color[v] == color[u]:
                        bipartite = False
            
            if not bipartite:
                print("NO")
                return
                
    # Now assign values to minimize lexicographical order
    # For each component, we can choose which color gets value 1.
    # To make the sequence as small as possible, for the first node in the natural order,
    # we should give it value 1 if possible.
    # Actually, let's think differently.
    # The coloring is fixed up to flipping entire components.
    # For each component, we can choose whether to map color 0 -> 1, color 1 -> 2 (don't flip)
    # or color 0 -> 2, color 1 -> 1 (flip).
    # To get lex smallest, for the first node in the component, we want it to be 1.
    # So if its color is 0, don't flip. If its color is 1, flip.
    
    # But in our current coloring, we started each component with color 0.
    # So node with color 0 should get value 1.
    # This already gives us what we want for lex smallest.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            result[i] = 1
        else:
            result[i] = 2
            
    print("YES")
    print(' '.join(map(str, result[1:])))

if __name__ == "__main__":
    main()