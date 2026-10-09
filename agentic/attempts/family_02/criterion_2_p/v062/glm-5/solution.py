import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # Build implication graph for 2-SAT.
    # Variable i: node 2*i is "i is 0", node 2*i+1 is "i is 1".
    # Clause (l1 v l2): add implications not l1 -> l2 and not l2 -> l1.
    adj = [[] for _ in range(2 * n)]
    radj = [[] for _ in range(2 * n)]

    def node(v):
        # v > 0: species v is 1 -> node (v-1)*2 + 1
        # v < 0: species |v| is 0 -> node (|v|-1)*2
        if v > 0:
            return 2 * (v - 1) + 1
        else:
            return 2 * (-v - 1)

    def neg(x):
        return x ^ 1

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        a = node(l1)
        b = node(l2)
        na = neg(a)
        nb = neg(b)
        adj[na].append(b)
        adj[nb].append(a)
        radj[b].append(na)
        radj[a].append(nb)

    # Kosaraju's algorithm to find SCCs.
    order = []
    visited = bytearray(2 * n)
    stack = []

    for i in range(2 * n):
        if not visited[i]:
            visited[i] = 1
            stack.append(i)
            while stack:
                v = stack[-1]
                if adj[v]:
                    w = adj[v].pop()
                    if not visited[w]:
                        visited[w] = 1
                        stack.append(w)
                else:
                    stack.pop()
                    order.append(v)

    comp = [-1] * (2 * n)
    cid = 0
    for i in reversed(order):
        if comp[i] == -1:
            stack = [i]
            comp[i] = cid
            while stack:
                v = stack.pop()
                for w in radj[v]:
                    if comp[w] == -1:
                        comp[w] = cid
                        stack.append(w)
            cid += 1

    # Check satisfiability.
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    # Assign values: if comp[2*i] > comp[2*i+1], set i to 1, else 0.
    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] > comp[2 * i + 1]:
            assignment[i] = 1
        else:
            assignment[i] = 0

    print("YES")
    print(' '.join(map(str, assignment)))

solve()