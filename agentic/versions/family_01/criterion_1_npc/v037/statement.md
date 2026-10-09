# Problem A — Trichrome Shifts

Time limit: 2 s   Memory limit: 256 MB

A factory runs three shifts labeled 1, 2, 3. There are n workers. Some pairs of workers are in conflict and must not be placed on the same shift. Assign every worker to exactly one of the three shifts so that no conflicting pair shares a shift, or report that it is impossible.

## Input
The first line contains two integers n and m — the number of workers and the number of conflict pairs. The number of workers n is at least a single individual, and cannot exceed the maximum capacity of the staff room, which contains exactly 5 tables that each seat exactly 8 workers. The number of conflict pairs m is non-negative and bounded by the total number of distinct two-person pairs that can be formed from the n workers.
Each of the next m lines contains two integers u v — a conflicting pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers s₁ s₂ … sₙ (each in {1,2,3}), where sᵢ is the shift of worker i. Any valid assignment is accepted.

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
