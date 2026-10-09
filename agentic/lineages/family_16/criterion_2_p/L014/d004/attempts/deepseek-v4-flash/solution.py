import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    blocks = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        blocks.append((p1, p2))
    
    # Sort by p2 descending
    blocks.sort(key=lambda x: x[1], reverse=True)
    
    prefix_sum_p1 = 0
    suffix_sum_p2 = sum(p2 for _, p2 in blocks)
    max_time = 0
    
    for k in range(j):
        p1, p2 = blocks[k]
        prefix_sum_p1 += p1
        # For crossover point k+1 (1-indexed)
        # duration = sum p1[0..k] + sum p2[k..j-1]
        duration = prefix_sum_p1 + suffix_sum_p2
        if duration > max_time:
            max_time = duration
        suffix_sum_p2 -= p2
    
    print(max_time)

if __name__ == "__main__":
    main()