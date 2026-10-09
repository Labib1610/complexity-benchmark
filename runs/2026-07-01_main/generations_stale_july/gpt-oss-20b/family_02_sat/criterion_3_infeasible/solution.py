import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    N = 2 * n
    G = [[] for _ in range(N)]
    GR = [[] for _ in range(N)]

    def lit_id(l):
        if l > 0:
            return 2 * (l - 1) + 1
        else:
            return 2 * ((-l) - 1)

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        id1 = lit_id(l1)
        id2 = lit_id(l2)
        n1 = id1 ^ 1
        n2 = id2 ^ 1
        G[n1].append(id2)
        GR[id2].append(n1)
        G[n2].append(id1)
        GR[id1].append(n2)

    visited = [False] * N
    order = []

    # first pass: order by finish time
    for v in range(N):
        if not visited[v]:
            stack = [(v, 0)]
            visited[v] = True
            while stack:
                node, idx = stack[-1]
                if idx < len(G[node]):
                    nei = G[node][idx]
                    stack[-1] = (node, idx + 1)
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append((nei, 0))
                else:
                    stack.pop()
                    order.append(node)

    comp = [-1] * N
    cid = 0
    # second pass: assign components
    for v in reversed(order):
        if comp[v] == -1:
            stack = [v]
            comp[v] = cid
            while stack:
                node = stack.pop()
                for nei in GR[node]:
                    if comp[nei] == -1:
                        comp[nei] = cid
                        stack.append(nei)
            cid += 1

    # find smallest trapped variable
    for i in range(1, n + 1):
        true_id = 2 * (i - 1) + 1
        false_id = 2 * (i - 1)
        if comp[true_id] == comp[false_id]:
            print(i)
            return

if __name__ == "__main__":
    main()