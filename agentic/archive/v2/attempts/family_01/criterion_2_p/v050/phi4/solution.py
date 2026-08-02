import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = defaultdict(list)
    index = 2
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges[u].append(v)
        edges[v].append(u)
        index += 2

    # Use a set to track visited nodes and their assigned block
    visited = [0] * (n + 1)  # 0: not visited, 1: in block 1, 2: in block 2
    assignment = [0] * (n + 1)
    
    def assign(node, block):
        if visited[node]:
            return visited[node] == block
        visited[node] = block
        for neighbor in edges[node]:
            if not assign(neighbor, 3 - block):  # Assign the opposite block to neighbors
                return False
        return True

    possible = True
    for i in range(1, n + 1):
        if not visited[i]:  # If node i is not yet visited
            if not assign(i, 1):  # Try assigning it to block 1
                possible = False
                break
    
    if possible:
        print("YES")
        print(' '.join(map(str, assignment[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    main()