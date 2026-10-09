import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n, m = map(int, input[ptr:ptr+2])
    ptr +=2
    
    adj = [set() for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input[ptr:ptr+2])
        ptr +=2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a < b < c such that a is connected to b and c, and b is connected to c.
    # Iterate a from 1 to n, then for each a, iterate b in adj[a] where b > a, then c in adj[a] where c > b, and check if c is in adj[b].
    for a in range(1, n+1):
        neighbors_a = sorted(adj[a])
        len_a = len(neighbors_a)
        for i in range(len_a):
            b = neighbors_a[i]
            if b <= a:
                continue
            for j in range(i+1, len_a):
                c = neighbors_a[j]
                if c <= b:
                    continue
                if c in adj[b]:
                    print(a, b, c)
                    return
    # Shouldn't reach here per problem statement
    print(-1, -1, -1)

solve()