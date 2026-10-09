import sys

# Increase recursion depth
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    t = int(input_data[1])
    
    units = []
    pos = [[] for _ in range(3 * q + 1)]
    
    idx = 2
    for u in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        units.append((a, b, c))
        pos[a].append(u)
        pos[b].append(u)
        pos[c].append(u)
    
    used = [False] * (3 * q + 1)
    selected = []
    
    # We can keep track of remaining uncovered elements
    # using a doubly linked list or a set, or just a list/array
    # An array of active elements that we filter is also fine.
    
    def search(rem_elements):
        if not rem_elements:
            return True
        
        # Find element with minimum choices
        best_elem = -1
        min_choices = float('inf')
        best_cand_units = []
        
        for elem in rem_elements:
            cand = []
            for u in pos[elem]:
                a, b, c = units[u]
                if not used[a] and not used[b] and not used[c]:
                    cand.append(u)
            
            c_len = len(cand)
            if c_len == 0:
                return False
            if c_len < min_choices:
                min_choices = c_len
                best_elem = elem
                best_cand_units = cand
                if c_len == 1:
                    break
        
        for u in best_cand_units:
            a, b, c = units[u]
            if used[a] or used[b] or used[c]:
                continue
            
            used[a] = used[b] = used[c] = True
            selected.append(u)
            
            # Form new rem_elements without a, b, c
            next_rem = [x for x in rem_elements if not used[x]]
            
            if search(next_rem):
                return True
            
            selected.pop()
            used[a] = used[b] = used[c] = False
            
        return False

    initial_rem = list(range(1, 3 * q + 1))
    if search(initial_rem):
        print("YES")
        out = []
        for u in selected:
            a, b, c = units[u]
            out.append(f"{a} {b} {c}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()