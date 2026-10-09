import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    k = int(input_data[0])
    t = int(input_data[1])
    voxels = []
    idx = 2
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        z = int(input_data[idx+2])
        idx += 3
        voxels.append((x, y, z))
    
    # If t < k, impossible
    if t < k:
        print("NO")
        return
    
    # Sort voxels maybe helps pruning
    voxels.sort()
    
    used_x = [False] * (k + 1)
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    
    selected = []
    
    def backtrack(start, count):
        if count == k:
            return True
        for i in range(start, t):
            x, y, z = voxels[i]
            if not used_x[x] and not used_y[y] and not used_z[z]:
                used_x[x] = used_y[y] = used_z[z] = True
                selected.append((x, y, z))
                if backtrack(i + 1, count + 1):
                    return True
                selected.pop()
                used_x[x] = used_y[y] = used_z[z] = False
        return False
    
    if backtrack(0, 0):
        print("YES")
        for v in selected:
            print(v[0], v[1], v[2])
    else:
        print("NO")

if __name__ == "__main__":
    solve()