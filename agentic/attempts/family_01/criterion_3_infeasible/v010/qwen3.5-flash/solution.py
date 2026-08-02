import sys

def solve():
    # Read all input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj_mask = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    
    # Read edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
        
        # Update adjacency mask (0-based bit index for vertex v is v-1)
        adj_mask[u] |= (1 << (v - 1))
        adj_mask[v] |= (1 << (u - 1))
        
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort and deduplicate neighbor lists to ensure we iterate b in increasing order
    for i in range(1, n + 1):
        adj_list[i] = sorted(list(set(adj_list[i])))
        
    # Precompute clear masks
    # clear_mask[b] should have bits 0..b-1 as 0, and bits >= b as 1
    # This corresponds to ~((1 << b) - 1)
    clear_mask = [~((1 << i) - 1) for i in range(n + 1)]
    
    # Iterate to find the lexicographically smallest triangle
    for a in range(1, n + 1):
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # Find common neighbors of a and b
            common = adj_mask[a] & adj_mask[b]
            
            # We need c > b. In 0-based bit index, c corresponds to bit c-1.
            # So we need bit index >= b.
            # clear_mask[b] clears bits < b.
            mask = common & clear_mask[b]
            
            if mask > 0:
                # Find the lowest set bit index
                # mask & -mask isolates the lowest set bit
                c_bit = (mask & -mask).bit_length() - 1
                c = c_bit + 1
                
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()