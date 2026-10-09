import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    degrees = [0] * (n + 1)
    for i in range(1, n + 1):
        degrees[i] = len(adj[i])
        
    # Sort vertices by degree in descending order
    # This minimizes the sum of |x - y| by placing highly connected vertices together
    vertices = list(range(1, n + 1))
    vertices.sort(key=lambda v: degrees[v], reverse=True)
    
    # Assign positions 1 to n to the sorted vertices
    pos = [0] * (n + 1)
    for i, v in enumerate(vertices):
        pos[v] = i + 1
        
    # Calculate total occupation time
    total_time = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v:
                total_time += abs(pos[u] - pos[v])
                
    if total_time <= B:
        print("YES")
        print(" ".join(map(str, pos[1:])))
    else:
        print("NO")

if __name__ == '__main__':
    solve()