import sys
sys.setrecursionlimit(300000)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # For each dish i, we have two variables:
    # i*2 represents dish i is SPICY
    # i*2+1 represents dish i is MILD
    # Given a literal l:
    # if l > 0: dish l is SPICY => variable (l-1)*2
    # if l < 0: dish -l is MILD => variable (-l-1)*2+1
    def var(l):
        if l > 0:
            return (l - 1) * 2
        else:
            return (-l - 1) * 2 + 1
    
    # The inverse: given a variable, what literal does it represent?
    def inv_var(v):
        dish = v // 2 + 1
        if v % 2 == 0:
            return dish
        else:
            return -dish
    
    clauses = []
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        clauses.append((var(l1), var(l2)))
    
    # We'll use 2-SAT solver approach with Kosaraju's algorithm for SCC
    # Number of variables: 2*n (n dishes, each can be SPICY or MILD)
    # Variables: 0 to 2*n - 1
    
    # Build implication graph
    # Each clause (a OR b) is equivalent to (~a -> b) AND (~b -> a)
    adj = [[] for _ in range(2 * n)]
    adj_rev = [[] for _ in range(2 * n)]
    
    for a, b in clauses:
        # ~a -> b  which is (a^1) -> b
        adj[a ^ 1].append(b)
        adj_rev[b].append(a ^ 1)
        # ~b -> a  which is (b^1) -> a
        adj[b ^ 1].append(a)
        adj_rev[a].append(b ^ 1)
    
    # Kosaraju's algorithm
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on transpose graph
    visited = [False] * (2 * n)
    components = [-1] * (2 * n)
    component_id = 0
    
    def dfs2(u):
        visited[u] = True
        components[u] = component_id
        for v in adj_rev[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            component_id += 1
    
    # Check if satisfiable
    # For each variable x, x and ~x should not be in the same SCC
    for i in range(n):
        spicy = i * 2
        mild = i * 2 + 1
        if components[spicy] == components[mild]:
            print("NO")
            return
    
    # Assign values: variables in later finishing times of DFS1 get True
    # In Kosaraju, the component_id increases with finishing time in reverse
    # So higher component_id was discovered later in the first DFS
    assignment = [False] * n
    
    # To determine value, we check which of x or ~x has higher component_id
    for i in range(n):
        spicy = i * 2
        mild = i * 2 + 1
        if components[spicy] > components[mild]:
            assignment[i] = True  # SPICY
        else:
            assignment[i] = False # MILD
    
    print("YES")
    print(' '.join(str(int(x)) for x in assignment))

if __name__ == "__main__":
    main()