import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    orders = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        orders.append((p1, p2))
    
    # Sort by p2 descending (Johnson's rule for two-machine flow shop)
    orders.sort(key=lambda x: -x[1])
    
    # Simulate the process
    # mixer_free: time when mixer becomes free
    # froster_free: time when froster becomes free
    mixer_free = 0
    froster_free = 0
    
    for p1, p2 in orders:
        # Mixer starts at mixer_free, finishes at mixer_free + p1
        # Order is placed on counter at mixer_free + p1
        counter_time = mixer_free + p1
        # Froster can start at max(froster_free, counter_time)
        froster_start = max(froster_free, counter_time)
        froster_free = froster_start + p2
        mixer_free = counter_time
    
    print(froster_free)

solve()