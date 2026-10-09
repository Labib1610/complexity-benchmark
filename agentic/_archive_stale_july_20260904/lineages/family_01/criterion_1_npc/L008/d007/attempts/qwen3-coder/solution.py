from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # For each edge (u,v), the condition for stability is:
    # M_{u->v} != M_{v->u}
    # s_u * u + s_v * v != s_v * v + s_u * u
    # This simplifies to: s_u * u + s_v * v != s_v * v + s_u * u
    # Which is always equal, so this approach is wrong.
    # Let's re-examine:
    # M_{u->v} = s_u * v + s_v * u
    # M_{v->u} = s_v * u + s_u * v
    # So M_{u->v} = M_{v->u} always. This seems like a contradiction.
    # Wait, let's read carefully.
    # "The magnitude of the forward pulse from oscillator u to oscillator v is given by M_{u→v} = s_u ⋅ v + s_v ⋅ u"
    # "Similarly, the magnitude of the reverse pulse from oscillator v to oscillator u is M_{v→u} = s_v ⋅ v + s_u ⋅ u"
    # That would mean M_{u->v} = s_u * v + s_v * u
    #                 M_{v->u} = s_v * u + s_u * v
    # These are the same expression, so they are always equal.
    # There must be a typo in the problem statement.
    # Perhaps it should be:
    # M_{u->v} = s_u * v + s_v * u
    # M_{v->u} = s_v * v + s_u * u
    # Then M_{u->v} - M_{v->u} = s_u*v + s_v*u - s_v*v - s_u*u = (s_u - s_v)(v - u)
    # For stability, we need M_{u->v} != M_{v->u}, i.e., (s_u - s_v)(v - u) != 0
    # Since u != v, we have v - u != 0, so we need s_u != s_v.
    # Ah, that makes sense! The condition is simply that adjacent nodes in the graph must have different multipliers.
    # This is a graph coloring problem with 3 colors.
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Graph coloring with 3 colors {1,2,3}
    color = [0] * n  # 0 means uncolored
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    # Try to color the graph using backtracking
    def solve(node):
        if node == n:
            return True
        # To minimize the system signature, try colors in order 1, 2, 3
        for c in [1, 2, 3]:
            if is_safe(node, c):
                color[node] = c
                if solve(node + 1):
                    return True
                color[node] = 0
        return False
    
    if solve(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    main()