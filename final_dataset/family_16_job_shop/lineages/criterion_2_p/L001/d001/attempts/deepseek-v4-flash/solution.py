import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    jobs = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        jobs.append((p1, p2))
    
    # Sort by p2 descending
    jobs.sort(key=lambda x: x[1], reverse=True)
    
    time_review = 0
    time_finish = 0
    for p1, p2 in jobs:
        time_review += p1
        time_finish = max(time_finish, time_review + p2)
    
    print(time_finish)

if __name__ == "__main__":
    main()