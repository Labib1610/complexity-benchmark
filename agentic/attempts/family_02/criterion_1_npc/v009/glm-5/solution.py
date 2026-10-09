import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 2-SAT variables:
    # Switch i ON is represented by 2*i
    # Switch i OFF is represented by 2*i + 1
    N = 2 * n
    
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    
    def add_implication(u, v):
        adj[u].append(v)
        radj[v].append(u)
        
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx+1])
        l3 = int(input_data[idx+2])
        idx += 3
        
        # Map condition to 2-SAT variable index
        # Positive li -> switch |li| ON -> 2*(|li|-1)
        # Negative li -> switch |li| OFF -> 2*(|li|-1) + 1
        def get_node(x):
            i = abs(x) - 1
            return 2 * i if x > 0 else 2 * i + 1
            
        u1 = get_node(l1)
        u2 = get_node(l2)
        u3 = get_node(l3)
        
        # A rule (u1 OR u2 OR u3) translates to three implications:
        # NOT u1 => u2
        # NOT u2 => u3
        # NOT u3 => u1
        add_implication(u1 ^ 1, u2)
        add_implication(u2 ^ 1, u3)
        add_implication(u3 ^ 1, u1)
        
    # Kosaraju's algorithm to find Strongly Connected Components
    visited = [False] * N
    order = []
    
    def dfs1(v):
        stack = [(v, 0)]
        while stack:
            node, state = stack.pop()
            if state == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        stack.append((neighbor, 0))
            else:
                order.append(node)
                
    for i in range(N):
        if not visited[i]:
            dfs1(i)
            
    comp_id = [-1] * N
    def dfs2(v, cid):
        stack = [v]
        comp_id[v] = cid
        while stack:
            node = stack.pop()
            for neighbor in radj[node]:
                if comp_id[neighbor] == -1:
                    comp_id[neighbor] = cid
                    stack.append(neighbor)
                    
    cid = 0
    for v in reversed(order):
        if comp_id[v] == -1:
            dfs2(v, cid)
            cid += 1
            
    # Check for contradictions and assign values
    assignment = [0] * n
    for i in range(n):
        on_node = 2 * i
        off_node = 2 * i + 1
        if comp_id[on_node] == comp_id[off_node]:
            print("NO")
            return
        # If ON component is assigned later than OFF component, it evaluates to True
        if comp_id[on_node] > comp_id[off_node]:
            assignment[i] = 1
        else:
            assignment[i] = 0
            
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == '__main__':
    solve()