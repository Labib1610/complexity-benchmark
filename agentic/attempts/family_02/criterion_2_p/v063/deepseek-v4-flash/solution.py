import sys
sys.setrecursionlimit(300000)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # node numbers: 0..2n-1
    # For variable i (1-indexed):  
    # node 2*(i-1)   -> positive literal (x_i = True)  
    # node 2*(i-1)+1 -> negative literal (x_i = False)
    
    def node(lit):
        # lit > 0: positive, lit < 0: negative
        var = abs(lit) - 1
        if lit > 0:
            return 2 * var
        else:
            return 2 * var + 1
    
    def neg_node(u):
        return u ^ 1
    
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # (a or b) => (!a -> b) and (!b -> a)
        g[neg_node(u)].append(v)
        gr[v].append(neg_node(u))
        g[neg_node(v)].append(u)
        gr[u].append(neg_node(v))
    
    # Kosaraju
    visited = [False] * N
    order = []
    
    def dfs1(v):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs1(to)
        order.append(v)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1] * N
    comp_id = 0
    
    def dfs2(v, cid):
        comp[v] = cid
        for to in gr[v]:
            if comp[to] == -1:
                dfs2(to, cid)
    
    for v in reversed(order):
        if comp[v] == -1:
            dfs2(v, comp_id)
            comp_id += 1
    
    # Check unsatisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    # Assignment: choose value based on SCC order
    # In Kosaraju, comp numbers are assigned in topological order of SCC DAG
    assignment = [False] * n
    for i in range(n):
        # If comp of True literal < comp of False literal -> assign True
        assignment[i] = comp[2*i] < comp[2*i+1]
    
    print("YES")
    print(" ".join("1" if assignment[i] else "0" for i in range(n)))

if __name__ == "__main__":
    main()