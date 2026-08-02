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
        
    # Convert sets to sorted lists for faster iteration
    adj_list = [sorted(list(s)) for s in adj]
    
    # We need to find the lexicographically smallest (a, b, c) with a < b < c
    # Iterate a from 1 to n-2
    for a in range(1, n + 1):
        # Iterate b from a+1 to n-1
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # Check if there exists c > b such that c is connected to both a and b
            # Intersection of adj[a] and adj[b] gives common neighbors
            # We need the smallest c > b
            common = set(adj_list[a]) & set(adj_list[b])
            
            # Find the smallest c > b in the common set
            best_c = float('inf')
            found = False
            for c in common:
                if c > b:
                    if c < best_c:
                        best_c = c
                        found = True
            
            if found:
                print(f"{a} {b} {best_c}")
                return

if __name__ == '__main__':
    solve()