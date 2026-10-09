import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    adj = [0] * (n + 1)
    for i in range(m):
        u = int(input_data[3 + 2*i])
        v = int(input_data[3 + 2*i + 1])
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        
    if k == 1:
        print("YES")
        print(1)
        return
        
    if k > n:
        print("NO")
        return

    half = n // 2
    left_size = half
    right_size = n - half
    
    left_adj = [0] * (left_size + 1)
    for i in range(1, left_size + 1):
        for j in range(1, left_size + 1):
            if adj[i] & (1 << j):
                left_adj[i] |= 1 << j
                
    right_adj = [0] * (right_size + 1)
    for i in range(1, right_size + 1):
        orig_i = half + i
        for j in range(1, right_size + 1):
            orig_j = half + j
            if adj[orig_i] & (1 << orig_j):
                right_adj[i] |= 1 << j

    left_independent_sets = []
    for mask in range(1 << left_size):
        valid = True
        for i in range(left_size):
            if (mask >> i) & 1:
                if mask & left_adj[i + 1]:
                    valid = False
                    break
        if valid:
            left_independent_sets.append(mask)
            
    right_independent_sets = []
    for mask in range(1 << right_size):
        valid = True
        for i in range(right_size):
            if (mask >> i) & 1:
                if mask & right_adj[i + 1]:
                    valid = False
                    break
        if valid:
            right_independent_sets.append(mask)
            
    left_independent_sets.sort(key=lambda x: bin(x).count('1'))
    right_independent_sets.sort(key=lambda x: bin(x).count('1'))
    
    left_sizes = [bin(x).count('1') for x in left_independent_sets]
    right_sizes = [bin(x).count('1') for x in right_independent_sets]
    
    left_ptr = len(left_independent_sets) - 1
    right_ptr = len(right_independent_sets) - 1
    
    while left_ptr >= 0 and right_ptr >= 0:
        total = left_sizes[left_ptr] + right_sizes[right_ptr]
        if total < k:
            break
        if total >= k:
            for i in range(left_ptr + 1):
                if left_sizes[i] + right_sizes[right_ptr] < k:
                    break
                left_mask = left_independent_sets[i]
                forbidden = 0
                for j in range(left_size):
                    if (left_mask >> j) & 1:
                        forbidden |= adj[j + 1] >> half
                
                if (right_independent_sets[right_ptr] & forbidden) == 0:
                    result = []
                    for j in range(left_size):
                        if (left_mask >> j) & 1:
                            result.append(j + 1)
                    for j in range(right_size):
                        if (right_independent_sets[right_ptr] >> j) & 1:
                            result.append(half + j + 1)
                            
                    print("YES")
                    print(" ".join(map(str, result[:k])))
                    return
            right_ptr -= 1
            
    print("NO")

if __name__ == '__main__':
    solve()