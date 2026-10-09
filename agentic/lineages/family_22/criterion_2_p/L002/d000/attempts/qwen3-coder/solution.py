import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        indegree[y] += 1
    
    queue = deque()
    for i in range(1, n + 1):
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
    
    if len(result) == n:
        print("YES")
        print(" ".join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    main()