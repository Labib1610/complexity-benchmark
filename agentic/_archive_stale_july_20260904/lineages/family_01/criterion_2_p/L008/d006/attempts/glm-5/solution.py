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
    
    # A1 = [[1, 2], [0, 1]], A2 = [[1, 0], [2, 1]]
    # trace(A_s A_t) = 6 iff s != t
    # So we need a proper 2-coloring of the graph.
    # The harmonic condition: in every simple cycle, #1 = #2.
    # This means every cycle must have even length.
    # Thus, the graph must be bipartite.
    
    color = [-1] * n
    is_bipartite = True
    
    for i in range(n):
        if color[i] == -1:
            stack = [i]
            color[i] = 0
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
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
    
    # We need to output the assignment minimizing sum s_i * 3^(n-i).
    # s_i in {1, 2}. Let's map color 0 -> s=1, color 1 -> s=2.
    # We want to minimize the sum.
    # The term 3^(n-i) is positive. s_i=1 is smaller than s_i=2.
    # So we want to maximize the number of s_i=1.
    # This corresponds to maximizing the number of vertices with color 0.
    # We can flip components. Flipping swaps color 0 and 1 counts.
    # We should flip if count(color 1) > count(color 0).
    
    # Re-traverse to find components and counts
    visited = [False] * n
    components = []
    
    for i in range(n):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            components.append(comp)
            
    final_assignment = [0] * n
    
    for comp in components:
        cnt0 = 0
        cnt1 = 0
        for u in comp:
            if color[u] == 0:
                cnt0 += 1
            else:
                cnt1 += 1
        
        # If cnt1 > cnt0, we flip the colors in this component
        # to get more 1s (which correspond to color 0).
        # If cnt1 <= cnt0, we keep as is.
        # Note: s = color + 1. If we flip, s becomes (1-color) + 1 = 2-color.
        # We want s=1 (color 0). So we want to maximize color 0.
        # If currently cnt1 > cnt0, flipping makes cnt0' = cnt1 > cnt0.
        # So we flip if cnt1 > cnt0.
        
        if cnt1 > cnt0:
            for u in comp:
                final_assignment[u] = 2 - color[u] # flip: 0->2, 1->1
        else:
            for u in comp:
                final_assignment[u] = color[u] + 1 # keep: 0->1, 1->2
                
    print("YES")
    print(*(final_assignment))

if __name__ == '__main__':
    solve()