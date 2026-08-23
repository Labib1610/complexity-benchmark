import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency matrix for O(1) lookup. 
    # n is up to 2000, so n^2 is 4*10^6, which fits in memory.
    # Using a bytearray or a list of lists.
    adj_matrix = [bytearray(n + 1) for _ in range(n + 1)]
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1
        # Store edges such that u < v to simplify search
        if u < v:
            adj_list[u].append(v)
        else:
            adj_list[v].append(u)
            
    # Sort adjacency lists to ensure lexicographical order
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # We need the lexicographically smallest triplet (a, b, c) with a < b < c.
    # Iterate a from 1 to n, then b from neighbors of a (where b > a),
    # then check if any neighbor c of b (where c > b) is also a neighbor of a.
    for a in range(1, n + 1):
        neighbors_a = adj_list[a]
        # To optimize, we can iterate through the sorted neighbors of a as potential b's
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Now we need c such that c > b and c is connected to both a and b.
            # Since we want the smallest c, we check neighbors of b that are > b.
            # However, it's faster to check neighbors of a that are > b.
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                # We already know a < b < c and (a,b), (a,c) are edges.
                # Just check if (b,c) is an edge.
                if adj_matrix[b][c]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()