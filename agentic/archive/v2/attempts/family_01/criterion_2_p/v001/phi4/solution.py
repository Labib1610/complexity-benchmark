import sys
input = sys.stdin.read

def solve():
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    restrictions = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        restrictions.append((u, v))
        index += 2
    
    # Create adjacency list and degree count for each member
    adj_list = {i: [] for i in range(1, n + 1)}
    degree = [0] * (n + 1)
    
    for u, v in restrictions:
        adj_list[u].append(v)
        adj_list[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Topological sort to find valid assignment
    from collections import deque
    
    team = [0] * (n + 1)  # 0: unassigned, 1: team 1, 2: team 2
    in_degree = [0] * (n + 1)
    
    for u in adj_list:
        for v in adj_list[u]:
            in_degree[v] += 1
    
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            team[i] = 1
    
    while queue:
        u = queue.popleft()
        current_team = team[u]
        opposite_team = 3 - current_team
        for v in adj_list[u]:
            if team[v] == 0:
                team[v] = opposite_team
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
    
    # Check if all members are assigned and no restrictions are violated
    valid = True
    for u, v in restrictions:
        if team[u] == team[v]:
            valid = False
            break
    
    if not valid or any(t == 0 for t in team[1:]):
        print("NO")
    else:
        print("YES")
        result = ' '.join(map(str, team[1:]))
        print(result)

solve()