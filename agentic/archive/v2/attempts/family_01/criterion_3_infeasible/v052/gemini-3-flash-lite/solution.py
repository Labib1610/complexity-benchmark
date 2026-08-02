import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Store conflicts in an adjacency list of sets for O(1) lookups
    # and a sorted adjacency list for iteration
    adj = [[] for _ in range(n + 1)]
    adj_sets = [set() for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        
        adj[u].append(v)
        adj[v].append(u)
        adj_sets[u].add(v)
        adj_sets[v].add(u)
        
    for i in range(1, n + 1):
        adj[i].sort()
        
    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # Iterate through a from 1 to n
    # Iterate through b in sorted adj[a] where b > a
    # Iterate through c in sorted adj[a] and check if c in adj[b] where c > b
    
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        for b in neighbors_a:
            if b <= a:
                continue
            
            # We want to find smallest c > b such that c is in adj[a] and adj[b]
            # Since adj[a] is sorted, we can iterate through it
            for c in neighbors_a:
                if c <= b:
                    continue
                if c in adj_sets[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()