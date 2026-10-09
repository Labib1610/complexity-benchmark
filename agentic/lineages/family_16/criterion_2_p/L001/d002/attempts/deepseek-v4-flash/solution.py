import sys

def main():
    input = sys.stdin.readline
    j = int(input())
    dossiers = []
    for _ in range(j):
        p1, p2 = map(int, input().split())
        dossiers.append((p1, p2))
    
    # Sort by p2 descending
    dossiers.sort(key=lambda x: x[1], reverse=True)
    
    prefix_sum = 0
    total_p2 = sum(p2 for _, p2 in dossiers)
    max_metric = 0
    
    for p1, p2 in dossiers:
        prefix_sum += p1
        metric = prefix_sum + total_p2
        if metric > max_metric:
            max_metric = metric
        total_p2 -= p2
    
    print(max_metric)

if __name__ == "__main__":
    main()