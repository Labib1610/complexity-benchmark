import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate to find the lexicographically smallest triplet
    for a in range(1, n - 1):
        # We need b > a such that (a, b) is an edge
        # To get lex smallest, we iterate b in increasing order
        # We can iterate through adj[a] and filter for b > a, then sort
        # However, sorting neighbors for every a might be costly if degrees are high.
        # But total edges is 2*m, and sorting subsets is generally acceptable.
        # Optimization: Iterate b from a+1 to n and check if b in adj[a].
        # This is O(N) per a, total O(N^2) which is 4*10^6, acceptable.
        
        for b in range(a + 1, n):
            if b in adj[a]:
                # Found edge (a, b). Now find c > b with edges (a, c) and (b, c).
                for c in range(b + 1, n + 1):
                    if c in adj[a] and c in adj[b]:
                        print(a, b, c)
                        return

if __name__ == '__main__':
    solve()