import sys
input = sys.stdin.readline

def solve():
    sys.setrecursionlimit(1 << 25)
    n_m = input().split()
    if not n_m:
        return
    n = int(n_m[0])
    m = int(n_m[1])

    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]

    for _ in range(m):
        l1_str, l2_str = input().split()
        l1 = int(l1_str)
        l2 = int(l2_str)
        
        u, v = abs(l1) - 1, abs(l2) - 1
        nu, nv = (l1 > 0), (l2 > 0)
        
        u_node = 2 * u + nu
        v_node = 2 * v + nv
        u_not_node = 2 * u + (1 - nu)
        v_not_node = 2 * v + (1 - nv)
        
        # Clause (l1 OR l2)
        adj[u_not_node].append(v_node)
        adj[v_not_node].append(u_node)
        rev_adj[v_node].append(u_not_node)
        rev_adj[u_node].append(v_not_node)

    # Kosaraju's algorithm
    order = []
    visited = [False] * (2 * n)

    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            
            if idx < len(adj[node]):
                neighbor = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[neighbor]:
                    stack.append((neighbor, 0))
            else:
                stack.pop()
                order.append(node)

    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)

    comp_id = [-1] * (2 * n)
    
    def dfs2(root, label):
        stack = [root]
        while stack:
            u = stack.pop()
            if comp_id[u] != -1:
                continue
            comp_id[u] = label
            for v in rev_adj[u]:
                if comp_id[v] == -1:
                    stack.append(v)

    label = 0
    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, label)
            label += 1

    result = [0] * n
    for i in range(n):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            print("NO")
            return
        if comp_id[2 * i] > comp_id[2 * i + 1]:
            result[i] = 1
    
    print("YES")
    print(*(result))

if __name__ == '__main__':
    solve()