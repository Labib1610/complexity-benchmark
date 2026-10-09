import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    in_degree = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        in_degree[b] += 1
        
    q = []
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)
            
    step = [1] * n
    cnt = [0] * (T + 2)
    
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        
        s = step[u]
        cnt[s] += 1
        
        if s > T:
            print("NO")
            return
            
        for v in adj[u]:
            if step[v] < s + 1:
                step[v] = s + 1
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
                
    if len(q) < n:
        print("NO")
        return
        
    for s in range(1, T + 1):
        if cnt[s] > M:
            print("NO")
            return
            
    print("YES")
    print(" ".join(str(x) for x in step))

if __name__ == '__main__':
    solve()