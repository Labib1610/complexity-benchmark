import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    k = int(data[idx])
    idx += 1
    
    # Build adjacency list
    adj = defaultdict(set)
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        adj[u].add(v)
        adj[v].add(u)
    
    # The key insight is that the graph is bipartite (since all cycles are even)
    # So we can color it with two colors and pick the larger color class
    # If the larger class has >= k nodes, we can select k from it
    
    color = {}
    visited = set()
    
    # Check if the graph is bipartite and get the color classes
    def bfs(start):
        queue = [start]
        color[start] = 0
        visited.add(start)
        c0 = 1
        c1 = 0
        while queue:
            u = queue.pop(0)
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    color[v] = 1 - color[u]
                    if color[v] == 0:
                        c0 += 1
                    else:
                        c1 += 1
                    queue.append(v)
                elif color[v] == color[u]:
                    # This should not happen due to problem constraints
                    return -1, -1
        return c0, c1
    
    # If m == 0, graph has no edges, so any k nodes work
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, min(k+1, n+1)))))
        return
    
    # Find all components and their color classes
    color_classes = []
    for i in range(1, n+1):
        if i not in visited:
            c0, c1 = bfs(i)
            if c0 == -1:
                # Should not happen due to constraints
                print("NO")
                return
            color_classes.append((c0, c1))
    
    # For each component, we can take either color class
    # We want to maximize the total number of nodes we can take
    # But since we just need k nodes, we check if it's possible
    
    # Actually, since it's bipartite, we can take the maximum of the two color classes
    # from each component, but we need to be careful about how many we take from each
    
    # Simpler approach: collect all nodes of each color globally
    color0_nodes = []
    color1_nodes = []
    
    for node in range(1, n+1):
        if node in color:
            if color[node] == 0:
                color0_nodes.append(node)
            else:
                color1_nodes.append(node)
        else:
            # Isolated node, can assign to any color, let's put in color0
            color0_nodes.append(node)
    
    # Now we have two independent sets: color0_nodes and color1_nodes
    # Take the larger one, see if we can get k nodes
    if len(color0_nodes) >= k:
        print("YES")
        print(' '.join(map(str, color0_nodes[:k])))
        return
    elif len(color1_nodes) >= k:
        print("YES")
        print(' '.join(map(str, color1_nodes[:k])))
        return
    else:
        print("NO")

if __name__ == "__main__":
    main()