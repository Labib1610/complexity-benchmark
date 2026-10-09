import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
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
    sets = [[], []]
    
    for i in range(1, n + 1):
        if color[i] == 0:
            stack = [i]
            color[i] = 1
            sets[0].append(i)
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        sets[color[v] - 1].append(v)
                        stack.append(v)
    
    if len(sets[0]) >= k:
        print("YES")
        print(' '.join(map(str, sets[0][:k])))
    elif len(sets[1]) >= k:
        print("YES")
        print(' '.join(map(str, sets[1][:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()