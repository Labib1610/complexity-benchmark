import sys
from collections import defaultdict, deque

def is_self_adjoint_product(A, B):
    # Check if (A * B) is self-adjoint, i.e., (A * B) == (A * B)^T
    # Since A and B are 2x2, we can compute the product and check
    # A = [[1, 4], [2, 5]]
    # B = [[5, -4], [-2, 1]]
    
    # Compute A*B
    AB = [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
          [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]
    
    # Check if AB is symmetric (self-adjoint)
    return AB[0][1] == AB[1][0]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [[] for _ in range(n+1)]
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u != v:  # Avoid self-loops
            edges.append((u, v))
            adj[u].append(v)
            adj[v].append(u)
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Define operators
    T1 = [[1, 4], [2, 5]]
    T2 = [[5, -4], [-2, 1]]
    ops = [T1, T2]
    
    # Precompute which operator pairs result in self-adjoint products
    # valid[i][j] = True if Ti * Tj is self-adjoint
    valid = [[False, False], [False, False]]
    for i in range(2):
        for j in range(2):
            if is_self_adjoint_product(ops[i], ops[j]):
                valid[i][j] = True
    
    # Build constraint graph
    # For each edge (u,v), the operators assigned to u and v must satisfy valid[s[u]][s[v]] = True
    # This is a 2-SAT problem
    
    # We'll use graph coloring: each node can be color 0 (T1) or 1 (T2)
    # For each edge, only certain color pairs are allowed
    
    # Build adjacency list for the constraint graph
    # We'll model this as a graph where each node can be 0 or 1
    # and edges represent constraints
    
    # For efficiency, we can model this as a graph where each node has two states (0 and 1)
    # and we check bipartiteness with constraints
    
    # But let's think differently: valid pairs are (0,1) and (1,0) only?
    # Let's compute valid:
    # T1 * T1: [[1,4],[2,5]] * [[1,4],[2,5]] = [[1*1+4*2, 1*4+4*5], [2*1+5*2, 2*4+5*5]] = [[9, 24], [12, 33]]
    # Not symmetric since 24 != 12
    # T1 * T2: [[1,4],[2,5]] * [[5,-4],[-2,1]] = [[1*5+4*(-2), 1*(-4)+4*1], [2*5+5*(-2), 2*(-4)+5*1]] = [[-3, 0], [0, -3]]
    # Symmetric since 0 == 0
    # T2 * T1: [[5,-4],[-2,1]] * [[1,4],[2,5]] = [[5*1+(-4)*2, 5*4+(-4)*5], [(-2)*1+1*2, (-2)*4+1*5]] = [[-3, 0], [0, -3]]
    # Symmetric
    # T2 * T2: [[5,-4],[-2,1]] * [[5,-4],[-2,1]] = [[5*5+(-4)*(-2), 5*(-4)+(-4)*1], [(-2)*5+1*(-2), (-2)*(-4)+1*1]] = [[33, -24], [12, 9]]
    # Not symmetric since -24 != 12
    
    # So valid pairs are (0,1) and (1,0) only
    # This means adjacent nodes must have different operators
    # This is a graph bipartitioning problem
    
    # Check if the graph is bipartite
    color = [-1] * (n+1)
    queue = deque()
    
    # Process each connected component
    for start in range(1, n+1):
        if color[start] == -1:
            queue.append(start)
            color[start] = 0
            while queue:
                u = queue.popleft()
                current_color = color[u]
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - current_color
                        queue.append(v)
                    elif color[v] == current_color:
                        print("NO")
                        return
    
    # If bipartite, assign colors (0 -> 1, 1 -> 2 to match operator numbers)
    assignment = [0] * (n+1)
    for i in range(1, n+1):
        assignment[i] = color[i] + 1
    
    print("YES")
    print(" ".join(map(str, assignment[1:])))

if __name__ == "__main__":
    main()