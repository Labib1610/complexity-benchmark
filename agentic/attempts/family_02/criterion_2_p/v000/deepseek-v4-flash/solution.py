import sys
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def node(var):
        # var: positive or negative integer
        if var > 0:
            return (var - 1) * 2 + 1  # true literal
        else:
            return (-var - 1) * 2     # false literal

    def neg_node(idx):
        return idx ^ 1

    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # (not u) -> v
        g[neg_node(u)].append(v)
        gr[v].append(neg_node(u))
        # (not v) -> u
        g[neg_node(v)].append(u)
        gr[u].append(neg_node(v))

    # Kosaraju SCC
    visited = [False] * N
    order = []

    def dfs1(u):
        visited[u] = True
        for w in g[u]:
            if not visited[w]:
                dfs1(w)
        order.append(u)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * N
    comp_id = 0

    def dfs2(u):
        comp[u] = comp_id
        for w in gr[u]:
            if comp[w] == -1:
                dfs2(w)

    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u)
            comp_id += 1

    # Check satisfiability
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    # Assign values: if comp[true] > comp[false] => true
    assignment = [0] * n
    for i in range(n):
        # true literal index = 2*i+1, false = 2*i
        assignment[i] = 1 if comp[2 * i + 1] > comp[2 * i] else 0

    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()