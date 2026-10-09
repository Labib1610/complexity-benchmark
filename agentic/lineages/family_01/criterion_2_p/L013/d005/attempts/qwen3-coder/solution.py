import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    degree = [0] * (n + 1)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        degree[u] += 1
        degree[v] += 1
        index += 2
    
    # The condition for perfect equilibrium is:
    # 3W - 2U = 5m
    # where W = sum(d_i * p_i) and U = sum(p_u * p_v)
    
    # Let's rewrite the condition:
    # 3 * sum(d_i * p_i) - 2 * sum(p_u * p_v) = 5m
    # This is a constraint satisfaction problem.
    
    # Let's consider all p_i are either 1 or 2.
    # We can try to model this as a 2-SAT problem or analyze mathematically.
    
    # Let's derive what the equation means.
    # W = sum of d_i * p_i
    # U = sum of p_u * p_v over all edges
    
    # The condition: 3W - 2U = 5m
    # 3 * sum(d_i * p_i) - 2 * sum(p_u * p_v) = 5m
    
    # Let's consider the contribution of each variable.
    # For each node i, if p_i changes from 1 to 2, the change in W is d_i.
    # For each edge (u,v), if both p_u and p_v change from 1 to 2, the change in U is 3.
    # But this is getting complex. Let's think differently.
    
    # Let's consider a different approach. 
    # Since each p_i is either 1 or 2, let's define x_i = p_i - 1, so x_i is 0 or 1.
    # Then p_i = x_i + 1
    # W = sum(d_i * (x_i + 1)) = sum(d_i * x_i) + sum(d_i)
    # U = sum((x_u + 1)(x_v + 1)) = sum(x_u * x_v + x_u + x_v + 1) 
    #   = sum(x_u * x_v) + sum(x_u) + sum(x_v) + m
    #   = sum(x_u * x_v) + 2 * sum(x_i * degree_i) + m
    
    # So the condition becomes:
    # 3(sum(d_i * x_i) + sum(d_i)) - 2(sum(x_u * x_v) + 2 * sum(x_i * degree_i) + m) = 5m
    # 3*sum(d_i * x_i) + 3*sum(d_i) - 2*sum(x_u * x_v) - 4*sum(x_i * degree_i) - 2m = 5m
    # 3*sum(d_i * x_i) - 2*sum(x_u * x_v) - 4*sum(x_i * degree_i) = 7m - 3*sum(d_i)
    
    # Since d_i = degree_i, we have:
    # 3*sum(degree_i * x_i) - 2*sum(x_u * x_v) - 4*sum(x_i * degree_i) = 7m - 3*sum(degree_i)
    # -sum(degree_i * x_i) - 2*sum(x_u * x_v) = 7m - 3*sum(degree_i)
    # sum(degree_i * x_i) + 2*sum(x_u * x_v) = 3*sum(degree_i) - 7m
    
    # Let S = sum(degree_i) = 2m
    # So the condition is:
    # sum(degree_i * x_i) + 2*sum(x_u * x_v) = 6m - 7m = -m
    
    # This seems problematic because the left side is non-negative but the right side is negative.
    # Wait, let me recheck the derivation.
    
    # Actually, let's go back to the original equation and try small examples.
    
    # For the first example:
    # n=4, m=4, edges = (1,2), (2,3), (3,4), (1,4)
    # degrees: d1=2, d2=2, d3=2, d4=2
    # W = 2*p1 + 2*p2 + 2*p3 + 2*p4
    # U = p1*p2 + p2*p3 + p3*p4 + p1*p4
    # Condition: 3W - 2U = 20
    # 3*(2*p1 + 2*p2 + 2*p3 + 2*p4) - 2*(p1*p2 + p2*p3 + p3*p4 + p1*p4) = 20
    # 6*(p1 + p2 + p3 + p4) - 2*(p1*p2 + p2*p3 + p3*p4 + p1*p4) = 20
    
    # With p = [1,2,1,2], we get:
    # W = 2*1 + 2*2 + 2*1 + 2*2 = 2+4+2+4 = 12
    # U = 1*2 + 2*1 + 1*2 + 1*2 = 2+2+2+2 = 8
    # 3*12 - 2*8 = 36 - 16 = 20. Correct.
    
    # Let's think of this as a quadratic optimization problem with binary variables.
    # It's NP-hard in general, but maybe there's a pattern or we can model it as 2-SAT.
    
    # Let's consider that this might be a special case where we can do a graph check.
    # In fact, let's consider that the condition might simplify to a property of the graph.
    
    # Let's try a different mathematical approach.
    # Let's denote by a the number of nodes with p_i = 2, and b = n - a the number with p_i = 1.
    # Let's also denote:
    # - E_11: number of edges where both endpoints have p=1
    # - E_12: number of edges where one endpoint has p=1 and the other p=2
    # - E_22: number of edges where both endpoints have p=2
    # Then U = E_11 * 1 + E_12 * 2 + E_22 * 4 = E_11 + 2*E_12 + 4*E_22
    # And W = sum(d_i * p_i) = sum_{p_i=1} d_i + 2 * sum_{p_i=2} d_i
    
    # But this is still complex. Let's think of the structure.
    
    # Key insight: let's try to see if the graph must be bipartite.
    # In example 1, the graph is a cycle of length 4, which is bipartite.
    # In example 2, the graph is a triangle, which is not bipartite.
    
    # Let's hypothesize that a solution exists if and only if the graph is bipartite.
    # And in that case, we assign 1 and 2 according to the bipartition, choosing the lex smallest.
    
    # Let's test this hypothesis.
    # For a bipartite graph with parts L and R:
    # If we assign p_i = 1 for i in L and p_i = 2 for i in R:
    # U = number of edges between L and R multiplied by 1*2 = 2 * |E(L,R)|
    # Since it's a bipartite graph, all edges are between L and R, so U = 2*m
    # W = sum_{i in L} d_i * 1 + sum_{i in R} d_i * 2 = sum_{i in L} d_i + 2 * sum_{i in R} d_i
    # sum(d_i) = 2m, so sum_{i in R} d_i = 2m - sum_{i in L} d_i
    # W = sum_{i in L} d_i + 2 * (2m - sum_{i in L} d_i) = sum_{i in L} d_i + 4m - 2 * sum_{i in L} d_i 
    #   = 4m - sum_{i in L} d_i
    # So 3W - 2U = 3*(4m - sum_{i in L} d_i) - 2*(2*m) = 12m - 3*sum_{i in L} d_i - 4m 
    #            = 8m - 3*sum_{i in L} d_i
    
    # For this to equal 5m, we need:
    # 8m - 3*sum_{i in L} d_i = 5m
    # 3*sum_{i in L} d_i = 3m
    # sum_{i in L} d_i = m
    
    # So in a bipartite graph, a solution exists if there is a bipartition where the sum of degrees 
    # in one part is exactly m. Since sum of all degrees is 2m, this means the sum of degrees in 
    # the other part is also m.
    
    # This is a very specific condition. But let's see if it's necessary and sufficient.
    
    # Actually, let's just implement the bipartite check and see.
    
    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Check if the graph is bipartite and find a valid 2-coloring
    color = [-1] * (n + 1)
    visited = [False] * (n + 1)
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        visited[start] = True
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    # Check if the whole graph is bipartite
    is_bipartite = True
    for i in range(1, n + 1):
        if not visited[i]:
            if not bfs(i):
                is_bipartite = False
                break
    
    if not is_bipartite:
        print("NO")
        return
    
    # Now we need to check if there exists a bipartition where sum of degrees in each part is m.
    # Since total degree is 2m, we need sum_L = m and sum_R = m.
    
    # Let's compute the sum of degrees for each part
    sum_0 = 0  # sum of degrees of nodes with color 0
    sum_1 = 0  # sum of degrees of nodes with color 1
    
    for i in range(1, n + 1):
        if color[i] == 0:
            sum_0 += degree[i]
        else:
            sum_1 += degree[i]
    
    if sum_0 == m and sum_1 == m:
        # Valid assignment: color 0 -> 1, color 1 -> 2
        result = []
        for i in range(1, n + 1):
            if color[i] == 0:
                result.append("1")
            else:
                result.append("2")
        print("YES")
        print(" ".join(result))
        return
    else:
        # Try the other way: color 0 -> 2, color 1 -> 1
        if sum_1 == m and sum_0 == m:  # This is the same condition
            result = []
            for i in range(1, n + 1):
                if color[i] == 0:
                    result.append("2")
                else:
                    result.append("1")
            print("YES")
            print(" ".join(result))
            return
        else:
            print("NO")
            return

if __name__ == "__main__":
    main()