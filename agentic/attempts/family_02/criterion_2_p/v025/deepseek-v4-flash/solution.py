import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    # 2-SAT: node for x is 2*x, for ~x is 2*x+1
    # variable index from 1..n
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    
    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)
    
    def node(lit):
        # lit > 0 -> variable lit, lit < 0 -> negation
        if lit > 0:
            return 2 * (lit - 1)
        else:
            return 2 * (-lit - 1) + 1
    
    def neg_node(u):
        return u ^ 1
    
    for _ in range(m):
        a, b = map(int, input().split())
        u = node(a)
        v = node(b)
        # (a OR b) => (~a -> b) and (~b -> a)
        add_imp(neg_node(u), v)
        add_imp(neg_node(v), u)
    
    # Tarjan SCC
    index = 0
    indices = [-1] * N
    lowlink = [0] * N
    onstack = [False] * N
    stack = []
    scc_id = [-1] * N
    scc_count = 0
    
    def strongconnect(v):
        nonlocal index, scc_count
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        onstack[v] = True
        
        for w in g[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif onstack[w]:
                lowlink[v] = min(lowlink[v], indices[w])
        
        if lowlink[v] == indices[v]:
            while True:
                w = stack.pop()
                onstack[w] = False
                scc_id[w] = scc_count
                if w == v:
                    break
            scc_count += 1
    
    for v in range(N):
        if indices[v] == -1:
            strongconnect(v)
    
    # Check satisfiability
    for i in range(n):
        if scc_id[2*i] == scc_id[2*i+1]:
            print("NO")
            return
    
    # Assign values: in reverse topological order of SCCs
    # If scc_id[x] > scc_id[~x], then x is True
    assignment = [0] * n
    for i in range(n):
        assignment[i] = 1 if scc_id[2*i] > scc_id[2*i+1] else 0
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()