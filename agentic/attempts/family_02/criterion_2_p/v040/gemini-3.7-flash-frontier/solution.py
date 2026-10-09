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

        u = (2 * (l1 - 1)) if l1 > 0 else (2 * (-l1 - 1) + 1)
        v = (2 * (l2 - 1)) if l2 > 0 else (2 * (-l2 - 1) + 1)

        neg_u = u ^ 1
        neg_v = v ^ 1

        # neg_u -> v
        adj[neg_u].append(v)
        rev_adj[v].append(neg_u)

        # neg_v -> u
        adj[neg_v].append(u)
        rev_adj[u].append(neg_v)

    visited = [0] * num_nodes
    order = []

    for i in range(num_nodes):
        if visited[i]:
            continue
        stack = [i]
        while stack:
            u = stack[-1]
            if visited[u] == 0:
                visited[u] = 1
                for v in adj[u]:
                    if visited[v] == 0:
                        stack.append(v)
            else:
                stack.pop()
                if visited[u] == 1:
                    visited[u] = 2
                    order.append(u)

    scc = [-1] * num_nodes
    scc_count = 0

    for i in reversed(order):
        if scc[i] != -1:
            continue
        stack = [i]
        scc[i] = scc_count
        while stack:
            u = stack.pop()
            for v in rev_adj[u]:
                if scc[v] == -1:
                    scc[v] = scc_count
                    stack.append(v)
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


if __name__ == "__main__":
    solve()