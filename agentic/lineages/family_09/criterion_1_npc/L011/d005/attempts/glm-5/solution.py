import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1
    
    adj = [0] * n
    for i in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    if k == 0:
        print("YES")
        print()
        return
    
    if k > n:
        print("NO")
        return
    
    half = n // 2
    left_size = half
    right_size = n - half
    
    left_nodes = list(range(half))
    right_nodes = list(range(half, n))
    
    # For right half, compute adjacency within right half
    right_adj = {}
    for i, node in enumerate(right_nodes):
        mask = 0
        for j, other in enumerate(right_nodes):
            if adj[node] & (1 << other):
                mask |= (1 << j)
        right_adj[i] = mask
    
    # Map: (count, forbidden_mask) -> set of achievable masks
    # forbidden_mask tracks which right nodes are blocked by selected left nodes
    right_achievable = defaultdict(set)
    
    # Enumerate all independent sets in right half
    right_count = right_size
    for mask in range(1 << right_count):
        # Check if independent set
        valid = True
        temp = mask
        while temp:
            low = temp & (-temp)
            i = low.bit_length() - 1
            if mask & right_adj[i]:
                valid = False
                break
            temp ^= low
        
        if valid:
            cnt = bin(mask).count('1')
            right_achievable[cnt].add(mask)
    
    # For left half, enumerate all independent sets
    left_adj = {}
    for i, node in enumerate(left_nodes):
        mask = 0
        for j, other in enumerate(left_nodes):
            if adj[node] & (1 << other):
                mask |= (1 << j)
        left_adj[i] = mask
    
    # For each left independent set, compute forbidden mask on right
    left_count = left_size
    
    for mask in range(1 << left_count):
        valid = True
        temp = mask
        while temp:
            low = temp & (-temp)
            i = low.bit_length() - 1
            if mask & left_adj[i]:
                valid = False
                break
            temp ^= low
        
        if not valid:
            continue
        
        cnt = bin(mask).count('1')
        if cnt > k:
            continue
        
        need = k - cnt
        if need < 0 or need > right_count:
            continue
        
        # Compute forbidden mask on right
        forbidden = 0
        temp = mask
        while temp:
            low = temp & (-temp)
            i = low.bit_length() - 1
            node = left_nodes[i]
            for j, other in enumerate(right_nodes):
                if adj[node] & (1 << other):
                    forbidden |= (1 << j)
            temp ^= low
        
        # Find right independent set of size 'need' not touching forbidden
        if need in right_achievable:
            for rmask in right_achievable[need]:
                if rmask & forbidden == 0:
                    # Found solution
                    panel = []
                    temp = mask
                    while temp:
                        low = temp & (-temp)
                        i = low.bit_length() - 1
                        panel.append(left_nodes[i] + 1)
                        temp ^= low
                    temp = rmask
                    while temp:
                        low = temp & (-temp)
                        i = low.bit_length() - 1
                        panel.append(right_nodes[i] + 1)
                        temp ^= low
                    print("YES")
                    print(' '.join(map(str, sorted(panel))))
                    return
    
    print("NO")

solve()