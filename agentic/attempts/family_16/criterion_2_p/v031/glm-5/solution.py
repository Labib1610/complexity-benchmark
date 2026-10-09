import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    group1 = []
    group2 = []
    
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    
    # Sort group1 by p1 ascending
    group1.sort(key=lambda x: x[0])
    # Sort group2 by p2 descending
    group2.sort(key=lambda x: -x[1])
    
    # Combine: group1 first, then group2
    order = group1 + group2
    
    time_translator = 0
    time_proofreader = 0
    
    for p1, p2 in order:
        time_translator += p1
        # Document finishes translator at time_translator
        # Can start proofreader at max(time_proofreader, time_translator)
        start_proof = time_translator if time_translator > time_proofreader else time_proofreader
        time_proofreader = start_proof + p2
    
    print(time_proofreader)

if __name__ == "__main__":
    solve()