import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    # The determinant condition det([[c_u, c_v],[1,1]]) != 0
    # simplifies to c_u != c_v. So we need a proper 3-coloring.
    # To minimize the hash sum c_i * 2^(2n-2i), we greedily assign
    # the smallest valid color to each node in order 1..n.
    
    color = [0] * n
    for i in range(n):
        used = [False] * 4
        for j in adj[i]:
            if j < i:
                used[color[j]] = True
        for c in (1, 2, 3):
            if not used[c]:
                color[i] = c
                break
        else:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()