import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    nL = int(data[0])
    nR = int(data[1])
    m = int(data[2])
    
    edges = []
    adj = defaultdict(list)
    
    index = 3
    for i in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        index += 2
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v + nL].append((u, i))
    
    # Calculate degrees
    deg = [0] * (nL + nR)
    for u, v in edges:
        deg[u] += 1
        deg[v + nL] += 1
    
    delta = max(deg) if deg else 0
    
    if delta == 0:
        print("YES")
        return
    
    # Color edges
    result = [0] * m
    used_colors = [set() for _ in range(nL + nR)]
    free_color = [list(range(1, delta + 1)) for _ in range(nL + nR)]
    
    for u, v in edges:
        v_idx = v + nL
        color = None
        # Find a free color
        for c in free_color[u]:
            if c not in used_colors[v_idx]:
                color = c
                break
        
        if color is None:
            # This shouldn't happen due to König's theorem
            color = 1
            
        result[edges.index((u, v))] = color
        used_colors[u].add(color)
        used_colors[v_idx].add(color)
        
        # Remove color from free lists
        if color in free_color[u]:
            free_color[u].remove(color)
        if color in free_color[v_idx]:
            free_color[v_idx].remove(color)
    
    # More robust approach using BFS coloring
    result = [0] * m
    used = [set() for _ in range(nL + nR)]
    
    # For each node, keep track of available colors
    available = [set(range(1, delta + 1)) for _ in range(nL + nR)]
    
    # Process edges
    for i, (u, v) in enumerate(edges):
        v_idx = v + nL
        # Find a color that is not used by either u or v
        color = None
        for c in available[u]:
            if c not in used[v_idx]:
                color = c
                break
                
        if color is None:
            # Find any available color
            for c in range(1, delta + 1):
                if c not in used[u] and c not in used[v_idx]:
                    color = c
                    break
                    
        result[i] = color
        used[u].add(color)
        used[v_idx].add(color)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()