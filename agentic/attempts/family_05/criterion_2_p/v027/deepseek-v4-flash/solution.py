import sys
input = sys.stdin.readline

k, t = map(int, input().split())

# Map protein -> receptor (given fixed)
protein_receptor = [0] * (k + 1)
# Map protein -> list of enzymes
protein_enzymes = [[] for _ in range(k + 1)]

for _ in range(t):
    x, y, z = map(int, input().split())
    protein_receptor[x] = y
    protein_enzymes[x].append(z)

# Bipartite matching: proteins (1..k) to enzymes (1..k)
match_enzyme = [0] * (k + 1)  # which protein is matched to enzyme e

def dfs(protein, visited):
    for enzyme in protein_enzymes[protein]:
        if not visited[enzyme]:
            visited[enzyme] = True
            if match_enzyme[enzyme] == 0 or dfs(match_enzyme[enzyme], visited):
                match_enzyme[enzyme] = protein
                return True
    return False

match_count = 0
for p in range(1, k + 1):
    visited = [False] * (k + 1)
    if dfs(p, visited):
        match_count += 1

if match_count == k:
    print("YES")
    # Build output
    for enzyme in range(1, k + 1):
        protein = match_enzyme[enzyme]
        receptor = protein_receptor[protein]
        print(protein, receptor, enzyme)
else:
    print("NO")