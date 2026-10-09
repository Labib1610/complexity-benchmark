import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    adj = [[] for _ in range(k)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        adj[x-1].append(z-1)
    
    match_to = [-1] * k  # which protein is matched to each cell culture
    
    def dfs(protein, visited):
        for cell in adj[protein]:
            if not visited[cell]:
                visited[cell] = True
                if match_to[cell] == -1 or dfs(match_to[cell], visited):
                    match_to[cell] = protein
                    return True
        return False
    
    for p in range(k):
        visited = [False] * k
        if not dfs(p, visited):
            print("NO")
            return
    
    # Reconstruct the y (guide RNA) for each protein
    # Since protein i is paired with guide RNA i (1-indexed)
    print("YES")
    for cell, protein in enumerate(match_to):
        print(protein + 1, protein + 1, cell + 1)

if __name__ == "__main__":
    solve()