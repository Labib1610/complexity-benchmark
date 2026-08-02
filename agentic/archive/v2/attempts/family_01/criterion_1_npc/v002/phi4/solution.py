def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        edges.append((u, v))
        idx += 2
    
    # Initialize channels to None (meaning unassigned)
    channels = [None] * n
    
    def is_valid_assignment(channels):
        for u, v in edges:
            if channels[u] == channels[v]:
                return False
        return True

    def assign_channels(transmitter, used_channels):
        if transmitter == n:
            if is_valid_assignment(channels):
                return True
            else:
                return False
        
        for channel in range(1, 4):
            if channel not in used_channels[transmitter]:
                channels[transmitter] = channel
                new_used_channels = [uc.copy() for uc in used_channels]
                
                for neighbor in range(n):
                    if (transmitter, neighbor) in edges or (neighbor, transmitter) in edges:
                        new_used_channels[neighbor].add(channel)
                        
                if assign_channels(transmitter + 1, new_used_channels):
                    return True
                
                channels[transmitter] = None
        
        return False
    
    used_channels = [set() for _ in range(n)]
    
    if assign_channels(0, used_channels):
        print("YES")
        print(' '.join(map(str, channels)))
    else:
        print("NO")