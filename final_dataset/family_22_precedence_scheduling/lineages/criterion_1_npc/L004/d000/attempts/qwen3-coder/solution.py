from collections import defaultdict, deque

def solve():
    n, M, T, m = map(int, input().split())
    
    # Build graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    
    # Topological sort with room assignment
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    # Room assignment: room[i] is the room number for relic i
    room = [0] * (n + 1)
    room_count = [0] * (T + 1)  # Number of relics in each room
    
    # Process nodes in topological order
    while queue:
        current = queue.popleft()
        
        # Find the earliest room where we can place this relic
        # It must be after all its predecessors
        min_room = 1
        for pred in graph:
            if current in graph[pred]:
                min_room = max(min_room, room[pred] + 1)
        
        # Try to place in the earliest valid room
        placed = False
        for r in range(min_room, T + 1):
            if room_count[r] < M:
                room[current] = r
                room_count[r] += 1
                placed = True
                break
        
        if not placed:
            print("NO")
            return
    
    # Check if all relics were placed
    for i in range(1, n + 1):
        if room[i] == 0:
            print("NO")
            return
    
    # Verify topological constraints
    for i in range(1, n + 1):
        for j in graph[i]:
            if room[i] >= room[j]:
                print("NO")
                return
    
    print("YES")
    print(*room[1:])

solve()