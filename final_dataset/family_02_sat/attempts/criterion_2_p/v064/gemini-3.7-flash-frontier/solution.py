import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    V = 2 * n
    adj = [[] for _ in range(V)]
    radj = [[] for _ in range(V)]

    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx + 1])
        idx += 2

        u = (abs(l1) - 1) * 2 + (0 if l1 > 0 else 1)
        v = (abs(l2) - 1) * 2 + (0 if l2 > 0 else 1)

        not_u = u ^ 1
        not_v = v ^ 1

        adj[not_u].append(v)
        radj[v].append(not_u)

        adj[not_v].append(u)
        radj[u].append(not_v)

    visited = [False] * V
    order = []

    for i in range(V):
        if not visited[i]:
            stack = [(i, 0)]
            visited[i] = True
            while stack:
                u, edge_idx = stack.pop()
                if edge_idx < len(adj[u]):
                    stack.append((u, edge_idx + 1))
                    nxt = adj[u][edge_idx]
                    if not visited[nxt]:
                        visited[nxt] = True
                        stack.append((nxt, 0))
                else:
                    order.append(u)

    scc = [-1] * V
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