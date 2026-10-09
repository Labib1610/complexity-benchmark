import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        adj[u].add(v)
        adj[v].add(u)
        
    for a in range(1, n + 1):
        for b in adj[a]:
            if b > a:
                for c in adj[a]:
                    if c > b and c in adj[b]:
                        print(a, b, c)
                        return

if __name__ == '__main__':
    solve()