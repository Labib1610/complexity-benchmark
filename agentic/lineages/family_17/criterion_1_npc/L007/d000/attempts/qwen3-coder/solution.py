from collections import defaultdict
import sys

def find_matching(n, protocols):
    # Create adjacency list for the graph
    adj = defaultdict(list)
    for i, (a, b, c) in enumerate(protocols):
        adj[a].append(i)
        adj[b].append(i)
        adj[c].append(i)
    
    # Try to find a matching using backtracking with pruning
    used_protocols = [False] * len(protocols)
    used_anomalies = [False] * (n + 1)
    result = []
    
    def backtrack(protocol_idx, count):
        if count == n // 3:
            return True
            
        if protocol_idx >= len(protocols):
            return False
            
        # Try not using this protocol
        if backtrack(protocol_idx + 1, count):
            return True
            
        # Try using this protocol if possible
        a, b, c = protocols[protocol_idx]
        if not used_anomalies[a] and not used_anomalies[b] and not used_anomalies[c]:
            # Use this protocol
            used_protocols[protocol_idx] = True
            used_anomalies[a] = True
            used_anomalies[b] = True
            used_anomalies[c] = True
            result.append(protocol_idx)
            
            if backtrack(protocol_idx + 1, count + 1):
                return True
                
            # Backtrack
            used_protocols[protocol_idx] = False
            used_anomalies[a] = False
            used_anomalies[b] = False
            used_anomalies[c] = False
            result.pop()
            
        return False
    
    # Sort protocols by the smallest anomaly number they contain
    # This helps with pruning
    protocol_indices = list(range(len(protocols)))
    protocol_indices.sort(key=lambda i: min(protocols[i]))
    
    # Reorder protocols based on sorted indices
    sorted_protocols = [protocols[i] for i in protocol_indices]
    original_indices = list(range(len(protocols)))
    for i, idx in enumerate(protocol_indices):
        original_indices[idx] = i
    protocols = sorted_protocols
    
    if backtrack(0, 0):
        # Map back to original indices
        final_result = []
        for idx in result:
            final_result.append(protocols[idx])
        return final_result
    else:
        return None

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    protocols = []
    index = 2
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        protocols.append((a, b, c))
        index += 3
    
    # Special case for q=0
    if q == 0:
        print("YES")
        return
    
    # For small cases, try greedy approach first
    if q <= 10:
        result = find_matching(3*q, protocols)
        if result is not None:
            print("YES")
            for protocol in result:
                print(protocol[0], protocol[1], protocol[2])
        else:
            print("NO")
        return
    
    # For larger cases, use a more efficient approach
    # Try a greedy algorithm: at each step, pick a protocol that covers
    # three unused anomalies
    
    used = [False] * (3*q + 1)
    selected = []
    
    # Build a list of available protocols with their indices
    available = [(i, protocols[i]) for i in range(len(protocols))]
    
    # Greedy selection
    while len(selected) < q:
        found = False
        new_available = []
        for i, (a, b, c) in available:
            if not used[a] and not used[b] and not used[c]:
                used[a] = used[b] = used[c] = True
                selected.append((a, b, c))
                found = True
                # Add remaining protocols to new list
                new_available.extend(available[available.index((i, (a, b, c)))+1:])
                break
            else:
                new_available.append((i, (a, b, c)))
        
        if not found:
            # Greedy didn't work, try backtracking for small cases
            if q <= 8:
                result = find_matching(3*q, protocols)
                if result is not None:
                    print("YES")
                    for protocol in result:
                        print(protocol[0], protocol[1], protocol[2])
                    return
            
            print("NO")
            return
            
        available = new_available
    
    if len(selected) == q:
        print("YES")
        for a, b, c in selected:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    main()