import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    adj_x = [[] for _ in range(k)]
    adj_y = [[] for _ in range(k)]
    adj_z = [[] for _ in range(k)]
    
    idx = 2
    for _ in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx+1]) - 1
        z = int(input_data[idx+2]) - 1
        idx += 3
        adj_x[x].append((y, z))
        adj_y[y].append((x, z))
        adj_z[z].append((x, y))
        
    sol = []
    
    def search(mask_x, mask_y, mask_z, depth):
        if depth == k:
            return True
        
        min_deg = 1000000
        best_edges = None
        
        # Check X
        for x in range(k):
            if not ((mask_x >> x) & 1):
                valid = []
                for y, z in adj_x[x]:
                    if not ((mask_y >> y) & 1) and not ((mask_z >> z) & 1):
                        valid.append((x, y, z))
                lv = len(valid)
                if lv == 0:
                    return False
                if lv < min_deg:
                    min_deg = lv
                    best_edges = valid
                    if min_deg == 1:
                        break
        
        # Check Y
        if min_deg > 1:
            for y in range(k):
                if not ((mask_y >> y) & 1):
                    valid = []
                    for x, z in adj_y[y]:
                        if not ((mask_x >> x) & 1) and not ((mask_z >> z) & 1):
                            valid.append((x, y, z))
                    lv = len(valid)
                    if lv == 0:
                        return False
                    if lv < min_deg:
                        min_deg = lv
                        best_edges = valid
                        if min_deg == 1:
                            break
                            
        # Check Z
        if min_deg > 1:
            for z in range(k):
                if not ((mask_z >> z) & 1):
                    valid = []
                    for x, y in adj_z[z]:
                        if not ((mask_x >> x) & 1) and not ((mask_y >> y) & 1):
                            valid.append((x, y, z))
                    lv = len(valid)
                    if lv == 0:
                        return False
                    if lv < min_deg:
                        min_deg = lv
                        best_edges = valid
                        if min_deg == 1:
                            break

        for x, y, z in best_edges:
            sol.append((x + 1, y + 1, z + 1))
            if search(mask_x | (1 << x), mask_y | (1 << y), mask_z | (1 << z), depth + 1):
                return True
            sol.pop()
            
        return False

    if search(0, 0, 0, 0):
        out = ["YES"]
        for x, y, z in sol:
            out.append(f"{x} {y} {z}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()