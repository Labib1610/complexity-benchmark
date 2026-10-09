import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj = [[] for _ in range(2 * n)]
    radj = [[] for _ in range(2 * n)]

    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2

        u_lit = 2 * (u - 1) if u > 0 else 2 * (-u - 1) + 1
        v_lit = 2 * (v - 1) if v > 0 else 2 * (-v - 1) + 1

        # not u -> v
        not_u = u_lit ^ 1
        not_v = v_lit ^ 1

        adj[not_u].append(v_lit)
        radj[v_lit].append(not_u)

        # not v -> u
        adj[not_v].append(u_lit)
        radj[u_lit].append(not_v)

    # Kosaraju's algorithm
    order = []
    visited = [False] * (2 * n)

    for i in range(2 * n):
        if not visited[i]:
            stack = [(i, 0)]
            visited[i] = True
            while stack:
                u, edge_idx = stack[-1]
                if edge_idx < len(adj[u]):
                    stack[-1] = (u, edge_idx + 1)
                    nxt = adj[u][edge_idx]
                    if not visited[nxt]:
                        visited[nxt] = True
                        stack.append((nxt, 0))
                else:
                    order.append(u)
                    stack.pop()

    scc = [-1] * (2 * n)
    scc_count = 0

    for u in reversed(order):
        if scc[u] == -1:
            stack = [u]
            scc[u] = scc_count
            while stack:
                curr = stack.pop()
                for nxt in radj[curr]:
                    if scc[nxt] == -1:
                        scc[nxt] = scc_count
                        stack.append(nxt)
            scc_count += 1

    ans = []
    for i in range(n):
        pos = 2 * i
        neg = 2 * i + 1
        if scc[pos] == scc[neg]:
            print("NO")
            return
        ans.append(1 if scc[pos] > scc[neg] else 0)

    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()