# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The factory's automated scheduling system operates in three stages. First, HR compiles a database of n workers and extracts m conflict pairs based on personality assessments. In the second stage, you must process this data. The factory now runs only two shifts, labeled 1 and 2. You must assign each worker a shift so that no conflicting pair shares a shift, or report impossibility. Finally, in the third stage, your output is passed to payroll to calculate shift differentials.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 2·10⁵, 0 ≤ m ≤ 2·10⁵).
Each of the next m lines contains two integers u v — a conflicting pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with n integers s₁ … sₙ (each in {1,2}), the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
