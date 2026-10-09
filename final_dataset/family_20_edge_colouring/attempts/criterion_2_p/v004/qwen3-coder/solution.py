import sys
from collections import defaultdict
import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    nL = int(data[idx])
    idx += 1
    nR = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    cables = []
    left_ports = defaultdict(list)
    right_ports = defaultdict(list)
    
    for i in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        v = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        cables.append((u, v))
        left_ports[u].append(i)
        right_ports[v].append(i)
    
    # Determine the maximum degree (Δ)
    delta = 0
    for port_list in left_ports.values():
        delta = max(delta, len(port_list))
    for port_list in right_ports.values():
        delta = max(delta, len(port_list))
    
    # Initialize result array
    result = [0] * m
    
    # For each cable, we'll maintain which windows are forbidden at each of its two ports
    # We'll use a greedy approach: for each cable, assign the smallest window number
    # that is not forbidden at both of its ports.
    
    # forbidden_at_left[u][w] = whether window w is forbidden at left port u
    # forbidden_at_right[v][w] = whether window w is forbidden at right port v
    
    # Since delta is the max degree, we only need to consider windows 0 to delta-1
    # We'll use sets for forbidden windows at each port for efficiency
    forbidden_left = [set() for _ in range(nL)]
    forbidden_right = [set() for _ in range(nR)]
    
    # To make it more efficient, we can process cables in a smart order,
    # but a simple greedy approach works well in practice for this problem.
    # We'll process cables in the order they appear.
    
    for i in range(m):
        u, v = cables[i]
        # Find the smallest window number in {0, 1, ..., delta-1} that is not in
        # forbidden_left[u] and not in forbidden_right[v]
        w = 0
        while w < delta:
            if w not in forbidden_left[u] and w not in forbidden_right[v]:
                result[i] = w + 1  # Convert to 1-based for output
                forbidden_left[u].add(w)
                forbidden_right[v].add(w)
                break
            w += 1
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()