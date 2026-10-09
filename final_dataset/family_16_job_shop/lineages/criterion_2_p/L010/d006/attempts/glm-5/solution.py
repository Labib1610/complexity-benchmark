import sys

def solve():
    data = sys.stdin.read().split()
    j = int(data[0])
    brackets = []
    idx = 1
    total_d1 = 0
    for _ in range(j):
        d1 = int(data[idx])
        d2 = int(data[idx + 1])
        idx += 2
        brackets.append((d1, d2))
        total_d1 += d1
    
    # Sort by c_i = d2 - d1 in non-decreasing order
    brackets.sort(key=lambda x: x[1] - x[0])
    
    # Compute maximum suffix sum of c_i values
    max_suffix_sum = 0
    current_suffix = 0
    for d1, d2 in reversed(brackets):
        current_suffix += d2 - d1
        if current_suffix > max_suffix_sum:
            max_suffix_sum = current_suffix
    
    result = total_d1 + max_suffix_sum
    print(result)

solve()