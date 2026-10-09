def solve():
    uA, uB, s = map(int, input().split())
    consultants = []
    for _ in range(s):
        a, b = map(int, input().split())
        consultants.append((a, b))
    
    frontend_skills = set()
    backend_skills = set()
    for a, b in consultants:
        frontend_skills.add(a)
        backend_skills.add(b)
    
    
    min_consultants = float('inf')
    
    for i in range(1 << s):
        hired_consultants = []
        for j in range(s):
            if (i >> j) & 1:
                hired_consultants.append(consultants[j])
        
        covered_frontend = set()
        covered_backend = set()
        for a, b in hired_consultants:
            covered_frontend.add(a)
            covered_backend.add(b)
        
        if len(covered_frontend) == uA and len(covered_backend) == uB:
            min_consultants = min(min_consultants, len(hired_consultants))
            
    print(min_consultants)

solve()