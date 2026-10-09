import sys
from collections import defaultdict
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    try:
        line = sys.stdin.readline()
        if not line:
            print("YES")
            print()
            return
        nL, nR, m = map(int, line.split())
    except:
        print("YES")
        print()
        return
        
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        # Convert to 0-indexed
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, i))       # left node u connects to right node v via edge i
        adj[v + nL].append((u, i))  # right node v (offset by nL) connects to left node u via edge i
    
    # Determine maximum degree
    max_degree = 0
    for i in range(nL + nR):
        max_degree = max(max_degree, len(adj[i]))
    
    k = max_degree
    if k == 0:
        print("YES")
        return
    
    # Color the edges
    result = [-1] * m
    used_colors = [set() for _ in range(nL + nR)]  # For each node, which colors are used on its edges
    
    for i in range(m):
        u, v = edges[i]
        v_offset = v + nL
        
        # Find the first available color
        color = 1
        while color in used_colors[u] or color in used_colors[v_offset]:
            color += 1
        result[i] = color
        used_colors[u].add(color)
        used_colors[v_offset].add(color)
    
    print("YES")
    print(' '.join(map(str, result)))

threading.Thread(target=main).start()