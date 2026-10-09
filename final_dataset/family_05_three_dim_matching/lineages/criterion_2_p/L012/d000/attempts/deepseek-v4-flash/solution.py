import sys
sys.setrecursionlimit(1000000)

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # Map each catalyst to its reagent
    cat_to_reagent = {}
    # Store edges: for each catalyst, list of solvents
    edges = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        cat_to_reagent[x] = y
        edges[x].append(z)
    
    # Bipartite matching: left = catalyst (1..k), right = solvent (1..k)
    match_solvent = [0] * (k + 1)  # match_solvent[s] = catalyst assigned to solvent s
    match_cat = [0] * (k + 1)      # match_cat[c] = solvent assigned to catalyst c
    
    def dfs(cat, visited):
        for sol in edges[cat]:
            if not visited[sol]:
                visited[sol] = True
                if match_solvent[sol] == 0 or dfs(match_solvent[sol], visited):
                    match_solvent[sol] = cat
                    match_cat[cat] = sol
                    return True
        return False
    
    for cat in range(1, k + 1):
        visited = [False] * (k + 1)
        if not dfs(cat, visited):
            print("NO")
            return
    
    # If we matched all catalysts, output YES
    print("YES")
    for cat in range(1, k + 1):
        sol = match_cat[cat]
        reagent = cat_to_reagent[cat]
        print(cat, reagent, sol)

if __name__ == "__main__":
    solve()