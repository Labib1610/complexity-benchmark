# Problem A — Schedule Constraints

Time limit: 2 s   Memory limit: 256 MB

A factory runs shifts labeled 1, 2, and 3. There are n workers. Certain workers have a restriction and must not be placed on the same shift as each other. Assign every worker to exactly one of the available shifts so that no restricted workers share a shift, or report that it is impossible.

## Input
The first line contains two integers n and m — the number of workers and the number of restrictions (1 ≤ n ≤ 40, 0 ≤ m ≤ n·(n−1)/2).
Each of the next m lines contains two integers u v — two workers that cannot share a shift.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers s₁ s₂ … sₙ (each in {1,2,3}), where sᵢ is the shift of worker i. Among all valid assignments output the lexicographically smallest sequence (compare s₁ first, then s₂, and so on).

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
