def solve():
    n, m = map(int, input().split())
    incompatible_pairs = []
    for _ in range(m):
        u, v = map(int, input().split())
        incompatible_pairs.append((u, v))
    
    def is_valid(schedule):
        for u, v in incompatible_pairs:
            if schedule[u-1] == schedule[v-1]:
                return False
        return True

    def find_lexicographically_smallest_schedule():
        schedule = [0] * n
        
        def backtrack(index):
            if index == n:
                if is_valid(schedule):
                    return schedule[:]
                else:
                    return None
            
            for window in range(1, 4):
                schedule[index] = window
                result = backtrack(index + 1)
                if result:
                    return result
            
            return None
        
        return backtrack(0)

    schedule = find_lexicographically_smallest_schedule()
    
    if schedule:
        print("YES")
        print(*schedule)
    else:
        print("NO")

solve()