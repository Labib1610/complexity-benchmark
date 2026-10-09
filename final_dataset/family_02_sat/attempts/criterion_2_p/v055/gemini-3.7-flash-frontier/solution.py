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

        # Convert to 0-indexed literal:
        # positive x -> 2*(x-1), negative x -> 2*(|x|-1) + 1
        node_u = 2 * (u - 1) if u > 0 else 2 * (-u - 1) + 1
        node_v = 2 * (v - 1) if v > 0 else 2 * (-v - 1) + 1

        neg_u = node_u ^ 1
        neg_v = node_v ^ 1

        # Clause: (u or v) <=> (~u => v) and (~v => u)
        adj[neg_u].append(node_v)
        radj[node_v].append(neg_u)

        adj[neg_v].append(node_u)
        radj[node_u].append(neg_v)

    num_nodes = 2 * n

    # Kosaraju's Algorithm - Pass 1
    order = []
    visited = [False] * num_nodes
    for start in range(num_nodes):
        if visited[start]:
            continue
        stack = [(start, 0)]
        visited[start] = True
        while stack:
            u, i = stack[-1]
            if i < len(adj[u]):
                stack[-1] = (u, i + 1)
                v = adj[u][i]
                if not visited[v]:
                    visited[v] = True
                    stack.append((v, 0))
            else:
                order.append(u)
                stack.pop()

    # Kosaraju's Algorithm - Pass 2
    scc = [-1] * num_nodes
    scc_count = 0
    for start in reversed(order):
        if scc[start] != -1:
            continue
        stack = [start]
        scc[start] = scc_count
        while stack:
            u = stack.pop()
            for v in radj[u]:
                if scc[v] == -1:
                    scc[v] = scc_count
                    stack.append(v)
        scc_count += 1

    # Check 2-SAT satisfiability and construct solution
    res = []
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("NO")
            return
        if scc[2 * i] < scc[2 * i + 1]:
            res.append("1")
        else:
            res.append("0")

    print("YES")
    print(" ".join(res))

if __name__ == "__main__":
    solve()