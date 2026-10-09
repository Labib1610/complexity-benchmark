from collections import defaultdict
import sys

def find_matching(k, triplets):
    # Create adjacency list for bipartite matching
    # We'll model this as a matching problem between satellites and (frequency, key) pairs
    
    # Build graph: for each satellite, list of (freq, key) pairs it can use
    adj = defaultdict(list)
    freq_key_set = set()
    
    for x, y, z in triplets:
        adj[x].append((y, z))
        freq_key_set.add((y, z))
    
    # Check if we have enough unique (freq, key) pairs
    if len(freq_key_set) < k:
        return None
        
    # Try all permutations of (freq, key) pairs assigned to satellites 1..k
    from itertools import permutations
    
    freq_key_list = list(freq_key_set)
    
    # For small k, we can try all possible assignments
    # But we need to be smarter - let's use backtracking
    
    def backtrack(satellite, sat_used, freq_used, key_used, current_match):
        if satellite > k:
            return current_match[:]
        
        # Try each compatible (freq, key) pair for this satellite
        for freq, key in adj[satellite]:
            if freq not in freq_used and key not in key_used:
                freq_used.add(freq)
                key_used.add(key)
                current_match.append((satellite, freq, key))
                
                result = backtrack(satellite + 1, sat_used, freq_used, key_used, current_match)
                if result is not None:
                    return result
                    
                current_match.pop()
                freq_used.remove(freq)
                key_used.remove(key)
        
        return None
    
    # Also need to check that every satellite has at least one option
    for i in range(1, k+1):
        if i not in adj:
            return None
            
    result = backtrack(1, set(), set(), set(), [])
    return result

def solve():
    line = input().split()
    k, t = int(line[0]), int(line[1])
    
    triplets = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        triplets.append((x, y, z))
    
    # Special case: k=1
    if k == 1:
        for x, y, z in triplets:
            if x == 1 and y == 1 and z == 1:
                print("YES")
                print("1 1 1")
                return
        print("NO")
        return
    
    # For larger k, use a more systematic approach
    # Model as exact cover problem and use backtracking
    
    # Build mappings
    sat_to_options = defaultdict(list)
    freq_to_options = defaultdict(list)
    key_to_options = defaultdict(list)
    
    for i, (x, y, z) in enumerate(triplets):
        sat_to_options[x].append(i)
        freq_to_options[y].append(i)
        key_to_options[z].append(i)
    
    # Check if every resource appears at least once
    for i in range(1, k+1):
        if i not in sat_to_options or i not in freq_to_options or i not in key_to_options:
            print("NO")
            return
    
    # Backtracking with constraint checking
    selected = [False] * t
    sat_used = [False] * (k+1)
    freq_used = [False] * (k+1)
    key_used = [False] * (k+1)
    solution = []
    
    def backtrack_v2(index, count):
        if count == k:
            return True
            
        if index >= t:
            return False
            
        # Try not taking this triplet
        if backtrack_v2(index + 1, count):
            return True
            
        # Try taking this triplet
        x, y, z = triplets[index]
        if not sat_used[x] and not freq_used[y] and not key_used[z]:
            selected[index] = True
            sat_used[x] = True
            freq_used[y] = True
            key_used[z] = True
            solution.append((x, y, z))
            
            if backtrack_v2(index + 1, count + 1):
                return True
                
            selected[index] = False
            sat_used[x] = False
            freq_used[y] = False
            key_used[z] = False
            solution.pop()
            
        return False
    
    if backtrack_v2(0, 0):
        print("YES")
        for x, y, z in solution:
            print(x, y, z)
    else:
        print("NO")

solve()