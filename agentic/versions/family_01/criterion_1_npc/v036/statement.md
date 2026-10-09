# Problem A — Machinery Rotations

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant operates continuously across a morning (1), afternoon (2), and night (3) rotation. Each of the n employees must be scheduled for exactly one of these periods. 

Certain employees rely on the same specialized heavy machinery. Because only one person can operate this machinery at a time, these specific employees cannot be scheduled for the same rotation. 

Determine a rotation schedule for all employees that satisfies these machinery restrictions, or determine if no such schedule is possible.

## Input
The first line contains two integers n and m — the number of employees and the number of machinery restrictions (1 ≤ n ≤ 40, 0 ≤ m ≤ n·(n−1)/2).
Each of the next m lines contains two integers u v — two employees who rely on the same machinery.

## Output
If no valid schedule exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers s₁ s₂ … sₙ (each in {1,2,3}), where sᵢ is the rotation of employee i. Any valid schedule is accepted.

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
