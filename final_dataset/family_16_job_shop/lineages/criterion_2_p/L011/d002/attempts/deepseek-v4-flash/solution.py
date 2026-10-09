import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    performances = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        performances.append((p1, p2))
    
    # Sort by review duration descending
    performances.sort(key=lambda x: x[1], reverse=True)
    
    stage_time = 0
    review_end = 0
    for p1, p2 in performances:
        stage_time += p1
        review_end = max(review_end, stage_time) + p2
    
    print(review_end)

if __name__ == "__main__":
    main()