import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    brackets = []
    for _ in range(j):
        d1 = int(next(it))
        d2 = int(next(it))
        brackets.append((d1, d2))
    
    # Sort by min(d1, d2) descending, then by max(d1, d2) descending
    brackets.sort(key=lambda x: (-min(x[0], x[1]), -max(x[0], x[1])))
    
    # Compute prefix sums of d1
    prefix_d1 = [0] * (j + 1)
    for i in range(j):
        prefix_d1[i + 1] = prefix_d1[i] + brackets[i][0]
    
    # Compute suffix max of d2
    suffix_max_d2 = [0] * (j + 1)
    for i in range(j - 1, -1, -1):
        suffix_max_d2[i] = max(brackets[i][1], suffix_max_d2[i + 1])
    
    # Find optimal split point k (0 to j)
    # Answer is prefix_d1[k] + suffix_max_d2[k]
    ans = float('inf')
    for k in range(j + 1):
        val = prefix_d1[k] + suffix_max_d2[k]
        if val < ans:
            ans = val
    
    print(ans)

if __name__ == "__main__":
    solve()