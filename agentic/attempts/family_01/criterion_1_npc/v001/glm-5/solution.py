import sys
sys.setrecursionlimit(10000)

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    it = iter(input)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    
    def dfs(u, c):
        color[u] = c
        for v in adj[u]:
            if color[v] == 0:
                if not dfs(v, 3 - c):
                    return False
            elif color[v] == c:
                return False
        return True
    
    components = []
    visited = [False] * n
    
    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                print("NO")
                return
            comp = []
            for j in range(n):
                if color[j] != 0 and not visited[j]:
                    comp.append(j)
                    visited[j] = True
            components.append(comp)
    
    # Reset color for assignment
    color = [0] * n
    
    for comp in components:
        size = len(comp)
        # Each component is bipartite; maximum independent set size is ceil(size/2)
        # We need to split into 3 groups such that each group is independent set
        # This is possible iff ceil(size/2) <= 2, i.e., size <= 3
        if size > 3:
            print("NO")
            return
        if size == 1:
            color[comp[0]] = 1
        elif size == 2:
            color[comp[0]] = 1
            color[comp[1]] = 2
        else:  # size == 3
            # Check assignments: one node gets unique color
            # Option 1: node 0 gets color 3
            c0, c1, c2 = 1, 2, 3
            valid = True
            for v in comp:
                for nei in adj[v]:
                    if nei in comp:
                        if (v == comp[0] and color_assign[nei] == c0) or \
                           (v == comp[1] and color_assign[nei] == c1) or \
                           (v == comp[2] and color_assign[nei] == c2):
                            valid = False
            if valid:
                color_assign = {comp[0]: 1, comp[1]: 2, comp[2]: 3}
            else:
                # Option 2: node 1 gets color 3
                color_assign = {comp[0]: 1, comp[1]: 3, comp[2]: 2}
            for v in comp:
                color[v] = color_assign[v]
    
    # Verify final assignment
    for u in range(n):
        for v in adj[u]:
            if v > u and color[u] == color[v]:
                print("NO")
                return
    
    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()