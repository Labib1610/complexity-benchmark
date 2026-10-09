import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    vessels = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        vessels.append((p1, p2))
    
    # Sort by (p1 - p2) descending
    vessels.sort(key=lambda x: x[0] - x[1], reverse=True)
    
    # Compute prefix sums of p1 and suffix sums of p2
    prefix_p1 = [0] * (j + 1)
    suffix_p2 = [0] * (j + 1)
    
    for i in range(1, j + 1):
        prefix_p1[i] = prefix_p1[i - 1] + vessels[i - 1][0]
    
    for i in range(j - 1, -1, -1):
        suffix_p2[i] = suffix_p2[i + 1] + vessels[i][1]
    
    # The maximum penalty over all k
    max_penalty = 0
    for k in range(1, j + 1):
        penalty = prefix_p1[k] + suffix_p2[k - 1]
        if penalty > max_penalty:
            max_penalty = penalty
    
    print(max_penalty)

if __name__ == "__main__":
    solve()