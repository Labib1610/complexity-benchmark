import sys

def main():
    input = sys.stdin.readline
    j = int(input())
    vessels = []
    for _ in range(j):
        t1, t2 = map(int, input().split())
        vessels.append((t1, t2))
    
    # Sort by stern parameter descending, then bow parameter descending
    vessels.sort(key=lambda x: (-x[1], -x[0]))
    
    time = 0
    for t1, t2 in vessels:
        time = max(time, 0) + t1
        time += t2
    
    print(time)

if __name__ == "__main__":
    main()