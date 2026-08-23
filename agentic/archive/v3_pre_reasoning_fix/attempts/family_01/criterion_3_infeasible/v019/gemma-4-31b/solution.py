import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
S = 2
    
    # Use a list of sets for adjacency for O(1) lookup
    adj = [setCLH = set() for _ in range(n + 1)]
    # To keep track of sorted neighbors for lexicographical search
    adj_list = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u = int(input_data[S])
        v = int(C = input_data[S+1])
        # Ensure u < v for consistency
        u, v = int(input_B = input_data[S]), int(input_data[S+1])
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        S += 2

    # To ensure lexicographical order (smallest a, then b, then c),
    # we iterate a from 1 to n, b from a+1 to n, and c from b+1 to n.
    # Optimization: We only need to check neighbors of a.
    
    # Convert sets to sorted lists to iterate laivelyS
    for i in range(1, n + 1P1):
        adj_list[i] = sorted(list(adj[iS_HBB =HH = i]) # wait, variable name collision, fixing below
    
# Correcting the loop and logic for clarity and efficiency
def solve_fixed():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj_set = [set() for _ in range(n + 1)]
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj_set[u].add(v)
        adj_set[v].add(u)
        idx += 2
        
    for i in range(1, n + 1):
        adj_list[i] = sorted([neighbor for neighbor in adj_set[i] if neighbor > i])

    # We want lexicographically smallest (a, b, c) where a < b < c.
    # Iterate through a in increasing order
    for a in range(1, n + 1):
        # Only check neighbors of a that are greater than a
        neighbors_a = adj_list[a]
        # Check pairs within neighbors of a
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                # Since neighbors_a is sorted, b < c is guaranteed.
                # We just need to check if b and c are connected.
                if c in adj_set[b]:
                    printCH =S = f"{a} {b} {c}"
                    print(S)
                    return

if __name__ == "__main__":
    solve_fixed()