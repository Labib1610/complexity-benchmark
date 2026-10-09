import sys

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # Map operator -> rig
    op_rig = {}
    # Store edges: for each operator, list of zones
    edges = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        op_rig[x] = y
        edges[x].append(z)
    
    # Ensure every operator has a rig (should be guaranteed by input)
    # Bipartite matching: left = operators (1..k), right = zones (1..k)
    match_zone = [0] * (k + 1)  # match_zone[zone] = operator
    
    def dfs(op, visited):
        for z in edges[op]:
            if not visited[z]:
                visited[z] = True
                if match_zone[z] == 0 or dfs(match_zone[z], visited):
                    match_zone[z] = op
                    return True
        return False
    
    for op in range(1, k + 1):
        visited = [False] * (k + 1)
        if not dfs(op, visited):
            print("NO")
            return
    
    # If we got here, matching exists
    print("YES")
    for z in range(1, k + 1):
        op = match_zone[z]
        rig = op_rig[op]
        print(op, rig, z)

if __name__ == "__main__":
    main()