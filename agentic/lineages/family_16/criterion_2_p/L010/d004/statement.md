# Problem B — Structural Bracket Assembly

Time limit: 1 s   Memory limit: 256 MB

## Description

You are assembling a batch of $j$ structural brackets along a single-axis rail. You must arrange the $j$ given brackets into a single sequence $B_1, B_2, \dots, B_j$ (a permutation of the given brackets).

Each bracket has an Alpha span $d_1$ and a Beta span $d_2$. Let $d_1(B_k)$ and $d_2(B_k)$ denote the respective spans for the bracket placed at position $k$ in your sequence.

You must assign an Alpha coordinate $X_k$ and a Beta coordinate $Y_k$ for each position $k$ ($1 \le k \le j$). To ensure structural integrity, the placement must satisfy the following 1D distance constraints:
- The distance from the current bracket's Alpha coordinate to the next bracket's Alpha coordinate must be at least the current bracket's Alpha span:
  $X_{k+1} - X_k \ge d_1(B_k)$ for $1 \le k < j$
- The distance from a bracket's Alpha coordinate to its own Beta coordinate must be at least its Alpha span:
  $Y_k - X_k \ge d_1(B_k)$ for $1 \le k \le j$
- The distance from the current bracket's Beta coordinate to the next bracket's Beta coordinate must be at least the current bracket's Beta span:
  $Y_{k+1} - Y_k \ge d_2(B_k)$ for $1 \le k < j$

Assume the rail begins at $X_1 \ge 0$. Your goal is to find a sequence of the $j$ brackets and a valid coordinate assignment that minimizes the furthest boundary reached by the final bracket's Beta span, which is defined as $Y_j + d_2(B_j)$. Report this smallest possible final boundary value.

Note: The answer may exceed the range of a 32-bit signed integer.

## Input

The first line contains a single integer $j$ ($1 \le j \le 200000$).
Each of the next $j$ lines contains two integers $d_1$ and $d_2$ ($1 \le d_1, d_2 \le 1000000$): the Alpha and Beta spans of a bracket.

## Output

Print a single integer: the smallest possible final boundary value.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, there is only one bracket with $d_1 = 5$ and $d_2 = 3$. We can set $X_1 = 0$, satisfying $X_1 \ge 0$. The distance constraints require $Y_1 - X_1 \ge d_1(B_1) = 5$, so $Y_1 \ge 5$. We can set $Y_1 = 5$. The final boundary value is $Y_1 + d_2(B_1) = 5 + 3 = 8$.