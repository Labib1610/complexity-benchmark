import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        u = 2 * (abs(l1) - 1) + (1 if l1 > 0 else 0)
        v = 2 * (abs(l2) - 1) + (1 if l2 > 0 else 0)
        
        not_u = u ^ 1
        not_v = v ^ 1
        
        adj[not_u].append(v)
        adj[not_v].append(u)
    
    N = 2 * n
    visited = [False] * N
    order = []
    
    for i in range(N):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                node, idx = stack[-1]
                if not visited[node]:
                    visited[node] = True
                
                while idx < len(adj[node]) and visited[adj[node][idx]]:
                    idx += 1
                
                if idx < len(adj[node]):
                    stack[-1] = (node, idx + 1)
                    neighbor = adj[node][idx]
                    if not visited[neighbor]:
                        stack.append((neighbor, 0))
                else:
                    stack.pop()
                    order.append(node)
    
    comp_id = [-1] * N
    current_id = 0
    
    radj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            radj[v].append(u)
    
    for u in reversed(order):
        if comp_id[u] == -1:
            stack = [u]
            comp_id[u] = current_id
            while stack:
                curr = stack.pop()
                for v in radj[curr]:
                    if comp_id[v] == -1:
                        comp_id[v] = current_id
                        stack.append(v)
            current_id += 1
    
    assignment = [0] * n
    
    for i in range(n):
        zero_node = 2 * i
        one_node = 2 * i + 1
        if comp_id[zero_node] == comp_id[one_node]:
            print("NO")
            return
        if comp_id[one_node] > comp_id[zero_node]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()