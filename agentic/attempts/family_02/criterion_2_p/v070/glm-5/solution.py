import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(2 * n + 1)]

    def get_node(channel, mode):
        if mode == 1:
            return channel
        else:
            return n + channel

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        c1 = abs(l1)
        m1 = 1 if l1 > 0 else 0
        c2 = abs(l2)
        m2 = 1 if l2 > 0 else 0
        
        u = get_node(c1, 1 - m1)
        v = get_node(c2, m2)
        adj[u].append(v)
        
        u = get_node(c2, 1 - m2)
        v = get_node(c1, m1)
        adj[u].append(v)

    visited = [0] * (2 * n + 1)
    order = []
    
    def dfs1(u):
        visited[u] = 1
        for v in adj[u]:
            if visited[v] == 0:
                dfs1(v)
        order.append(u)

    for i in range(1, 2 * n + 1):
        if visited[i] == 0:
            dfs1(i)

    comp_id = [0] * (2 * n + 1)
    current_id = 0
    
    def dfs2(u, cid):
        comp_id[u] = cid
        for v in adj[u]:
            if comp_id[v] == 0:
                dfs2(v, cid)

    for u in reversed(order):
        if comp_id[u] == 0:
            current_id += 1
            dfs2(u, current_id)

    assignment = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        node_high = i
        node_low = n + i
        if comp_id[node_high] == comp_id[node_low]:
            possible = False
            break
        elif comp_id[node_high] > comp_id[node_low]:
            assignment[i] = 1
        else:
            assignment[i] = 0

    if not possible:
        print("NO")
    else:
        print("YES")
        print(*(assignment[1:]))

if __name__ == '__main__':
    solve()