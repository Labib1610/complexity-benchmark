import sys

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # Map catalyst -> fixed solvent
    cat_solvent = {}
    # Map catalyst -> list of temperatures
    cat_temps = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        if x not in cat_solvent:
            cat_solvent[x] = y
        # Since input is guaranteed consistent, we don't need to check mismatch
        cat_temps[x].append(z)
    
    # Build matching: temperature -> catalyst
    match_temp = [0] * (k + 1)  # match_temp[z] = catalyst assigned to temp z
    
    def dfs(cat, visited):
        for z in cat_temps[cat]:
            if not visited[z]:
                visited[z] = True
                if match_temp[z] == 0 or dfs(match_temp[z], visited):
                    match_temp[z] = cat
                    return True
        return False
    
    for cat in range(1, k + 1):
        visited = [False] * (k + 1)
        if not dfs(cat, visited):
            print("NO")
            return
    
    # If we reach here, perfect matching exists
    print("YES")
    for z in range(1, k + 1):
        cat = match_temp[z]
        y = cat_solvent[cat]
        print(cat, y, z)

if __name__ == "__main__":
    main()