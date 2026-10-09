import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    B = int(data[2])
    
    edges = []
    graph = defaultdict(list)
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # Since it's a tree (m = n-1 and connected), we can build the tree from any root
    # We'll build a tree rooted at node 0
    parent = [-1] * n
    children = [[] for _ in range(n)]
    
    visited = [False] * n
    queue = deque()
    queue.append(0)
    visited[0] = True
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                queue.append(v)
    
    # Now we have a tree structure rooted at 0
    # We will try to assign positions to minimize total cable length
    # A good heuristic is to do a BFS layout or DFS layout
    # But to ensure we don't exceed B, we can try a linear assignment that minimizes length
    
    # Let's try assigning nodes in a way that minimizes total length
    # One approach: do an in-order traversal of the tree (as if it's a binary tree)
    # But since it's a general tree, we can do a DFS that tries to keep children close
    
    # Another approach: since it's a tree, we can embed it in a line with minimal stretch
    # The optimal layout for a tree in a line to minimize sum of distances is not trivial
    # But we can use a greedy approach:
    # Assign the root to the middle, then assign children around it
    
    # Let's try a simple DFS-based assignment
    pos = [-1] * n
    
    # We'll do a DFS and assign positions greedily
    # Start by placing root at position 0
    order = []
    stack = [0]
    visited = [False] * n
    visited[0] = True
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v in children[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    # Now assign positions in the order of DFS
    # We'll place nodes as close as possible to their parent
    pos = [-1] * n
    pos[0] = 0  # Place root at position 0
    assigned = [False] * n
    assigned[0] = True
    
    # For each node in order, place it adjacent to its parent
    for u in order:
        for v in children[u]:
            if not assigned[v]:
                # Try to place v next to u
                # We'll need to find a free spot
                # For now, let's just place them in a line
                pass
    
    # Better approach: assign positions in a line based on DFS order
    # This ensures connected nodes are close
    for i in range(n):
        pos[order[i]] = i
    
    # Calculate total cable length
    total_length = 0
    for u, v in edges:
        total_length += abs(pos[u] - pos[v])
    
    # Check if it's within budget
    if total_length <= B:
        # Convert positions to bays (1-based)
        bay = [0] * n
        for i in range(n):
            bay[i] = pos[i] + 1
        # Check for duplicates
        if len(set(bay)) == n:
            print("YES")
            print(*bay)
            return
    
    # If the simple DFS layout doesn't work, try a different approach
    # Try placing nodes in BFS order
    pos = [-1] * n
    order_bfs = []
    queue = deque()
    visited = [False] * n
    queue.append(0)
    visited[0] = True
    
    while queue:
        u = queue.popleft()
        order_bfs.append(u)
        for v in children[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    
    for i in range(n):
        pos[order_bfs[i]] = i
        
    total_length = 0
    for u, v in edges:
        total_length += abs(pos[u] - pos[v])
        
    if total_length <= B:
        bay = [0] * n
        for i in range(n):
            bay[i] = pos[i] + 1
        if len(set(bay)) == n and all(1 <= x <= n for x in bay):
            print("YES")
            print(*bay)
            return
    
    # If both simple layouts fail, try a more sophisticated approach
    # Since it's a tree, we can always layout in a line such that 
    # the total stretch is at most n*(n-1)/2, but we need <= B
    
    # Let's try a DFS layout where we place children in available slots
    def dfs_layout(node, start, end, used):
        mid = (start + end) // 2
        while mid <= end and used[mid]:
            mid += 1
        if mid > end:
            mid = start
            while mid >= 0 and used[mid]:
                mid -= 1
        if mid < 0 or mid > end:
            # Find any free spot
            for i in range(n):
                if not used[i]:
                    mid = i
                    break
        pos[node] = mid
        used[mid] = True
        k = len(children[node])
        if k == 0:
            return
        step = max(1, (end - start) // (k + 1))
        for i, child in enumerate(children[node]):
            new_start = start + i * step
            new_end = start + (i + 1) * step - 1
            dfs_layout(child, new_start, new_end, used)
    
    # This is complex, let's try a simpler greedy assignment
    # Assign nodes to positions 0 to n-1 in the order of a DFS that tries to keep tree compact
    
    # Actually, let's just try all nodes in order 0 to n-1
    pos = list(range(n))
    total_length = 0
    for u, v in edges:
        total_length += abs(pos[u] - pos[v])
        
    if total_length <= B:
        bay = [p + 1 for p in pos]
        print("YES")
        print(*bay)
        return
        
    # Try reverse order
    pos = list(range(n-1, -1, -1))
    total_length = 0
    for u, v in edges:
        total_length += abs(pos[u] - pos[v])
        
    if total_length <= B:
        bay = [p + 1 for p in pos]
        print("YES")
        print(*bay)
        return
    
    # Since it's a tree, there always exists a layout with total length <= n*(n-1)/2
    # But we need <= B. Let's check if B is sufficient at all.
    
    # The minimum possible total length for any tree layout is at least 
    # the sum of distances in an optimal linear arrangement.
    # For a star graph, it's O(n), for a path it's O(n^2).
    
    # Let's compute a better layout using DFS and placing children consecutively
    pos = [-1] * n
    current_pos = 0
    
    def dfs_assign(u):
        nonlocal current_pos
        pos[u] = current_pos
        current_pos += 1
        for v in children[u]:
            dfs_assign(v)
            
    dfs_assign(0)
    
    total_length = 0
    for u, v in edges:
        total_length += abs(pos[u] - pos[v])
        
    if total_length <= B:
        # Create the bay assignment
        bay = [0] * n
        for i in range(n):
            bay[pos[i]] = i + 1
        print("YES")
        print(*bay)
        return
    
    # If this canonical DFS layout doesn't work, it's likely B is too small
    # But let's double-check with a BFS layout
    pos = [-1] * n
    current_pos = 0
    queue = deque([0])
    visited = [False] * n
    visited[0] = True
    pos[0] = current_pos
    current_pos += 1
    
    while queue:
        u = queue.popleft()
        for v in children[u]:
            if not visited[v]:
                visited[v] = True
                pos[v] = current_pos
                current_pos += 1
                queue.append(v)
    
    total_length = 0
    for u, v in edges:
        total_length += abs(pos[u] - pos[v])
        
    if total_length <= B:
        bay = [0] * n
        for i in range(n):
            bay[pos[i]] = i + 1
        print("YES")
        print(*bay)
        return
        
    print("NO")

if __name__ == "__main__":
    main()