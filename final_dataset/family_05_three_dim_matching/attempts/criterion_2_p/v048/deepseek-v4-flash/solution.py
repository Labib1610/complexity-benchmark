import sys

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # For each extraction site, store the possible injection wells
    adj = [[] for _ in range(k)]
    # Also store the blueprint (e, d, i) for output
    blueprint = {}
    
    for _ in range(t):
        e, d, i = map(int, input().split())
        e -= 1
        i -= 1
        adj[e].append(i)
        blueprint[(e, i)] = (e + 1, d, i + 1)
    
    # Kuhn's algorithm for bipartite matching
    match_to_site = [-1] * k  # which site is matched to well i
    match_to_well = [-1] * k  # which well is matched to site e
    
    def dfs(e, visited):
        for i in adj[e]:
            if visited[i]:
                continue
            visited[i] = True
            if match_to_site[i] == -1 or dfs(match_to_site[i], visited):
                match_to_site[i] = e
                match_to_well[e] = i
                return True
        return False
    
    for e in range(k):
        visited = [False] * k
        if not dfs(e, visited):
            print("NO")
            return
    
    # If we matched all sites, output
    print("YES")
    for e in range(k):
        i = match_to_well[e]
        # Find the blueprint for (e, i)
        # Since each site has only one d, we can get d from any blueprint of that site
        # We stored blueprint with (e, i) key
        _, d, _ = blueprint[(e, i)]
        print(e + 1, d, i + 1)

if __name__ == "__main__":
    main()