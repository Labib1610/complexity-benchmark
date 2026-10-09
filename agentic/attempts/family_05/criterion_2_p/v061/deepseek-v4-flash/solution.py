import sys
input = sys.stdin.readline

k, t = map(int, input().split())
# vessel_to_reagent: which reagent is in which vessel
vessel_reagent = [0] * (k + 1)
# adjacency: vessel -> list of pressure settings
adj = [[] for _ in range(k + 1)]

for _ in range(t):
    x, y, z = map(int, input().split())
    vessel_reagent[y] = x
    adj[y].append(z)

# We need to match each vessel to a distinct pressure setting
match_z = [0] * (k + 1)  # match_z[z] = vessel assigned to pressure z
match_y = [0] * (k + 1)  # match_y[y] = pressure assigned to vessel y

def dfs(v, visited):
    for z in adj[v]:
        if not visited[z]:
            visited[z] = True
            if match_z[z] == 0 or dfs(match_z[z], visited):
                match_z[z] = v
                match_y[v] = z
                return True
    return False

for v in range(1, k + 1):
    visited = [False] * (k + 1)
    if not dfs(v, visited):
        print("NO")
        sys.exit()

print("YES")
for y in range(1, k + 1):
    z = match_y[y]
    x = vessel_reagent[y]
    print(x, y, z)