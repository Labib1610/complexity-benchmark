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
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    # Iterate b in sorted order of neighbors of a such that b > a
    # Check if there exists c in neighbors of a such that c > b and c is in neighbors of b
    
    for a in range(1, n + 1):
        neighbors_a = sorted([x for x in adj[a] if x > a])
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # We want smallest c > b such that c is in adj[a] and c is in adj[b]
            # This is equivalent to checking common neighbors of a and b that are > b
            neighbors_b = adj[b]
            
            # Optimization: iterate through the smaller set of neighbors
            if len(neighbors_a) < len(neighbors_b):
                for c in neighbors_a[i+1:]:
                    if c in neighbors_b:
                        print(f"{a} {b} {c}")
                        return
            else:
                # Iterate through neighbors of b that are > b
                potential_c = sorted([x for x in neighbors_b if x > b])
                for c in potential_c:
                    if c in adj[a]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()