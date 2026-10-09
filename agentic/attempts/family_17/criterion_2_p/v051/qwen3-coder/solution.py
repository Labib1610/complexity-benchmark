import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    edges = []
    index = 2
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        edges.append((a, b))
        index += 2

    # Build graph for bipartite matching
    # Left side: 1 to q (acidic)
    # Right side: q+1 to 2*q (alkaline) mapped to 1 to q for easier handling
    adj = defaultdict(list)
    for i in range(t):
        a, b = edges[i]
        b_mapped = b - q  # Map from [q+1, 2q] to [1, q]
        adj[a].append((b_mapped, i))
    
    # Try to find a maximum matching that matches all q nodes on left
    # Use Hopcroft-Karp or similar. But since we just need to check if perfect matching exists,
    # we can use a simple augmenting path approach like Ford-Fulkerson with BFS (Edmonds-Karp style)
    
    # For each node in left (1..q), we want to match it to a node in right (1..q)
    # So this is a standard bipartite matching problem
    
    match_right = [-1] * (q + 1)  # match_right[r] = l means right node r is matched to left node l
    match_left = [-1] * (q + 1)   # match_left[l] = r means left node l is matched to right node r
    
    def bfs():
        dist = [-1] * (q + 1)
        queue = deque()
        for u in range(1, q + 1):
            if match_left[u] == -1:
                dist[u] = 0
                queue.append(u)
        
        found = False
        while queue:
            u = queue.popleft()
            for v_mapped, _ in adj[u]:
                if match_right[v_mapped] != -1 and dist[match_right[v_mapped]] == -1:
                    dist[match_right[v_mapped]] = dist[u] + 1
                    queue.append(match_right[v_mapped])
                elif match_right[v_mapped] == -1:
                    found = True
        return found
    
    def dfs(u):
        for v_mapped, _ in adj[u]:
            if match_right[v_mapped] != -1 and dist[match_right[v_mapped]] == dist[u] + 1:
                if dfs(match_right[v_mapped]):
                    match_right[v_mapped] = u
                    match_left[u] = v_mapped
                    return True
            elif match_right[v_mapped] == -1:
                match_right[v_mapped] = u
                match_left[u] = v_mapped
                return True
        return False
    
    # Hopcroft-Karp main loop
    while bfs():
        for u in range(1, q + 1):
            if match_left[u] == -1:
                dfs(u)
    
    # Check if all left nodes are matched
    if all(match_left[u] != -1 for u in range(1, q + 1)):
        print("YES")
        for u in range(1, q + 1):
            v_mapped = match_left[u]
            # Need to find the original edge index
            # We can store the index in adj
            for v_orig_mapped, idx in adj[u]:
                if v_orig_mapped == v_mapped:
                    a, b = edges[idx]
                    print(a, b)
                    break
    else:
        print("NO")

if __name__ == "__main__":
    main()