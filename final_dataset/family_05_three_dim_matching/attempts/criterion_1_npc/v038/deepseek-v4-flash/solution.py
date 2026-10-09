import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    k = int(input_data[0])
    t = int(input_data[1])
    triplets = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        triplets.append((a, b, c))
    
    target_sum = 3 * k * (k + 1) // 2
    used_a = [False] * (k + 1)
    used_b = [False] * (k + 1)
    used_c = [False] * (k + 1)
    
    # Sort triplets by sum descending for better pruning
    triplets.sort(key=lambda x: -(x[0] + x[1] + x[2]))
    
    selected = []
    
    def backtrack(pos, count, current_sum):
        if count == k:
            return current_sum == target_sum
        if current_sum > target_sum:
            return False
        # Prune: even if we take max possible remaining sums
        # (not strictly needed but can help)
        for i in range(pos, t):
            a, b, c = triplets[i]
            if not used_a[a] and not used_b[b] and not used_c[c]:
                used_a[a] = True
                used_b[b] = True
                used_c[c] = True
                selected.append((a, b, c))
                if backtrack(i + 1, count + 1, current_sum + a + b + c):
                    return True
                selected.pop()
                used_a[a] = False
                used_b[b] = False
                used_c[c] = False
        return False
    
    if backtrack(0, 0, 0):
        print("YES")
        for a, b, c in selected:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()