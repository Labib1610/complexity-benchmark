import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    if t < k:
        print("NO")
        return

    # Triples: x, y, z all 0-indexed internally
    # Group triples by x
    spec_options = [[] for _ in range(k)]
    mach_options = [[] for _ in range(k)]
    slot_options = [[] for _ in range(k)]
    
    triples = []
    idx = 2
    for i in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx+1]) - 1
        z = int(input_data[idx+2]) - 1
        idx += 3
        spec_options[x].append((y, z))
        mach_options[y].append((x, z))
        slot_options[z].append((x, y))
        triples.append((x, y, z))

    # Check if any specialist, machine, or slot has 0 options
    for i in range(k):
        if not spec_options[i] or not mach_options[i] or not slot_options[i]:
            print("NO")
            return

    # Sort specialists by number of options initially
    spec_order = sorted(range(k), key=lambda x: len(spec_options[x]))

    assignment = [None] * k
    
    # Pre-sort each specialist's options
    # Maybe sort options by frequency of y and z?
    
    def search(depth, used_y, used_z):
        if depth == k:
            return True
        
        # Pick the next specialist with the fewest available options (dynamic MRV over remaining specialists)
        best_spec = -1
        min_options = 1000
        best_valid_pairs = None
        
        for s in spec_order:
            if assignment[s] is not None:
                continue
            valid_pairs = []
            for y, z in spec_options[s]:
                if not ((used_y & (1 << y)) or (used_z & (1 << z))):
                    valid_pairs.append((y, z))
            cnt = len(valid_pairs)
            if cnt == 0:
                return False
            if cnt < min_options:
                min_options = cnt
                best_spec = s
                best_valid_pairs = valid_pairs
                if cnt == 1:
                    break
        
        s = best_spec
        for y, z in best_valid_pairs:
            assignment[s] = (y, z)
            if search(depth + 1, used_y | (1 << y), used_z | (1 << z)):
                return True
            assignment[s] = None
            
        return False

    if search(0, 0, 0):
        print("YES")
        out = []
        for s in range(k):
            y, z = assignment[s]
            out.append(f"{s + 1} {y + 1} {z + 1}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()