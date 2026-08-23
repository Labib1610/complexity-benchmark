import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        
    for a in range(1, n - 1):
        for b in adj[a]:
            if b <= a:
                continue
            for c in adj[b]:
                if c <= b:
                    continue
                if c in adj[a]:
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()