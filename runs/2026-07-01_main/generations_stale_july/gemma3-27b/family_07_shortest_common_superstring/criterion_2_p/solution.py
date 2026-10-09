def solve():
    s1 = input()
    s2 = input()
    
    n1 = len(s1)
    n2 = len(s2)
    
    overlap = 0
    for i in range(1, min(n1, n2) + 1):
        if s1[n1-i:] == s2[:i]:
            overlap = i
    
    merged1 = s1 + s2[overlap:]
    
    overlap = 0
    for i in range(1, min(n1, n2) + 1):
        if s2[n2-i:] == s1[:i]:
            overlap = i
            
    merged2 = s2 + s1[overlap:]
    
    if len(merged1) < len(merged2):
        print(merged1)
    elif len(merged2) < len(merged1):
        print(merged2)
    else:
        if merged1 < merged2:
            print(merged1)
        else:
            print(merged2)

solve()