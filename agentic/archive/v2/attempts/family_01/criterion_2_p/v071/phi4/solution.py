import sys
from collections import defaultdict

def read_input():
    return map(int, sys.stdin.read().split())

def solve(n, m, edges):
    if n == 1:
        print("YES")
        print(1)
        return
    
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Sort the vertices based on their degree (number of connections)
    vertices = sorted(range(1, n + 1), key=lambda x: len(adj[x]))
    
    vault_assignment = [0] * (n + 1)
    
    def assign_vault(start):
        queue = [start]
        vault_assignment[start] = 1
        while queue:
            current = queue.pop()
            next_vault = 3 - vault_assignment[current]
            for neighbor in adj[current]:
                if vault_assignment[neighbor] == 0:
                    vault_assignment[neighbor] = next_vault
                    queue.append(neighbor)
    
    # Try to assign vaults starting from the vertex with the smallest degree
    for i in range(1, n + 1):
        if vault_assignment[i] == 0:
            assign_vault(i)
    
    # Check if there's any invalid assignment
    for u, v in edges:
        if vault_assignment[u] == vault_assignment[v]:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, vault_assignment[1:])))
    
def main():
    data = read_input()
    n, m = next(data), next(data)
    edges = [(next(data), next(data)) for _ in range(m)]
    solve(n, m, edges)

if __name__ == "__main__":
    main()