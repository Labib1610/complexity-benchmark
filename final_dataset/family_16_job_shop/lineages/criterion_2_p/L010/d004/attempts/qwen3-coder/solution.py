import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    brackets = []
    index = 1
    for i in range(j):
        d1 = int(data[index])
        d2 = int(data[index+1])
        brackets.append((d1, d2))
        index += 2
    
    # Sort brackets by d1 ascending and d2 descending
    # This heuristic helps minimize the total span
    brackets.sort(key=lambda x: (x[0], -x[1]))
    
    # Initialize coordinates
    X = [0] * j
    Y = [0] * j
    
    # Set the first bracket's coordinates
    X[0] = 0
    Y[0] = X[0] + brackets[0][0]  # Y[0] - X[0] >= d1[0] => Y[0] >= X[0] + d1[0]
    
    # Calculate coordinates for subsequent brackets
    for k in range(1, j):
        d1_prev, d2_prev = brackets[k-1]
        d1_curr, d2_curr = brackets[k]
        
        # X[k] - X[k-1] >= d1_prev => X[k] >= X[k-1] + d1_prev
        X[k] = X[k-1] + d1_prev
        
        # Y[k] - X[k] >= d1_curr => Y[k] >= X[k] + d1_curr
        y_min_from_x = X[k] + d1_curr
        
        # Y[k] - Y[k-1] >= d2_prev => Y[k] >= Y[k-1] + d2_prev
        y_min_from_y = Y[k-1] + d2_prev
        
        # Take the maximum of both constraints
        Y[k] = max(y_min_from_x, y_min_from_y)
    
    # Final boundary is Y[j-1] + d2 of last bracket
    d1_last, d2_last = brackets[j-1]
    result = Y[j-1] + d2_last
    print(result)

if __name__ == '__main__':
    threading.Thread(target=main).start()