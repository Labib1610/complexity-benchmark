import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    triples = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        triples.append((x - 1, y - 1, z - 1))
    
    # Build adjacency: surgeon -> list of (room, time)
    adj = [[] for _ in range(k)]
    for x, y, z in triples:
        adj[x].append((y, z))
    
    match_y = [-1] * k  # room -> surgeon
    match_z = [-1] * k  # time -> surgeon
    
    def dfs(v, visited_y, visited_z):
        for y, z in adj[v]:
            if visited_y[y] or visited_z[z]:
                continue
            visited_y[y] = True
            visited_z[z] = True
            if match_y[y] == -1 and match_z[z] == -1:
                match_y[y] = v
                match_z[z] = v
                return True
            # Try to reassign the surgeon currently using room y
            if match_y[y] != -1:
                old_v = match_y[y]
                # Temporarily free both
                match_y[y] = -1
                old_z = -1
                for oz, ov in enumerate(match_z):
                    if ov == old_v:
                        old_z = oz
                        match_z[oz] = -1
                        break
                if dfs(old_v, visited_y, visited_z):
                    match_y[y] = v
                    match_z[z] = v
                    return True
                # Restore
                match_y[y] = old_v
                if old_z != -1:
                    match_z[old_z] = old_v
                continue
            # Try to reassign the surgeon currently using time z
            if match_z[z] != -1:
                old_v = match_z[z]
                match_z[z] = -1
                old_y = -1
                for oy, ov in enumerate(match_y):
                    if ov == old_v:
                        old_y = oy
                        match_y[oy] = -1
                        break
                if dfs(old_v, visited_y, visited_z):
                    match_y[y] = v
                    match_z[z] = v
                    return True
                # Restore
                match_z[z] = old_v
                if old_y != -1:
                    match_y[old_y] = old_v
        return False
    
    for v in range(k):
        visited_y = [False] * k
        visited_z = [False] * k
        if not dfs(v, visited_y, visited_z):
            print("NO")
            return
    
    print("YES")
    # Build result: for each surgeon, find their assigned room and time
    result = [None] * k
    for x in range(k):
        for y, z in adj[x]:
            if match_y[y] == x and match_z[z] == x:
                result[x] = (x + 1, y + 1, z + 1)
                break
    for triple in result:
        print(' '.join(map(str, triple)))

if __name__ == "__main__":
    solve()