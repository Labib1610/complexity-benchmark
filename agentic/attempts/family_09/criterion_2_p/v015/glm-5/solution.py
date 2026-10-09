import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0]*(n+1)
    comp = [0]*(n+1)
    comp_cnt = [0,0]
    comp_id = 0
    valid = True
    
    for i in range(1, n+1):
        if color[i] == 0:
            comp_id += 1
            color[i] = 1
            comp[i] = comp_id
            comp_cnt.append(0)
            comp_cnt.append(0)
            comp_cnt[comp_id*2+1] = 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        comp[v] = comp_id
                        comp_cnt[comp_id*2 + color[v]] += 1
                        q.append(v)
                    elif color[v] == color[u]:
                        valid = False
                        break
                if not valid:
                    break
        if not valid:
            break
    
    if not valid:
        print("NO")
        return
    
    total = sum(max(comp_cnt[c*2+1], comp_cnt[c*2+2]) for c in range(1, comp_id+1))
    if k > total:
        print("NO")
        return
    
    print("YES")
    res = []
    rem = k
    for c in range(1, comp_id+1):
        cnt1 = comp_cnt[c*2+1]
        cnt2 = comp_cnt[c*2+2]
        if cnt1 >= cnt2:
            take = min(cnt1, rem)
            target = 1
        else:
            take = min(cnt2, rem)
            target = 2
        rem -= take
        for v in range(1, n+1):
            if take == 0:
                break
            if comp[v] == c and color[v] == target:
                res.append(v)
                take -= 1
        if rem == 0:
            break
    
    print(' '.join(map(str, res)))

solve()