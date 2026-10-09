def solve():
    n, k, C = map(int, input().split())
    w = list(map(int, input().split()))
    
    assignment = [0] * n
    
    def can_load(index):
        if index == n:
            container_weights = [0] * k
            for i in range(n):
                container_weights[assignment[i] - 1] += w[i]
            
            for weight in container_weights:
                if weight > C:
                    return False
            return True
        
        for container in range(1, k + 1):
            assignment[index] = container
            if can_load(index + 1):
                return True
        
        return False
    
    if can_load(0):
        print("YES")
        print(*assignment)
    else:
        print("NO")

solve()