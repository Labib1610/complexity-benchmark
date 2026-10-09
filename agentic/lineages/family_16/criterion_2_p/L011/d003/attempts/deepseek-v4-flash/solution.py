import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    acts = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        acts.append((p1, p2))
        idx += 2

    # Sort by review time descending
    acts.sort(key=lambda x: x[1], reverse=True)

    stage_time = 0
    review_time = 0
    for p1, p2 in acts:
        stage_time += p1
        review_time = max(review_time, stage_time) + p2

    print(review_time)

if __name__ == "__main__":
    main()