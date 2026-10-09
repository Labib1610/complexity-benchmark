import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    triples = []
    idx = 2
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        triples.append((x, y, z))
    
    if k == 0:
        print("YES")
        return
    
    # Build adjacency: for each x, list of (y, z)
    adj = [[] for _ in range(k+1)]
    for (x, y, z) in triples:
        adj[x].append((y, z))
    
    matchY = [0] * (k+1)   # which x is matched to y
    matchZ = [0] * (k+1)   # which x is matched to z
    matchX = [None] * (k+1)  # which (y,z) is matched to x
    
    def try_kuhn(x, visited):
        for (y, z) in adj[x]:
            if visited[y]:
                continue
            visited[y] = True
            if matchY[y] == 0 and matchZ[z] == 0:
                matchY[y] = x
                matchZ[z] = x
                matchX[x] = (y, z)
                return True
        for (y, z) in adj[x]:
            if visited[y]:
                continue
            visited[y] = True
            other_x = matchY[y]
            if matchZ[z] == 0:
                # z is free, but y is matched; try to reassign other_x
                oy, oz = matchX[other_x]
                # temporarily free other_x from y
                matchY[y] = 0
                if try_kuhn(other_x, visited):
                    matchY[y] = x
                    matchZ[z] = x
                    matchX[x] = (y, z)
                    return True
                else:
                    matchY[y] = other_x
            elif matchZ[z] == other_x:
                # both y and z matched to same other_x, try reassign
                matchY[y] = 0
                matchZ[z] = 0
                if try_kuhn(other_x, visited):
                    matchY[y] = x
                    matchZ[z] = x
                    matchX[x] = (y, z)
                    return True
                else:
                    matchY[y] = other_x
                    matchZ[z] = other_x
        return False
    
    for x in range(1, k+1):
        visited = [False] * (k+1)
        if not try_kuhn(x, visited):
            print("NO")
            return
    
    # Verify all resources used
    used_y = set()
    used_z = set()
    for x in range(1, k+1):
        yz = matchX[x]
        if yz is None:
            print("NO")
            return
        used_y.add(yz[0])
        used_z.add(yz[1])
    if len(used_y) != k or len(used_z) != k:
        print("NO")
        return
    
    print("YES")
    out = []
    for x in range(1, k+1):
        y, z = matchX[x]
        out.append(f"{x} {y} {z}")
    sys.stdout.write("\n".join(out) + "\n")

solve()