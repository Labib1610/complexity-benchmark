import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    # We'll do BFS/DFS to color components
    from collections import deque
    
    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
    
    # Now we have a valid bipartition.
    # Lexicographically smallest: we want s_i = 1 whenever possible.
    # Since 1 < 2, we try to assign 1 to as many early nodes as possible.
    # But we must respect bipartition: if we set one node to 1, all its neighbors must be 2.
    # We can do this by processing nodes in order and assigning greedily.
    
    # We'll treat color 0 as "can be 1 or 2", color 1 as the opposite.
    # For each component, we can choose which side gets 1.
    # To get lexicographically smallest, for each component, we try to put 1 on the side that contains the smallest index.
    
    comp_id = [-1] * n
    comps = []
    comp_counter = 0
    for i in range(n):
        if comp_id[i] == -1:
            # BFS to collect component
            stack = [i]
            comp_id[i] = comp_counter
            nodes = []
            while stack:
                u = stack.pop()
                nodes.append(u)
                for v in adj[u]:
                    if comp_id[v] == -1:
                        comp_id[v] = comp_counter
                        stack.append(v)
            comps.append(nodes)
            comp_counter += 1
    
    # For each component, decide which color gets 1
    assign = [0] * n  # 0 means not decided yet, will be 1 or 2
    for nodes in comps:
        # Find smallest index in this component
        min_idx = min(nodes)
        # The color of min_idx in our coloring is color[min_idx]
        # We want min_idx to be 1, so:
        # If color[min_idx] == 0, then color 0 -> 1, color 1 -> 2
        # If color[min_idx] == 1, then color 1 -> 1, color 0 -> 2
        if color[min_idx] == 0:
            for u in nodes:
                assign[u] = 1 if color[u] == 0 else 2
        else:
            for u in nodes:
                assign[u] = 1 if color[u] == 1 else 2
    
    print("YES")
    print(" ".join(map(str, assign)))

if __name__ == "__main__":
    solve()