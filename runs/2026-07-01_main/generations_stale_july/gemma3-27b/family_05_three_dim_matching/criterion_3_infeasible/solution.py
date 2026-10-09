def solve():
    k, e = map(int, input().split())
    allowed_tasks = [set() for _ in range(k + 1)]
    for _ in range(e):
        x, y = map(int, input().split())
        allowed_tasks[x].add(y)
    
    for i in range(1, k + 1):
        if not allowed_tasks[i]:
            print(i)
            return

solve()