import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    color = [-1] * n
    bipartite = True
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                bipartite = False
                break
    
    if not bipartite:
        print("NO")
        return
    
    # Check if the solution satisfies the 2-hour sync condition
    # For each edge (u,v), the maintenance times must overlap for exactly 2 hours
    # Window 1: [0,2), Window 2: [1,3)
    # Overlap(Window 1, Window 1) = [0,2) ∩ [0,2) = [0,2) => length 2
    # Overlap(Window 1, Window 2) = [0,2) ∩ [1,3) = [1,2) => length 1
    # Overlap(Window 2, Window 1) = [1,3) ∩ [0,2) = [1,2) => length 1
    # Overlap(Window 2, Window 2) = [1,3) ∩ [1,3) = [1,3) => length 2
    
    # So for the sync check to be active for exactly 2 hours,
    # we need the overlap to be exactly 1 hour where only one is maintained.
    # Wait, let's re-read the problem.
    
    # "The sync check is active during any time when exactly one of the two linked servers is undergoing maintenance"
    # "The total accumulated time during which the sync check is active for that pair must be exactly 2 hours."
    
    # Let's think about when exactly one is under maintenance:
    # If both are in same window: overlap is 2 hours, so neither is exclusively under maintenance => sync time = 0
    # If one in window 1 and one in window 2:
    #   Window 1: [0,2)
    #   Window 2: [1,3)
    #   Time when only window 1 is active: [0,1) => length 1
    #   Time when only window 2 is active: [2,3) => length 1
    #   Total sync time = 1 + 1 = 2 hours. This works!
    
    # Therefore, for each edge, the two endpoints must be assigned DIFFERENT windows.
    # This means we need a bipartite coloring where adjacent nodes have different colors.
    # We already did that.
    
    # The assignment should be such that color 0 -> window 1, color 1 -> window 2
    # Or vice versa. We want the lexicographically smallest.
    
    # To get lex smallest, for each component, we can choose whether to map 0->1 and 1->2 or 0->2 and 1->1.
    # But since we want lex smallest, and we process nodes in order, for each component,
    # we should ensure node 0 (if in this component) gets window 1.
    
    # Actually, our BFS already gives a fixed coloring once we start from a node.
    # To ensure lex smallest, we can do the following:
    # For each connected component, the first node (smallest index) should get window 1.
    # That means if color[first_node] == 1, we flip all colors in that component.
    
    # But actually, in our current approach, we start BFS from the first unvisited node,
    # and arbitrarily assign it color 0. To make it lex smallest, 
    # we should ensure that in the final assignment, node 0 gets window 1 if possible.
    
    # Let's rebuild the logic:
    visited = [False] * n
    final_color = [-1] * n
    
    for i in range(n):
        if not visited[i]:
            # Do BFS to get component
            component = []
            queue = deque()
            queue.append(i)
            visited[i] = True
            component.append(i)
            temp_color = {i: 0}
            
            is_bipartite = True
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        temp_color[v] = temp_color[u] ^ 1
                        queue.append(v)
                        component.append(v)
                    elif temp_color[v] == temp_color[u]:
                        is_bipartite = False
            
            if not is_bipartite:
                print("NO")
                return
                
            # Decide mapping for this component to minimize lex order
            # We want the first node in component to have window 1 if possible
            first_node = min(component)
            current_color_of_first = temp_color[first_node]
            # Map current_color_of_first -> 0 (window 1), the other -> 1 (window 2)
            # Or if that makes first node get window 2, try the reverse
            # Actually, we want first node to get window 1, i.e., final_color[first_node] = 0
            # final_color = 0 means window 1
            # temp_color[first_node] can be 0 or 1
            # If temp_color[first_node] == 0, map 0->0, 1->1 (window 1->1, 2->2) 
            # If temp_color[first_node] == 1, map 1->0, 0->1 (window 2->1, 1->2)
            
            for node in component:
                if temp_color[first_node] == 0:
                    final_color[node] = temp_color[node]
                else:
                    final_color[node] = temp_color[node] ^ 1
    
    # Convert final_color to window assignments
    # final_color 0 -> window 1
    # final_color 1 -> window 2
    result = []
    for c in final_color:
        if c == 0:
            result.append('1')
        else:
            result.append('2')
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()