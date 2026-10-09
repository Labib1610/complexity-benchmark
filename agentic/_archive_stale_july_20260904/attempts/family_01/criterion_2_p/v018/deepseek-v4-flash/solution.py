import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    color = [-1] * n
    comp = []
    
    def dfs(u, c):
        color[u] = c
        comp.append(u)
        for v in adj[u]:
            if color[v] == -1:
                if not dfs(v, c ^ 1):
                    return False
            elif color[v] == color[u]:
                return False
        return True
    
    # Check bipartite and assign initial colors
    for i in range(n):
        if color[i] == -1:
            comp = []
            if not dfs(i, 0):
                print("NO")
                return
    
    # Now we have a bipartite graph, but we need lexicographically smallest assignment
    # We'll try to assign 1 to as many early vertices as possible
    # Since graph is bipartite, we can flip components independently.
    # But flipping a component means swapping colors in that component.
    # We want lexicographically smallest sequence, so process vertices in order.
    
    # Build component id and component size
    comp_id = [-1] * n
    comps = []
    for i in range(n):
        if comp_id[i] == -1:
            cid = len(comps)
            stack = [i]
            comp_id[i] = cid
            nodes = []
            while stack:
                u = stack.pop()
                nodes.append(u)
                for v in adj[u]:
                    if comp_id[v] == -1:
                        comp_id[v] = cid
                        stack.append(v)
            comps.append(nodes)
    
    # For each component, we can decide whether to flip or not.
    # But flipping a component changes all its vertices' colors.
    # We want lexicographically smallest, so process vertices in order.
    # For each vertex, if we can set it to 1 without conflict, do so.
    # This is equivalent to 2-SAT style but simpler: since each component is bipartite,
    # we can try both orientations and pick the one that gives smaller result.
    
    # Actually, we can do greedy: process vertices in order, try to set to 1.
    # For each vertex, if not assigned, BFS/DFS to assign its component with this vertex as 1.
    # But we need to ensure consistency.
    
    # Simpler: Since graph is bipartite, we can do BFS and for each component,
    # try both colorings and pick the one that gives lexicographically smaller result.
    
    res = [0] * n
    visited = [False] * n
    
    for start in range(n):
        if visited[start]:
            continue
        # BFS to get component
        stack = [start]
        visited[start] = True
        nodes = []
        while stack:
            u = stack.pop()
            nodes.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        
        # Now nodes form a connected component
        # Try both colorings
        for flip in [0, 1]:
            temp = {}
            ok = True
            q = [nodes[0]]
            temp[nodes[0]] = flip
            while q:
                u = q.pop()
                for v in adj[u]:
                    if v in temp:
                        if temp[v] == temp[u]:
                            ok = False
                            break
                    else:
                        temp[v] = temp[u] ^ 1
                        q.append(v)
                if not ok:
                    break
            if ok:
                # Assign to res
                for u, c in temp.items():
                    res[u] = c + 1
                break
        else:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()