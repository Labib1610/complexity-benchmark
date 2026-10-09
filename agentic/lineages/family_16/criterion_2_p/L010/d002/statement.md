# Problem B — Manufacturing Order Sequence

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing plant is fulfilling a batch of $j$ custom orders. You must arrange the $j$ orders into a single sequence $O_1, O_2, \dots, O_j$ (a permutation of the given orders).

Each order is associated with two processing durations. For each order, you are given its primary duration, $d_1$, and its secondary duration, $d_2$. Let $d_1(O_k)$ and $d_2(O_k)$ denote the respective durations for the order placed at position $k$ in your sequence.

You must assign a primary timestamp $X_k$ and a secondary timestamp $Y_k$ for each position $k$ ($1 \le k \le j$). The assignment must satisfy the following transition inequalities:
- $X_{k+1} \ge X_k + d_1(O_k)$ for $1 \le k < j$
- $Y_k \ge X_k + d_1(O_k)$ for $1 \le k \le j$
- $Y_{k+1} \ge Y_k + d_2(O_k)$ for $1 \le k < j$

Assume $X_1 \ge 0$. Find a sequence of the $j$ orders and a valid timestamp assignment that minimizes the final target value, defined as $Y_j + d_2(O_j)$. Report this smallest possible target value.

## Input

The first line contains a single integer $j$ ($1 \le j \le 200000$).
Each of the next $j$ lines contains two integers $d_1$ and $d_2$ ($1 \le d_1, d_2 \le 1000000$): the primary and secondary durations of an order.

## Output

Print a single integer: the smallest possible final target value.

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

In Example 2, there is only one order with $d_1 = 5$ and $d_2 = 3$. We can set $X_1 = 0$, satisfying $X_1 \ge 0$. The inequalities require $Y_1 \ge X_1 + d_1(O_1) = 5$. We can set $Y_1 = 5$. The final target value is $Y_1 + d_2(O_1) = 5 + 3 = 8$.