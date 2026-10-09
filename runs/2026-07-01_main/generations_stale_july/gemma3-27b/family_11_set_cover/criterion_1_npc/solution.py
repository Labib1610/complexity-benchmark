def solve():
    u, s, k = map(int, input().split())
    consultants = []
    for _ in range(s):
        line = input().split()
        c = int(line[0])
        skills = list(map(int, line[1:]))
        consultants.append(set(skills))
    
    for i in range(1 << s):
        if bin(i).count('1') <= k:
            covered_skills = set()
            hired_consultants = []
            for j in range(s):
                if (i >> j) & 1:
                    covered_skills.update(consultants[j])
                    hired_consultants.append(j + 1)
            
            if len(covered_skills) == u:
                print("YES")
                print(*hired_consultants)
                return
    
    print("NO")

solve()