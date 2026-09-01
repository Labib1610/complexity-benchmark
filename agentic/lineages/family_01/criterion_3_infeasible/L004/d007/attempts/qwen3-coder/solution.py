import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2

    # Function to compute stability characteristic
    def stability_characteristic(nodes):
        # nodes is a sorted list of 3 elements
        u1, u2, u3 = nodes
        # Build 3x3 matrix Z
        Z = [[0]*3 for _ in range(3)]
        # Map node labels to indices
        node_to_index = {u1:0, u2:1, u3:2}
        node_list = [u1, u2, u3]
        
        # Fill the matrix
        for i in range(3):
            for j in range(3):
                if i == j:
                    Z[i][j] = 1
                else:
                    # Check if there's an edge between node_list[i] and node_list[j]
                    if node_list[j] in adj[node_list[i]]:
                        Z[i][j] = 0
                    else:
                        Z[i][j] = 1
        
        # Now compute Z^5 and return trace
        # Matrix multiplication for 3x3 matrices
        def mat_mult(A, B):
            C = [[0]*3 for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        C[i][j] += A[i][k] * B[k][j]
            return C
        
        # Compute Z^5
        current = Z
        # Z^1
        Z1 = current
        # Z^2
        Z2 = mat_mult(Z1, Z1)
        # Z^3
        Z3 = mat_mult(Z2, Z1)
        # Z^4
        Z4 = mat_mult(Z3, Z1)
        # Z^5
        Z5 = mat_mult(Z4, Z1)
        
        # Trace is sum of diagonal
        trace = Z5[0][0] + Z5[1][1] + Z5[2][2]
        return trace

    # Iterate through all combinations of 3 nodes, in lexicographical order
    # To ensure the correct tie-breaking, we generate combinations in sorted order
    candidates = []
    for comb in combinations(range(1, n+1), 3):
        u1, u2, u3 = sorted(comb)
        if stability_characteristic([u1, u2, u3]) == 3:
            candidates.append((u1, u2, u3))
    
    # Since combinations generates in lexicographical order, the first one is the answer
    res = candidates[0]
    print(res[0], res[1], res[2])

if __name__ == "__main__":
    main()