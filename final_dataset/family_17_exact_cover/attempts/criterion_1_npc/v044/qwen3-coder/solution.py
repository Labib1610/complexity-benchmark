from collections import defaultdict
import sys

def find_valid_allocation(q, t, protocols):
    if t < q:
        return None
    
    # Create a mapping from responder ID to list of protocols containing it
    responder_to_protocols = defaultdict(list)
    for i, (a, b, c) in enumerate(protocols):
        responder_to_protocols[a].append(i)
        responder_to_protocols[b].append(i)
        responder_to_protocols[c].append(i)
    
    # Try to build a valid allocation using backtracking
    selected = []
    used_protocols = [False] * t
    used_responders = [False] * (3 * q + 1)
    
    def backtrack(responder_id):
        # If we've assigned all responders, we're done
        if responder_id > 3 * q:
            return len(selected) == q
        
        # If this responder is already assigned, move to the next one
        if used_responders[responder_id]:
            return backtrack(responder_id + 1)
        
        # Try each protocol containing this responder
        for protocol_idx in responder_to_protocols[responder_id]:
            if used_protocols[protocol_idx]:
                continue
                
            a, b, c = protocols[protocol_idx]
            
            # Check if all responders in this protocol are available
            if used_responders[a] or used_responders[b] or used_responders[c]:
                continue
            
            # Use this protocol
            selected.append(protocol_idx)
            used_protocols[protocol_idx] = True
            used_responders[a] = used_responders[b] = used_responders[c] = True
            
            # Recurse
            if backtrack(responder_id + 1):
                return True
            
            # Backtrack
            selected.pop()
            used_protocols[protocol_idx] = False
            used_responders[a] = used_responders[b] = used_responders[c] = False
        
        return False
    
    if backtrack(1):
        return [protocols[i] for i in selected]
    else:
        return None

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    
    q, t = map(int, input_lines[0].split())
    protocols = []
    for i in range(1, t + 1):
        a, b, c = map(int, input_lines[i].split())
        protocols.append((a, b, c))
    
    result = find_valid_allocation(q, t, protocols)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        for protocol in result:
            print(protocol[0], protocol[1], protocol[2])

if __name__ == "__main__":
    main()