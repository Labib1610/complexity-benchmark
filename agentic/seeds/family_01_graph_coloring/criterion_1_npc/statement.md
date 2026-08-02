# Problem A — Trichrome Shifts

Time limit: 2 s   Memory limit: 256 MB

A factory runs three shifts labeled 1, 2, 3. There are n workers. Some pairs of
workers are in conflict and must not be placed on the same shift. Assign every
worker to exactly one of the three shifts so that no conflicting pair shares a
shift, or report that it is impossible.

## Input
The first line contains two integers n and m — the number of workers and the
number of conflict pairs (1 ≤ n ≤ 40, 0 ≤ m ≤ n·(n−1)/2).
Each of the next m lines contains two integers u v — a conflicting pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s₁ s₂ … sₙ (each in {1,2,3}), where sᵢ is the shift of worker i. Among all valid
assignments output the lexicographically smallest sequence (compare s₁ first,
then s₂, and so on).

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
