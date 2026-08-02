from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    g = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, stdin.readline().split())
        g[u].append(v)
        g[v].append(u)

    d = [2] * n
    s = set([i for i in range(n)])
    
    while len(s):
        v = min(s)
        ns = []
        
        if len(g[v]) == 0:
            d[v] = 1
        
        for w in g[v]:
            if d[w] != 2:
                continue
            if d[v] == 1:
                d[w] = 2
            else:
                d[w] = 1
            ns.append(w)
        
        s -= set([v])
        s |= set(ns)

    ok = True
    
    for v in range(n):
        for w in g[v]:
            if d[v] == d[w]:
                print("NO")
                return
    
    print("YES")
    print(*d)

if __name__ == "__main__":
    main()