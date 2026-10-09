import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in range(2 * n)]
    
    # We'll use 2-SAT: variable i means s_i = 1
    # For each clause, we need to derive implications.
    # Condition: l1*(2*s_u - 1) + l2*(2*s_v - 1) = -(|l1|+|l2|)
    # Let's analyze when this fails.
    # Let a = 2*s_u - 1, b = 2*s_v - 1, so a,b in {-1, 1}
    # l1*a + l2*b = -(|l1|+|l2|)
    # Since |l1*a + l2*b| <= |l1|+|l2|, equality holds only if l1*a and l2*b are both non-positive and sum to -( |l1|+|l2| )
    # That means l1*a = -|l1| and l2*b = -|l2|, i.e., a = -sign(l1), b = -sign(l2)
    # So failure occurs iff s_u = (1 - sign(l1))/2 and s_v = (1 - sign(l2))/2
    # i.e., s_u = (1 - sign(l1))//2, s_v = (1 - sign(l2))//2
    # So to avoid failure, we must NOT have both equalities simultaneously.
    # That is: (s_u != (1 - sign(l1))//2) OR (s_v != (1 - sign(l2))//2)
    # This is a 2-SAT clause: (s_u == val1) OR (s_v == val2) where val1 = 1 - (1 - sign(l1))//2? Let's compute.
    # Let's define: for variable x_i meaning s_i = 1.
    # If l1 > 0, sign=1 => failure if s_u=0. So to avoid: s_u=1 OR s_v=1 (if l2>0) etc.
    # Let's derive systematically:
    # failure if s_u = (1 - sign(l1))//2 and s_v = (1 - sign(l2))//2
    # So safe if NOT (s_u = A and s_v = B) where A = (1 - sign(l1))//2, B = (1 - sign(l2))//2
    # That is: (s_u != A) OR (s_v != B)
    # In terms of literals:
    # If A == 0: s_u != 0 => s_u = 1 => literal x_u
    # If A == 1: s_u != 1 => s_u = 0 => literal ¬x_u
    # Similarly for v.
    # So clause: (lit_u) OR (lit_v)
    # where lit_u = x_u if A==0 else ¬x_u, lit_v = x_v if B==0 else ¬x_v
    
    for _ in range(m):
        l1, l2 = map(int, input().split())
        u = abs(l1) - 1
        v = abs(l2) - 1
        sign1 = 1 if l1 > 0 else -1
        sign2 = 1 if l2 > 0 else -1
        A = (1 - sign1) // 2  # 0 if sign1=1, 1 if sign1=-1
        B = (1 - sign2) // 2
        # lit_u = x_u if A==0 else ¬x_u
        # lit_v = x_v if B==0 else ¬x_v
        # Add clause (lit_u OR lit_v)
        # In 2-SAT: (a OR b) => (¬a -> b) and (¬b -> a)
        # Let's encode: variable index: 2*i for x_i false? We'll use standard: node 2*i means x_i=False? Actually typical: 2*i = x_i false, 2*i+1 = x_i true.
        # We'll use: 2*i for x_i = False, 2*i+1 for x_i = True.
        # Then literal x_i is node 2*i+1, literal ¬x_i is node 2*i.
        # Clause (p OR q) => (¬p -> q) and (¬q -> p)
        # p = lit_u, q = lit_v
        # If A==0: lit_u = x_u => node 2*u+1, ¬lit_u = node 2*u
        # If A==1: lit_u = ¬x_u => node 2*u, ¬lit_u = node 2*u+1
        # Similarly for v.
        if A == 0:
            u_true = 2*u+1
            u_false = 2*u
        else:
            u_true = 2*u
            u_false = 2*u+1
        if B == 0:
            v_true = 2*v+1
            v_false = 2*v
        else:
            v_true = 2*v
            v_false = 2*v+1
        # lit_u is u_true if A==0 else u_false? Wait careful:
        # If A==0: lit_u = x_u => node 2*u+1 (true)
        # If A==1: lit_u = ¬x_u => node 2*u (false)
        # So lit_u_node = 2*u+1 if A==0 else 2*u
        # ¬lit_u_node = 2*u if A==0 else 2*u+1
        # Similarly for v.
        lit_u_node = 2*u+1 if A == 0 else 2*u
        lit_v_node = 2*v+1 if B == 0 else 2*v
        not_lit_u_node = 2*u if A == 0 else 2*u+1
        not_lit_v_node = 2*v if B == 0 else 2*v+1
        # (lit_u OR lit_v) => (¬lit_u -> lit_v) and (¬lit_v -> lit_u)
        g[not_lit_u_node].append(lit_v_node)
        g[not_lit_v_node].append(lit_u_node)
    
    # Kosaraju SCC
    N = 2*n
    visited = [False]*N
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
    
    rg = [[] for _ in range(N)]
    for v in range(N):
        for to in g[v]:
            rg[to].append(v)
    
    comp = [-1]*N
    def dfs2(v, c):
        comp[v] = c
        for to in rg[v]:
            if comp[to] == -1:
                dfs2(to, c)
    
    cid = 0
    for v in reversed(order):
        if comp[v] == -1:
            dfs2(v, cid)
            cid += 1
    
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    print("YES")
    res = []
    for i in range(n):
        # comp[2*i] < comp[2*i+1] => x_i true
        if comp[2*i] < comp[2*i+1]:
            res.append('1')
        else:
            res.append('0')
    print(' '.join(res))

if __name__ == "__main__":
    solve()