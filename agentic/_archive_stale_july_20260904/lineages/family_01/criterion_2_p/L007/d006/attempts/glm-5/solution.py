import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # We need sum of ||v_u x v_v||^2 = 75m
    # For c=1: v=(1,2,3), c=2: v=(3,1,2)
    # ||v1 x v1||^2 = 0
    # ||v2 x v2||^2 = 0
    # ||v1 x v2||^2 = ||v2 x v1||^2 = 75
    # So we need exactly m edges with different grades
    
    color = [-1] * n
    possible = True
    
    for i in range(n):
        if color[i] == -1:
            # BFS from this component
            queue = [i]
            color[i] = 0
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
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
        return
    
    # Check if the coloring gives exactly m cross edges
    cross_count = 0
    for u in range(n):
        for v in adj[u]:
            if v > u:  # count each edge once
                if color[u] != color[v]:
                    cross_count += 1
    
    if cross_count == m:
        # Output the coloring (0 -> grade 1, 1 -> grade 2)
        result = [1 if c == 0 else 2 for c in color]
        print("YES")
        print(' '.join(map(str, result)))
    elif cross_count == 0:
        # All same color, need to flip some
        # Find a node with minimum degree to flip
        min_deg = n + 1
        flip_node = -1
        for i in range(n):
            deg = len(adj[i])
            if deg < min_deg:
                min_deg = deg
                flip_node = i
        
        # Flip the component containing flip_node
        # Find all nodes in that component
        comp = []
        visited = [False] * n
        stack = [flip_node]
        visited[flip_node] = True
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        
        # Flip colors in this component
        for node in comp:
            color[node] = 1 - color[node]
        
        result = [1 if c == 0 else 2 for c in color]
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()