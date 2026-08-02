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
        
    # To find the lexicographically smallest triple (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    #   Iterate b from a+1 to n-1
    #     If a and b are connected:
    #       Find intersection of neighbors of a and neighbors of b
    #       If any neighbor c > b exists, we found a potential triple
    
    for a in range(1, n - 1):
        # Sort neighbors to try smaller b and c first
        neighbors_a = sorted([x for x in adj[a] if x > a])
        for b in neighbors_a:
            # We want smallest c > b such that c is in adj[a] and adj[b]
            # Intersection of sorted lists
            common = sorted(list(adj[a].intersection(adj[b])))
            for c in common:
                if c > b:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()