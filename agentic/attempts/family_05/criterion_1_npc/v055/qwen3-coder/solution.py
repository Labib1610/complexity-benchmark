from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
        
    combinations = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        combinations.append((x, y, z))
    
    # Try all subsets of exactly k combinations
    # Since k <= 22, and we need to check combinations, we'll use a more efficient approach
    # We'll model this as a bipartite matching problem or use backtracking
    
    # Let's use backtracking with pruning
    def is_valid(current_selection):
        surgeons = [combo[0] for combo in current_selection]
        rooms = [combo[1] for combo in current_selection]
        times = [combo[2] for combo in current_selection]
        return (len(set(surgeons)) == len(surgeons) and 
                len(set(rooms)) == len(rooms) and 
                len(set(times)) == len(times))
    
    # More efficient approach: build incrementally
    def backtrack(index, selected, used_surgeons, used_rooms, used_times):
        if len(selected) == k:
            return selected[:]
        
        if index >= t:
            return None
            
        # Try including current combination
        x, y, z = combinations[index]
        if x not in used_surgeons and y not in used_rooms and z not in used_times:
            selected.append(combinations[index])
            used_surgeons.add(x)
            used_rooms.add(y)
            used_times.add(z)
            
            result = backtrack(index + 1, selected, used_surgeons, used_rooms, used_times)
            if result is not None:
                return result
                
            selected.pop()
            used_surgeons.remove(x)
            used_rooms.remove(y)
            used_times.remove(z)
        
        # Try not including current combination (if we still have enough left)
        if t - index > k - len(selected):
            result = backtrack(index + 1, selected, used_surgeons, used_rooms, used_times)
            if result is not None:
                return result
        
        return None
    
    result = backtrack(0, [], set(), set(), set())
    
    if result is None:
        print("NO")
    else:
        print("YES")
        for combo in result:
            print(combo[0], combo[1], combo[2])

solve()