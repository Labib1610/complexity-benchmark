import sys
import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    color = [-1] * n
    comp = []
    ok = True

    # Check self-loops
    for u, v in edges:
        if u == v:
            print("NO")
            return

    # BFS to check bipartite and assign colors
    from collections import deque
    for i in range(n):
        if color[i] == -1:
            q = deque([i])
            color[i] = 0
            comp.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return

    # Now we have a bipartite graph, but we need lexicographically smallest assignment
    # The condition is: for edge (u,v), we need Re(c_u * c_v) > 0
    # c=3+4i or 3-4i. Let's compute:
    # If s=1: c=3+4i, if s=2: c=3-4i
    # Re(c_u * c_v) = Re(c_u)*Re(c_v) - Im(c_u)*Im(c_v)
    # For s=1: (3,4), for s=2: (3,-4)
    # If both same: 3*3 - 4*4 = 9-16 = -7 <0 -> invalid
    # If different: 3*3 - 4*(-4) = 9+16 = 25 >0 -> valid
    # So adjacent vertices must have different assignments.
    # That's exactly a proper 2-coloring. So any bipartite graph works.
    # Lexicographically smallest: assign 1 to vertex 0 if possible, then greedily.

    # But we already have a valid 2-coloring. We need lexicographically smallest.
    # We can try both colorings and pick lexicographically smaller.
    # However, the graph may be disconnected, so we need to handle each component.
    # For each component, we can flip all colors and choose the one that gives lexicographically smaller result.

    # Let's build the assignment from color: 0->1, 1->2
    res1 = [0]*n
    for i in range(n):
        res1[i] = color[i] + 1

    # Try flipping each component
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            # BFS to get component
            comp_nodes = []
            q = [i]
            visited[i] = True
            while q:
                u = q.pop()
                comp_nodes.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            # Try flipping this component
            # Check if flipping gives lexicographically smaller
            # We'll just try both and pick better
            # But we need to be careful: flipping a component might affect other components? No, components are independent.
            # So for each component, we can decide orientation independently.
            # For lexicographically smallest, for each component, we want the smallest possible values at the smallest indices.
            # Since components are independent, we can just try both orientations for each component and choose the one that gives lexicographically smaller result for the whole array.
            pass

    # Simpler: Since the graph is bipartite, we can just do a BFS/DFS and assign colors greedily.
    # But we need lexicographically smallest. We can do a BFS from vertex 0, and for each unvisited vertex, try to assign 1 if possible.
    # Actually, we can just do a BFS and assign colors, but for lexicographically smallest, we need to be careful.
    # Let's do a BFS and assign colors, but when we have a choice (i.e., when we start a new component), we assign 1.
    # That should give lexicographically smallest because we process vertices in order.

    # Let's redo with BFS and assign 1 to the first vertex of each component.
    color2 = [-1]*n
    for i in range(n):
        if color2[i] == -1:
            color2[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color2[v] == -1:
                        color2[v] = color2[u] ^ 1
                        q.append(v)
                    elif color2[v] == color2[u]:
                        print("NO")
                        return

    # Now color2 is a valid 2-coloring. But is it lexicographically smallest?
    # Not necessarily, because we might have flipped a component. But since we start each component with 0, and we process vertices in order, this should be lexicographically smallest.
    # Let's verify with example 1: n=4, edges: 1-2,2-3,3-4,1-4. This is a cycle of length 4, bipartite.
    # BFS from 1: color[1]=0, neighbors 2,4 -> color[2]=1, color[4]=1. Then from 2: neighbor 3 -> color[3]=0. So colors: [0,1,0,1] -> assignments: [1,2,1,2] which matches output.

    # Example 2: triangle, not bipartite -> NO.

    # So the answer is just color2+1
    print("YES")
    print(' '.join(str(c+1) for c in color2))

if __name__ == "__main__":
    solve()