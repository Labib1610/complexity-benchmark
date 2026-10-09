import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    edges = []
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        edges.append((u, v))
        idx += 2
        
    # The identity assignment p_i = i minimizes the sum of |p_u - p_v|
    # because |u - v| < n guarantees that the edges form a subgraph of a 
    # Hamiltonian path, which is a forest of caterpillars. 
    # For such graphs, the identity permutation is an optimal linear arrangement.
    min_power = sum(abs(u - v) for u, v in edges)
    
    if min_power <= B:
        print("YES")
        print(" ".join(map(str, range(1, n + 1))))
    else:
        print("NO")

if __name__ == '__main__':
    solve()