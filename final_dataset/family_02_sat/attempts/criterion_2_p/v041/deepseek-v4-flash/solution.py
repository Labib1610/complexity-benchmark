import sys
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    # 2-SAT: variable i (1..n) -> node 2*i for True, 2*i+1 for False
    # We'll use 0-based: node 2*i for True, 2*i+1 for False, i from 0..n-1
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    
    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)
    
    def node(lit):
        # lit > 0: variable lit must be True
        # lit < 0: variable -lit must be False
        var = abs(lit) - 1
        if lit > 0:
            return 2 * var      # True node
        else:
            return 2 * var + 1  # False node
    
    def neg_node(lit):
        # returns node for negation of lit
        var = abs(lit) - 1
        if lit > 0:
            return 2 * var + 1  # False node
        else:
            return 2 * var      # True node
    
    for _ in range(m):
        a, b = map(int, input().split())
        # clause (a or b) => (!a -> b) and (!b -> a)
        add_imp(neg_node(a), node(b))
        add_imp(neg_node(b), node(a))
    
    # Kosaraju's SCC
    visited = [False] * N
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1] * N
    def dfs2(u, cid):
        comp[u] = cid
        for v in gr[u]:
            if comp[v] == -1:
                dfs2(v, cid)
    
    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1
    
    # Check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    # Assign values: if comp[True] > comp[False] => True
    ans = [0] * n
    for i in range(n):
        # True node has higher comp id => assign True
        ans[i] = 1 if comp[2*i] > comp[2*i+1] else 0
    
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()