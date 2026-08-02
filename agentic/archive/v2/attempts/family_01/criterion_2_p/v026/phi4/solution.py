import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    constraints = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        constraints.append((u, v))
        index += 2
    
    # Initialize adjacency list
    adj = defaultdict(list)
    for u, v in constraints:
        adj[u].append(v)
        adj[v].append(u)
    
    # Array to store channel assignments: -1 means unassigned, 0 means Channel 1, 1 means Channel 2
    channels = [-1] * (n + 1)

    def is_valid_assignment():
        for u in range(1, n + 1):
            if channels[u] == -1:
                # Try assigning channel 1 to the current unit
                channels[u] = 0
                queue = [u]
                
                while queue:
                    curr = queue.pop()
                    
                    for neighbor in adj[curr]:
                        if channels[neighbor] == -1:
                            channels[neighbor] = 1 - channels[curr]
                            queue.append(neighbor)
                        elif channels[neighbor] == channels[curr]:
                            return False
        return True
    
    # Try to assign channels and check validity
    if is_valid_assignment():
        print("YES")
        for i in range(1, n + 1):
            print(channels[i] + 1, end=" ")
    else:
        print("NO")

if __name__ == "__main__":
    main()