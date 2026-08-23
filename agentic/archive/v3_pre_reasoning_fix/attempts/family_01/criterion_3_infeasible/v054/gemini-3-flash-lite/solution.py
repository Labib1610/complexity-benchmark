import sys

def solve():
    # Use fast I/O
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
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # We want the lexicographically smallest (a, b, c) with a < b < c
    # Iterate a from 1 to n-2
    for a in range(1, n - 1):
        # Get neighbors of a that are > a
        neighbors_a = sorted([x for x in adj[a] if x > a])
        
        # Iterate b in neighbors of a
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            
            # Now we need a c such that b < c and c is a neighbor of both a and b
            # To be lexicographically smallest, we check neighbors of b that are > b
            # and also in neighbors of a
            neighbors_b = adj[b]
            
            # We can find common neighbors by intersecting sorted lists or checking
            # Since we want the smallest c, iterate through neighbors_b > b
            potential_c = [x for x in neighbors_b if x > b and x in adj[a]]
            
            if potential_c:
                c = min(potential_c)
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()