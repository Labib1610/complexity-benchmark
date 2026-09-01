import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2

    # The stability score formula: 3(r_u + r_v) - 2*r_u*r_v
    # Let's compute what this value is for each possible pair:
    # r_u=1, r_v=1: 3(1+1) - 2*1*1 = 6 - 2 = 4
    # r_u=1, r_v=2: 3(1+2) - 2*1*2 = 9 - 4 = 5
    # r_u=2, r_v=1: 3(2+1) - 2*2*1 = 9 - 4 = 5
    # r_u=2, r_v=2: 3(2+2) - 2*2*2 = 12 - 8 = 4
    # So the score is 5 if and only if exactly one of r_u or r_v is 2 (i.e., they are different).
    # The total score is 5m if and only if ALL edges have different resonance levels at their endpoints.
    # This is equivalent to a 2-coloring (bipartite) of the graph.
    
    # So the problem reduces to checking if the graph is bipartite.
    # If it is, we find the lexicographically smallest 2-coloring.
    
    color = [-1] * (n + 1)
    
    # Check bipartiteness using BFS for each connected component
    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0  # Assign color 0 to the starting node
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # If bipartite, construct the lexicographically smallest valid assignment.
    # For each node, we prefer to assign it level 1 if possible.
    # Since color 0 or 1 can correspond to level 1 or 2, we need to decide which mapping gives lex smallest.
    # Let's try both mappings and pick the lex smaller one.
    
    # Mapping 0 -> 1, 1 -> 2
    res1 = [1 if color[i] == 0 else 2 for i in range(1, n + 1)]
    # Mapping 0 -> 2, 1 -> 1
    res2 = [2 if color[i] == 0 else 1 for i in range(1, n + 1)]
    
    # Choose the lexicographically smaller one
    chosen = res1 if res1 <= res2 else res2
    
    print("YES")
    print(" ".join(map(str, chosen)))

if __name__ == "__main__":
    main()