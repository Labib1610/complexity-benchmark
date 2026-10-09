import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    num_nodes = 2 * n
    head = [-1] * num_nodes
    to = []
    nxt = []

    head_rev = [-1] * num_nodes
    to_rev = []
    nxt_rev = []

    def add_edge(u, v):
        nxt.append(head[u])
        to.append(v)
        head[u] = len(to) - 1

        nxt_rev.append(head_rev[v])
        to_rev.append(u)
        head_rev[v] = len(to_rev) - 1

    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx + 1])
        idx += 2

        u = 2 * (l1 - 1) if l1 > 0 else 2 * (-l1 - 1) + 1
        v = 2 * (l2 - 1) if l2 > 0 else 2 * (-l2 - 1) + 1

        not_u = u ^ 1
        not_v = v ^ 1

        add_edge(not_u, v)
        add_edge(not_v, u)

    # Kosaraju's Algorithm (Iterative)
    visited = [False] * num_nodes
    order = []
    stack = []

    for i in range(num_nodes):
        if not visited[i]:
            stack.append((i, head[i]))
            visited[i] = True
            while stack:
                u, e = stack[-1]
                if e != -1:
                    stack[-1] = (u, nxt[e])
                    v = to[e]
                    if not visited[v]:
                        visited[v] = True
                        stack.append((v, head[v]))
                else:
                    order.append(u)
                    stack.pop()

    scc = [-1] * num_nodes
    scc_count = 0
    stack = []

    for i in reversed(order):
        if scc[i] == -1:
            scc[i] = scc_count
            stack.append((i, head_rev[i]))
            while stack:
                u, e = stack[-1]
                if e != -1:
                    stack[-1] = (u, nxt_rev[e])
                    v = to_rev[e]
                    if scc[v] == -1:
                        scc[v] = scc_count
                        stack.append((v, head_rev[v]))
                else:
                    stack.pop()
            scc_count += 1

    ans = [0] * n
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("NO")
            return
        ans[i] = 1 if scc[2 * i] > scc[2 * i + 1] else 0

    print("YES")
    print(*(ans[i] for i in range(n)))


if __name__ == "__main__":
    solve()