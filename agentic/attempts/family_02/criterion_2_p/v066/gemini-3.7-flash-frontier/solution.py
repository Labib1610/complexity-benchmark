import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    # 2*i for True (Standard), 2*i + 1 for False (Auxiliary)
    adj = [[] for _ in range(2 * n)]
    radj = [[] for _ in range(2 * n)]

    idx = 2
    for _ in range(m):
        c1 = int(input_data[idx])
        c2 = int(input_data[idx + 1])
        idx += 2

        if c1 > 0:
            u = 2 * (c1 - 1)
        else:
            u = 2 * (-c1 - 1) + 1

        if c2 > 0:
            v = 2 * (c2 - 1)
        else:
            v = 2 * (-c2 - 1) + 1

        # not u -> v
        not_u = u ^ 1
        adj[not_u].append(v)
        radj[v].append(not_u)

        # not v -> u
        not_v = v ^ 1
        adj[not_v].append(u)
        radj[u].append(not_v)

    # Pass 1: Order by finishing time
    visited = [False] * (2 * n)
    order = []

    for i in range(2 * n):
        if not visited[i]:
            stack = [i]
            it_stack = [0]
            visited[i] = True
            while stack:
                u = stack[-1]
                it = it_stack[-1]
                if it < len(adj[u]):
                    v = adj[u][it]
                    it_stack[-1] += 1
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
                        it_stack.append(0)
                else:
                    order.append(u)
                    stack.pop()
                    it_stack.pop()

    # Pass 2: Strongly Connected Components on reverse graph
    scc = [-1] * (2 * n)
    num_scc = 0
    for u in reversed(order):
        if scc[u] == -1:
            scc[u] = num_scc
            stack = [u]
            while stack:
                curr = stack.pop()
                for v in radj[curr]:
                    if scc[v] == -1:
                        scc[v] = num_scc
                        stack.append(v)
            num_scc += 1

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