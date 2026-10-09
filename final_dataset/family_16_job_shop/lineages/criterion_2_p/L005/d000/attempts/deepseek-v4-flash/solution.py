import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    tasks = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        tasks.append((p1, p2))
    
    group_a = []
    group_b = []
    for p1, p2 in tasks:
        if p1 <= p2:
            group_a.append((p1, p2))
        else:
            group_b.append((p1, p2))
    
    group_a.sort(key=lambda x: x[0])  # ascending drafting time
    group_b.sort(key=lambda x: x[1], reverse=True)  # descending rendering time
    
    order = group_a + group_b
    
    time_draft = 0
    time_render = 0
    for p1, p2 in order:
        time_draft += p1
        if time_render < time_draft:
            time_render = time_draft
        time_render += p2
    
    print(time_render)

if __name__ == "__main__":
    main()