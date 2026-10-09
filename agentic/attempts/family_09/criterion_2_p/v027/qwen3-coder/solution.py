import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, k = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Since the graph is bipartite (frequency isolation property),
    # we can color it with two colors.
    # We'll use BFS to color the graph.
    color = [-1] * (n + 1)  # -1: unvisited, 0: color A, 1: color B
    partition = [[], []]  # partition[0] for color 0, partition[1] for color 1
    
    # Check if the graph is bipartite and get the partitions
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
        queue = deque()
        queue.append(start)
        color[start] = 0
        visited[start] = True
        partition[0].append(start)
        
        while queue:
            u = queue.popleft()
            c = color[u]
            next_c = 1 - c
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = next_c
                    partition[next_c].append(v)
                    queue.append(v)
                elif color[v] != next_c:
                    # This should not happen as per problem statement
                    # but we check for safety
                    pass
    
    # Now we have the two partitions
    part0 = partition[0]
    part1 = partition[1]
    size0 = len(part0)
    size1 = len(part1)
    
    # We can select up to size0 from part0 and up to size1 from part1
    # We want exactly k antennas
    # So we want to find a0, a1 such that a0 + a1 = k, 0 <= a0 <= size0, 0 <= a1 <= size1
    
    # Try all possible values of a0 from max(0, k - size1) to min(k, size0)
    found = False
    a0 = max(0, k - size1)
    if a0 <= min(k, size0):
        a1 = k - a0
        if 0 <= a1 <= size1:
            found = True
    else:
        # Try a0 = min(k, size0)
        a0 = min(k, size0)
        a1 = k - a0
        if 0 <= a1 <= size1:
            found = True
        else:
            # Try a0 = max(0, k - size1)
            a0 = max(0, k - size1)
            a1 = k - a0
            if 0 <= a1 <= size1:
                found = True
    
    if found and a0 >= 0 and a1 >= 0:
        result = []
        if a0 > 0:
            result.extend(part0[:a0])
        if a1 > 0:
            result.extend(part1[:a1])
        if len(result) == k:
            print("YES")
            print(' '.join(map(str, result)))
        else:
            print("NO")
    else:
        print("NO")

if __name__ == "__main__":
    main()