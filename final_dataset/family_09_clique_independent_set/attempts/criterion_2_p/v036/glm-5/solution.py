import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            stack = [i]
            color[i] = 1
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
    
    cnt = [0, 0, 0]
    for i in range(1, n + 1):
        cnt[color[i]] += 1
    
    if cnt[1] >= k:
        print("YES")
        res = []
        for i in range(1, n + 1):
            if color[i] == 1:
                res.append(i)
                if len(res) == k:
                    break
        print(' '.join(map(str, res)))
    elif cnt[2] >= k:
        print("YES")
        res = []
        for i in range(1, n + 1):
            if color[i] == 2:
                res.append(i)
                if len(res) == k:
                    break
        print(' '.join(map(str, res)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()