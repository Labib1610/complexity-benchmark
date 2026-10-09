import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n_L = int(input_data[0])
    n_R = int(input_data[1])
    m = int(input_data[2])
    
    if m == 0:
        print("YES")
        print()
        return
        
    edges = []
    for i in range(m):
        u = int(input_data[3 + 2*i])
        v = int(input_data[3 + 2*i + 1])
        edges.append((u, v))
        
    deg_L = [0] * (n_L + 1)
    deg_R = [0] * (n_R + 1)
    for u, v in edges:
        deg_L[u] += 1
        deg_R[v] += 1
        
    Delta = max(max(deg_L), max(deg_R))
    
    if Delta == 0:
        print("YES")
        print()
        return
        
    adj_L = [[] for _ in range(n_L + 1)]
    adj_R = [[] for _ in range(n_R + 1)]
    for i, (u, v) in enumerate(edges):
        adj_L[u].append((v, i))
        adj_R[v].append((u, i))
        
    ans = [0] * m
    
    for u in range(1, n_L + 1):
        if not adj_L[u]:
            continue
        used = set()
        for v, idx in adj_L[u]:
            ans[idx] = deg_L[u]
            used.add(deg_L[u])
            deg_L[u] -= 1
            
        k = 1
        for v, idx in adj_L[u]:
            if ans[idx] == 0:
                while k in used:
                    k += 1
                ans[idx] = k
                k += 1
                
    for v in range(1, n_R + 1):
        if not adj_R[v]:
            continue
        used = set()
        for u, idx in adj_R[v]:
            if ans[idx] <= deg_R[v]:
                used.add(ans[idx])
                
        k = 1
        for u, idx in adj_R[v]:
            if ans[idx] > deg_R[v]:
                while k in used:
                    k += 1
                ans[idx] = k
                used.add(k)
                k += 1
                
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    solve()