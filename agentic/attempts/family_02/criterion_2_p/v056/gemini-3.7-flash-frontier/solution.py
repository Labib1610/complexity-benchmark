import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    num_nodes = 2 * n
    adj = [[] for _ in range(num_nodes)]
    rev_adj = [[] for _ in range(num_nodes)]

    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx + 1])
        idx += 2

        u = (l1 - 1) * 2 if l1 > 0 else (-l1 - 1) * 2 + 1
        v = (l2 - 1) * 2 if l2 > 0 else (-l2 - 1) * 2 + 1

        # Clause (u or v) <=> (~u -> v) and (~v -> u)
        not_u = u ^ 1
        not_v = v ^ 1

        adj[not_u].append(v)
        rev_adj[v].append(not_u)

        adj[not_v].append(u)
        rev_adj[u].append(not_v)

    # Kosaraju's algorithm
    order = []
    visited = [False] * num_nodes

    for i in range(num_nodes):
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
                    stack.pop()
                    order.append(u)

    scc = [-1] * num_nodes
    scc_id = 0

    for u in reversed(order):
        if scc[u] == -1:
            stack = [u]
            scc[u] = scc_id
            while stack:
                curr = stack.pop()
                for nxt in rev_adj[curr]:
                    if scc[nxt] == -1:
                        scc[nxt] = scc_id
                        stack.append(nxt)
            scc_id += 1

    ans = [0] * n
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("NO")
            return
        ans[i] = 1 if scc[2 * i] > scc[2 * i + 1] else 0

    print("YES")
    print(*(ans))


if __name__ == "__main__":
    solve()