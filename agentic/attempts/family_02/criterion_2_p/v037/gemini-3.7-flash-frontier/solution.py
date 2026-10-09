import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    def get_node(lit):
        if lit > 0:
            return 2 * (lit - 1)
        else:
            return 2 * (-lit - 1) + 1

    num_nodes = 2 * n
    adj = [[] for _ in range(num_nodes)]
    rev_adj = [[] for _ in range(num_nodes)]

    idx = 2
    for _ in range(m):
        u_lit = int(input_data[idx])
        v_lit = int(input_data[idx + 1])
        idx += 2

        u = get_node(u_lit)
        v = get_node(v_lit)

        # (u or v) is equivalent to (not u => v) and (not v => u)
        adj[u ^ 1].append(v)
        adj[v ^ 1].append(u)
        rev_adj[v].append(u ^ 1)
        rev_adj[u].append(v ^ 1)

    # Kosaraju's algorithm - Pass 1: compute finish order
    visited = [False] * num_nodes
    order = []
    for start in range(num_nodes):
        if not visited[start]:
            stack = [(start, 0)]
            visited[start] = True
            while stack:
                u, edge_idx = stack[-1]
                if edge_idx < len(adj[u]):
                    stack[-1] = (u, edge_idx + 1)
                    v = adj[u][edge_idx]
                    if not visited[v]:
                        visited[v] = True
                        stack.append((v, 0))
                else:
                    stack.pop()
                    order.append(u)

    # Kosaraju's algorithm - Pass 2: find SCCs
    scc = [-1] * num_nodes
    scc_count = 0
    for start in reversed(order):
        if scc[start] == -1:
            stack = [start]
            scc[start] = scc_count
            while stack:
                u = stack.pop()
                for v in rev_adj[u]:
                    if scc[v] == -1:
                        scc[v] = scc_count
                        stack.append(v)
            scc_count += 1

    # Determine satisfiability and build solution
    res = []
    for i in range(n):
        pos_node = 2 * i
        neg_node = 2 * i + 1
        if scc[pos_node] == scc[neg_node]:
            print("NO")
            return
        if scc[pos_node] > scc[neg_node]:
            res.append("1")
        else:
            res.append("0")

    print("YES")
    print(" ".join(res))


if __name__ == "__main__":
    solve()