import sys


def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    adj = [[] for _ in range(2 * n)]
    radj = [[] for _ in range(2 * n)]

    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx + 1])
        idx += 2

        # Convert literals to node indices:
        # positive x -> 2*(x-1), negative -x -> 2*(x-1) + 1
        if l1 > 0:
            u = 2 * (l1 - 1)
        else:
            u = 2 * (-l1 - 1) + 1

        if l2 > 0:
            v = 2 * (l2 - 1)
        else:
            v = 2 * (-l2 - 1) + 1

        # Clause: (u or v) <=> (~u -> v) and (~v -> u)
        not_u = u ^ 1
        not_v = v ^ 1

        adj[not_u].append(v)
        radj[v].append(not_u)

        adj[not_v].append(u)
        radj[u].append(not_v)

    # Iterative Kosaraju's Algorithm
    order = []
    visited = [False] * (2 * n)
    for start in range(2 * n):
        if not visited[start]:
            stack = [(start, 0)]
            visited[start] = True
            while stack:
                curr, edge_idx = stack[-1]
                if edge_idx < len(adj[curr]):
                    stack[-1] = (curr, edge_idx + 1)
                    nxt = adj[curr][edge_idx]
                    if not visited[nxt]:
                        visited[nxt] = True
                        stack.append((nxt, 0))
                else:
                    order.append(curr)
                    stack.pop()

    scc = [-1] * (2 * n)
    scc_id = 0
    for start in reversed(order):
        if scc[start] == -1:
            stack = [start]
            scc[start] = scc_id
            while stack:
                curr = stack.pop()
                for nxt in radj[curr]:
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
    print(*(ans[i] for i in range(n)))


if __name__ == "__main__":
    main()