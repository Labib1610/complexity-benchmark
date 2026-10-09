import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(2 * n)]
    radj = [[] for _ in range(2 * n)]
    
    def get_lit(x):
        if x > 0:
            return 2 * (x - 1)
        else:
            return 2 * (-x - 1) + 1

    def get_neg(lit):
        return lit ^ 1

    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx + 1])
        idx += 2
        
        u = get_lit(l1)
        v = get_lit(l2)
        
        # (u or v) <=> (not u -> v) and (not v -> u)
        adj[get_neg(u)].append(v)
        radj[v].append(get_neg(u))
        adj[get_neg(v)].append(u)
        radj[u].append(get_neg(v))

    # Kosaraju's Algorithm
    order = []
    visited = [False] * (2 * n)
    for i in range(2 * n):
        if not visited[i]:
            visited[i] = True
            stack = [(i, 0)]
            while stack:
                u, edge_idx = stack.pop()
                if edge_idx < len(adj[u]):
                    stack.append((u, edge_idx + 1))
                    v = adj[u][edge_idx]
                    if not visited[v]:
                        visited[v] = True
                        stack.append((v, 0))
                else:
                    order.append(u)

    comp = [-1] * (2 * n)
    comp_count = 0
    for u in reversed(order):
        if comp[u] == -1:
            stack = [u]
            comp[u] = comp_count
            while stack:
                curr = stack.pop()
                for v in radj[curr]:
                    if comp[v] == -1:
                        comp[v] = comp_count
                        stack.append(v)
            comp_count += 1

    res = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        if comp[2 * i] > comp[2 * i + 1]:
            res[i] = 1
        else:
            res[i] = 0

    print("YES")
    print(*(res))

if __name__ == '__main__':
    solve()