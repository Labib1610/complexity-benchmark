import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    M = int(data[idx+1])
    T = int(data[idx+2])
    m = int(data[idx+3])
    idx += 4
    
    # Build graph
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        graph[a].append(b)
        indegree[b] += 1
    
    # Topological sort with day assignment
    queue = deque()
    day = [0] * (n + 1)
    
    # Find all nodes with indegree 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    # Process nodes in topological order
    days_used = [0] * (T + 1)  # count of injections per day
    order = []
    
    while queue:
        u = queue.popleft()
        order.append(u)
        
        # Assign the earliest possible day
        best_day = 1
        for v in graph[u]:
            if day[v] > 0:
                best_day = max(best_day, day[v])
        
        # Find the first day where we can place u
        d = max(1, best_day)
        while d <= T and days_used[d] >= M:
            d += 1
            
        if d > T:
            print("NO")
            return
            
        day[u] = d
        days_used[d] += 1
        
        # Update neighbors
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    # Check if all nodes were processed
    if len(order) != n:
        print("NO")
        return
    
    # Verify all constraints
    for i in range(1, n + 1):
        if day[i] == 0:
            print("NO")
            return
        for v in graph[i]:
            if day[v] <= day[i]:
                print("NO")
                return
    
    print("YES")
    print(*day[1:])

if __name__ == "__main__":
    main()