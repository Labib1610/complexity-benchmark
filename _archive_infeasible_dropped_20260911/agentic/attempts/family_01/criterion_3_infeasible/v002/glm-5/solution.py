import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        
    best_a = n + 1
    best_b = n + 1
    best_c = n + 1
    
    for a in range(1, n + 1):
        if best_a < a:
            break
        neighbors_a = adj[a]
        for b in neighbors_a:
            if b <= a:
                continue
            if best_a < a or (best_a == a and best_b < b):
                break
            neighbors_b = adj[b]
            for c in neighbors_a:
                if c <= b:
                    continue
                if c in neighbors_b:
                    if a < best_a or (a == best_a and b < best_b) or (a == best_a and b == best_b and c < best_c):
                        best_a = a
                        best_b = b
                        best_c = c
                    break
                    
    print(best_a, best_b, best_c)

if __name__ == '__main__':
    solve()