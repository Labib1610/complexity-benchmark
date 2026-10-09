# Problem A — Production Cycle Allocation

Time limit: 2 s   Memory limit: 256 MB

The factory operations pipeline consists of three distinct stages:

1. **Collision Detection:** First, a monitoring system analyzes the factory floor to identify pairs of personnel who require the same specialized machinery simultaneously. This generates a definitive list of operational collisions. This stage is already complete, and its output is provided to you.
2. **Cycle Allocation (Your Task):** You must take the collision list and assign each of the $n$ personnel to exactly one of three daily production cycles (labeled 1, 2, and 3). To maintain safety and efficiency, any two individuals flagged with an operational collision must be allocated to different cycles. You must determine if a valid allocation is possible and generate the cycle assignments.
3. **Payroll Processing:** Finally, the assignments are sent to the payroll department to calculate cycle-specific pay rates. You do not need to implement this stage.

Write a program to execute the Cycle Allocation stage.

## Input
The first line contains two integers $n$ and $m$ — the number of personnel and the number of operational collisions ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of personnel with an operational collision.

## Output
If no valid allocation exists, print a single line `NO`.
Otherwise print `YES` on the first line. On the second line print $n$ integers $c_1, c_2, \dots, c_n$ (each in $\{1, 2, 3\}$), where $c_i$ is the cycle assigned to person $i$. Any valid allocation is accepted.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
