from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    records = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        records.append((a, b, c))
    
    # Build graph for matching
    # Left side: records (0 to t-1)
    # Right side: personnel (0 to 3*q-1)
    # We want to match each personnel to exactly one record they're in
    
    # This is a maximum matching problem
    # But we want a perfect matching where all 3*q personnel are matched
    # And each record can be matched to at most one of its three personnel
    
    # Actually, let's think differently:
    # We want to select exactly q records such that each person appears exactly once
    # This is a exact cover problem, or more specifically, a matching problem
    
    # Let's model this as a bipartite matching:
    # Left side: positions 0 to q-1 (slots for records)
    # Right side: records 0 to t-1
    # But this isn't right either.
    
    # Better approach:
    # Left side: personnel 1 to 3*q
    # Right side: record slots 1 to q (we need exactly q records)
    # But this is also complex.
    
    # Let's model it as:
    # Find a matching from records to personnel such that:
    # Each record is matched to exactly 3 personnel (its members)
    # Each personnel is matched to exactly 1 record
    
    # This is a hypergraph matching problem. Let's try a different approach.
    
    # Use backtracking with pruning
    def backtrack(record_idx, used_personnel, selected_records):
        if len(selected_records) == q:
            return selected_records[:]
        
        if record_idx == t:
            return None
            
        # Try not taking this record
        result = backtrack(record_idx + 1, used_personnel, selected_records)
        if result is not None:
            return result
            
        # Try taking this record
        a, b, c = records[record_idx]
        if a not in used_personnel and b not in used_personnel and c not in used_personnel:
            used_personnel.add(a)
            used_personnel.add(b)
            used_personnel.add(c)
            selected_records.append(records[record_idx])
            
            result = backtrack(record_idx + 1, used_personnel, selected_records)
            if result is not None:
                return result
                
            selected_records.pop()
            used_personnel.remove(a)
            used_personnel.remove(b)
            used_personnel.remove(c)
            
        return None
    
    # This might be too slow. Let's try a more efficient approach.
    
    # Model as exact cover and use algorithm X (Dancing Links) or simpler backtracking
    result = backtrack(0, set(), [])
    
    if result is None:
        print("NO")
    else:
        print("YES")
        for record in result:
            print(record[0], record[1], record[2])

solve()