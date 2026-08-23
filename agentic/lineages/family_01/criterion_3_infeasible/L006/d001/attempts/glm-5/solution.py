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
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for lexicographical processing
    adj_lists = [sorted(adj[i]) for i in range(n + 1)]
    
    # Iterate over all pairs (a, b) with a < b
    # For each pair, check if they are connected, then find common neighbor c > b
    for a in range(1, n - 1):
        for b in adj_lists[a]:
            if b <= a:
                continue
            # We have edge a-b, now find c in intersection of adj[a] and adj[b] such that c > b
            # Since adj_lists are sorted, we can use two pointers
            list_a = adj_lists[a]
            list_b = adj_lists[b]
            i = 0
            j = 0
            len_a = len(list_a)
            len_b = len(list_b)
            
            # Advance i to first element > b in list_a
            while i < len_a and list_a[i] <= b:
                i += 1
            # Advance j to first element > b in list_b
            while j < len_b and list_b[j] <= b:
                j += 1
            
            # Find intersection
            while i < len_a and j < len_b:
                if list_a[i] == list_b[j]:
                    c = list_a[i]
                    print(f"{a} {b} {c}")
                    return
                elif list_a[i] < list_b[j]:
                    i += 1
                else:
                    j += 1
    
    # Should not reach here as per problem statement
    print("-1 -1 -1")

if __name__ == "__main__":
    solve()