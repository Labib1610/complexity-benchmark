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
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        while queue:
            u = queue.popleft()
            current_color = color[u]
            next_color = 3 - current_color  # flips 1->2, 2->1
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = next_color
                    queue.append(v)
                elif color[v] == current_color:
                    return False
        return True
    
    for i in range(1, n + 1):
        if color[i] == 0:
            if not bfs(i):
                print("NO")
                return
    
    print("YES")
    # To get lexicographically smallest assignment:
    # For each component, if node 1 is in it, we fix its color to 1.
    # If node 1 is not in the component, we can choose.
    # To ensure lex smallest, in each component, 
    # we want the earliest node to be colored 1 if possible.
    
    # Actually, since we process nodes in order and assign the first available color,
    # and we start with color 1, this already ensures lex smallest.
    
    # But to be precise, we can re-assign each component:
    # For each component, find the smallest node, and ensure it gets color 1.
    # But since our BFS already starts with color 1 and processes in order,
    # it should already be lex smallest.
    
    # Let's re-think: we want the lexicographically smallest sequence.
    # That means we want to assign s1=1 if possible, then s2=1 if possible, etc.
    # But we have constraints.
    
    # The proper way is to try to assign each node to 1 first, if not possible then 2,
    # respecting the bipartite constraints.
    
    # But our BFS already does a valid 2-coloring.
    # To make it lex smallest, for each connected component,
    # we can decide whether to flip the colors or not.
    # We want the first node in the component to be 1.
    
    visited_comp = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited_comp[i] and color[i] != 0:
            # This is the first node of a new component
            # If it's already 1, we're good.
            # If it's 2, we need to flip the whole component.
            if color[i] == 2:
                # We need to flip the component
                queue_comp = deque()
                queue_comp.append(i)
                visited_comp[i] = True
                color[i] = 1
                while queue_comp:
                    u = queue_comp.popleft()
                    current_color = color[u]
                    next_color = 3 - current_color
                    for v in adj[u]:
                        if not visited_comp[v]:
                            visited_comp[v] = True
                            if color[v] == current_color:
                                color[v] = next_color
                            else:
                                color[v] = current_color
                            queue_comp.append(v)
    
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()