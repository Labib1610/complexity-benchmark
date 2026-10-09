import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        u = abs(l1) - 1
        v = abs(l2) - 1
        
        if l1 > 0:
            nu = u + n
        else:
            nu = u
        
        if l2 > 0:
            nv = v + n
        else:
            nv = v
        
        adj[nu].append(v)
        adj[nv].append(u)
    
    sys.setrecursionlimit(300000)
    visited = [False] * (2 * n)
    order = []
    
    def dfs(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            if idx < len(adj[node]):
                nei = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[nei]:
                    stack.append((nei, 0))
            else:
                stack.pop()
                order.append(node)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs(i)
    
    visited = [False] * (2 * n)
    comp_id = [-1] * (2 * n)
    current_comp = 0
    
    for u in reversed(order):
        if not visited[u]:
            stack = [u]
            visited[u] = True
            comp_nodes = []
            while stack:
                node = stack.pop()
                comp_nodes.append(node)
                for v in adj[node]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            for node in comp_nodes:
                comp_id[node] = current_comp
            current_comp += 1
    
    assignment = [0] * n
    for i in range(n):
        if comp_id[i] == comp_id[i + n]:
            print("NO")
            return
        assignment[i] = 1 if comp_id[i] > comp_id[i + n] else 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()