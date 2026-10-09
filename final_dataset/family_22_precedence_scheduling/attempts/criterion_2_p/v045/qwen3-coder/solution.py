import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 2
    
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, n+1))))
        return
    
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        graph[x].append(y)
        indegree[y] += 1
    
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
    
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) != n:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()