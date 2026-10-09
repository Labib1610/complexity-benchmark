import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    graph = [[] for _ in range(N)]
    rev_graph = [[] for _ in range(N)]

    def node(var, val):
        return var * 2 + (0 if val else 1)

    for _ in range(m):
        l1, l2 = map(int, input().split())
        a = abs(l1) - 1
        av = l1 > 0
        b = abs(l2) - 1
        bv = l2 > 0

        # not A -> B
        u = node(a, not av)
        v = node(b, bv)
        graph[u].append(v)
        rev_graph[v].append(u)

        # not B -> A
        u = node(b, not bv)
        v = node(a, av)
        graph[u].append(v)
        rev_graph[v].append(u)

    visited = [False] * N
    order = []
    sys.setrecursionlimit(1 << 25)

    def dfs1(v):
        stack = [(v, 0)]
        while stack:
            v, idx = stack[-1]
            if idx == 0:
                visited[v] = True
            if idx < len(graph[v]):
                to = graph[v][idx]
                stack[-1] = (v, idx + 1)
                if not visited[to]:
                    stack.append((to, 0))
            else:
                order.append(v)
                stack.pop()

    for v in range(N):
        if not visited[v]:
            dfs1(v)

    comp = [-1] * N
    comp_cnt = 0

    def dfs2(v):
        stack = [v]
        while stack:
            v = stack.pop()
            comp[v] = comp_cnt
            for to in rev_graph[v]:
                if comp[to] == -1:
                    stack.append(to)

    for v in reversed(order):
        if comp[v] == -1:
            dfs2(v)
            comp_cnt += 1

    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    # Assignment: in topological order of condensation, comp ids are in reverse topological order.
    assign = [False] * n
    for i in range(n):
        assign[i] = comp[2 * i] > comp[2 * i + 1]

    print("YES")
    print(" ".join("1" if x else "0" for x in assign))

if __name__ == "__main__":
    main()