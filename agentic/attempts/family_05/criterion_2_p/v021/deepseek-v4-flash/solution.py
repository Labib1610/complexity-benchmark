import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # For each catalyst, store the reagent and list of solvents
    reagent_for = [0] * (k + 1)
    solvents_for = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        reagent_for[x] = y
        solvents_for[x].append(z)
    
    # Bipartite matching: catalysts -> solvents
    match_solvent = [0] * (k + 1)  # which catalyst is matched to solvent
    match_catalyst = [0] * (k + 1) # which solvent is matched to catalyst
    
    def dfs(cat, visited):
        for sol in solvents_for[cat]:
            if not visited[sol]:
                visited[sol] = True
                if match_solvent[sol] == 0 or dfs(match_solvent[sol], visited):
                    match_solvent[sol] = cat
                    match_catalyst[cat] = sol
                    return True
        return False
    
    for cat in range(1, k + 1):
        visited = [False] * (k + 1)
        if not dfs(cat, visited):
            # If a catalyst cannot be matched, we can still try others,
            # but if any catalyst has no possible match, we fail.
            # Actually we need to try all; if any fails, matching size < k.
            pass
    
    # Check if all catalysts matched
    if all(match_catalyst[i] != 0 for i in range(1, k + 1)):
        print("YES")
        for cat in range(1, k + 1):
            sol = match_catalyst[cat]
            print(cat, reagent_for[cat], sol)
    else:
        print("NO")

if __name__ == "__main__":
    solve()