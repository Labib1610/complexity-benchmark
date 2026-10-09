import sys
import heapq

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    
    amplifiers = []
    for i in range(j):
        p1 = int(input_data[idx]); idx += 1
        p2 = int(input_data[idx]); idx += 1
        amplifiers.append((p1, p2))
    
    # Sort by p1 ascending, then by p2 ascending
    amplifiers.sort()
    
    # Min-heap of p2 values for available amplifiers (those with p1 <= S)
    available = []
    ptr = 0
    S = 0
    
    while ptr < j or available:
        # Add all amplifiers with p1 <= S to available
        while ptr < j and amplifiers[ptr][0] <= S:
            heapq.heappush(available, amplifiers[ptr][1])
            ptr += 1
        
        if available:
            # Process amplifier with smallest p2 (gives contribution p2 - p1 <= p2 - S)
            p2 = heapq.heappop(available)
            # Find its p1 - but we need to track this... 
            # Actually we need p1 to compute new S = max(S - p1, 0) + p2
            pass
        else:
            # No amplifier can be covered, pick smallest p2 among remaining
            # This amplifier has p1 > S, so new S = 0 + p2 = p2
            p1, p2 = amplifiers[ptr]
            ptr += 1
            S = p2
    
    # This approach has a bug - we lose track of p1 when using heap
    # Let me reconsider...

solve()