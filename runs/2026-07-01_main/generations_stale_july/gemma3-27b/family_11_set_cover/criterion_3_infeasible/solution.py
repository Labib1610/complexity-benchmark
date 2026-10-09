def solve():
    u, s = map(int, input().split())
    skills = set()
    for _ in range(s):
        c, *skill_ids = map(int, input().split())
        for skill_id in skill_ids:
            skills.add(skill_id)
    
    for i in range(1, u + 1):
        if i not in skills:
            print(i)
            return

solve()