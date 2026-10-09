import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(2 * n + 1)]
    
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        
        u = -l1 + n if l1 < 0 else l1
        v = -l2 + n if l2 < 0 else l2
        
        adj[u].append(v)
        adj[v].append(u)
        
    visited = [False] * (2 * n + 1)
    assignment = [0] * (n + 1)
    
    for i in range(1, 2 * n + 1):
        if visited[i]:
            continue
            
        component = []
        stack = [i]
        visited[i] = True
        
        while stack:
            u = stack.pop()
            component.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
                    
        for node in component:
            if node <= n:
                if visited[node + n]:
                    print("NO")
                    return
            else:
                if visited[node - n]:
                    print("NO")
                    return
                    
        for node in component:
            if node <= n:
                assignment[node] = 1
            else:
                assignment[node - n] = 0
                
    print("YES")
    print(" ".join(map(str, assignment[1:])))

if __name__ == '__main__':
    solve()