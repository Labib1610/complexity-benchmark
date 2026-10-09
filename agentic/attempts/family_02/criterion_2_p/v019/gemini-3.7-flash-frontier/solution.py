import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    num_vars = 2 * n
    head = [-1] * num_vars
    to = []
    nxt = []

    head_rev = [-1] * num_vars
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

        u = (l1 - 1) * 2 if l1 > 0 else (-l1 - 1) * 2 + 1
        v = (l2 - 1) * 2 if l2 > 0 else (-l2 - 1) * 2 + 1

        add_edge(u ^ 1, v)
        add_edge(v ^ 1, u)

    # Kosaraju's Algorithm (Iterative)
    visited = [False] * num_vars
    order = []

    for i in range(num_vars):
        if not visited[i]:
            stack = [i]
            edge_ptr = [head[i]]
            visited[i] = True

            while stack:
                u = stack[-1]
                e = edge_ptr[-1]
                found = False
                while e != -1:
                    v = to[e]
                    e = nxt[e]
                    edge_ptr[-1] = e
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
                        edge_ptr.append(head[v])
                        found = True
                        break
                if not found:
                    order.append(stack.pop())
                    edge_ptr.pop()

    scc = [-1] * num_vars
    scc_cnt = 0

    for u in reversed(order):
        if scc[u] == -1:
            stack = [u]
            scc[u] = scc_cnt
            while stack:
                curr = stack.pop()
                e = head_rev[curr]
                while e != -1:
                    v = to_rev[e]
                    if scc[v] == -1:
                        scc[v] = scc_cnt
                        stack.append(v)
                    e = nxt_rev[e]
            scc_cnt += 1

    assignment = [0] * n
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("NO")
            return
        if scc[2 * i] < scc[2 * i + 1]:
            assignment[i] = 1
        else:
            assignment[i] = 0

    print("YES")
    print(*(assignment))


if __name__ == "__main__":
    solve()