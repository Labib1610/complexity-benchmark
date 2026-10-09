import sys
from itertools import accumulate

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    processors = []
    idx = 1
    for _ in range(j):
        t1 = int(data[idx])
        t2 = int(data[idx+1])
        processors.append((t1, t2))
        idx += 2
    
    # Calculate total decay delay (base latency)
    total_t2 = sum(t2 for t1, t2 in processors)
    
    # For each processor, compute (activation_delay - decay_delay)
    diff = [t1 - t2 for t1, t2 in processors]
    
    # Compute prefix sums of diff
    prefix_diff = [0] + list(accumulate(diff))
    
    # The interference spike at position k is:
    # total_t2 + prefix_diff[k]
    # We want to minimize the maximum of these values.
    
    # To minimize max(total_t2 + prefix_diff[k]) for k=1..j,
    # we need to minimize max(prefix_diff[k]) for k=1..j.
    
    # However, we can permute the processors. 
    # Let's sort the processors based on (t1 - t2) in descending order
    # to minimize the maximum prefix sum.
    
    # Actually, let's think differently.
    # The peak interference is max_k (total_t2 + sum_{i=1}^k (t1[i] - t2[i-1]))
    # Wait, no. Let's re-read the definition carefully.
    
    # Interference spike at position k:
    # base_latency + sum of activation delays from 1 to k 
    #                - sum of decay delays from 1 to k-1
    
    # So it's: total_t2 + sum_{i=1}^k t1[i] - sum_{i=1}^{k-1} t2[i]
    
    # This can be rewritten as:
    # total_t2 + (sum_{i=1}^{k-1} t1[i] + t1[k]) - sum_{i=1}^{k-1} t2[i]
    # = total_t2 + sum_{i=1}^{k-1} (t1[i] - t2[i]) + t1[k]
    
    # So for each k, spike[k] = total_t2 + prefix_sum_of_(t1-t2)_{1 to k-1} + t1[k]
    
    # But actually, looking at the indexing, let's be more careful.
    # Position k means we consider elements 1 through k (1-indexed).
    # Interference spike at k = total_t2 + sum(t1[1]...t1[k]) - sum(t2[1]...t2[k-1])
    
    # Let's define arrays properly.
    t1_list = [p[0] for p in processors]
    t2_list = [p[1] for p in processors]
    
    # Prefix sums
    prefix_t1 = [0] + list(accumulate(t1_list))
    prefix_t2 = [0] + list(accumulate(t2_list))
    
    # Calculate all interference spikes
    max_interference = 0
    for k in range(1, j+1):
        spike = total_t2 + prefix_t1[k] - prefix_t2[k-1]
        if spike > max_interference:
            max_interference = spike
            
    print(max_interference)

if __name__ == "__main__":
    main()