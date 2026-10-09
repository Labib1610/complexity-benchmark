import sys

def solve():
    input = sys.stdin.read
    data = input().split()
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
        adj[u ^ 1].append(v)
        adj[v ^ 1].append(u)
        
    sys.setrecursionlimit(1 << 25)
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            curr, idx = stack[-1]
            if not visited[curr]:
                visited[curr] = True
            if idx < len(adj[curr]):
                stack[-1] = (curr, idx + 1)
                v = adj[curr][idx]
                if not visited[v]:
                    stack.append((v, 0))
            else:
                stack.pop()
                order.append(curr)
                
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
            
    comp_id = [-1] * (2 * n)
    current_id = 0
    
    def dfs2(u, current_id):
        stack = [u]
        comp_id[u] = current_id
        while stack:
            curr = stack[-1]
            unvisited_child = False
            for v in adj[curr]:
                if comp_id[v] == -1:
                    comp_id[v] = current_id
                    stack.append(v)
                    unvisited_child = True
                    break
            if not unvisited_child:
                stack.pop()
                
    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, current_id)
            current_id += 1
            
    assignment = [0] * n
    for i in range(n):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            print("NO")
            return
        if comp_id[2 * i] > comp_id[2 * i + 1]:
            assignment[i] = 1
            
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == '__main__':
    solve()