import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 2-SAT setup
    # Variable i (1-based):
    # True is 2*(i-1)
    # False is 2*(i-1) + 1
    num_nodes = 2 * n
    head = [-1] * num_nodes
    to = []
    nxt = []
    
    head_rev = [-1] * num_nodes
    to_rev = []
    nxt_rev = []
    
    def add_edge(u, v):
        nxt.append(head[u])
        head[u] = len(to)
        to.append(v)
        
        nxt_rev.append(head_rev[v])
        head_rev[v] = len(to_rev)
        to_rev.append(u)

    def literal_to_node(lit):
        if lit > 0:
            return 2 * (lit - 1)
        else:
            return 2 * (-lit - 1) + 1

    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        
        u_node = literal_to_node(u)
        v_node = literal_to_node(v)
        
        # (u or v) <=> (~u => v) and (~v => u)
        add_edge(u_node ^ 1, v_node)
        add_edge(v_node ^ 1, u_node)

    # Kosaraju's Algorithm (Iterative)
    visited = [False] * num_nodes
    order = []
    
    for start in range(num_nodes):
        if not visited[start]:
            stack = [(start, head[start])]
            visited[start] = True
            while stack:
                u, e = stack[-1]
                if e != -1:
                    stack[-1] = (u, nxt[e])
                    v = to[e]
                    if not visited[v]:
                        visited[v] = True
                        stack.append((v, head[v]))
                else:
                    order.append(u)
                    stack.pop()

    scc = [-1] * num_nodes
    scc_count = 0
    
    for start in reversed(order):
        if scc[start] == -1:
            stack = [start]
            scc[start] = scc_count
            while stack:
                u = stack.pop()
                e = head_rev[u]
                while e != -1:
                    v = to_rev[e]
                    if scc[v] == -1:
                        scc[v] = scc_count
                        stack.append(v)
                    e = nxt_rev[e]
            scc_count += 1

    ans = [0] * n
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("NO")
            return
        # In Kosaraju, SCC with smaller index appears later in topological order.
        # If scc[true] < scc[false], true has higher topological order, so set to true (1).
        ans[i] = 1 if scc[2 * i] < scc[2 * i + 1] else 0

    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()