# Problem A — Tri-cycle Operations

Time limit: 2 s   Memory limit: 256 MB

A factory runs three operational cycles labeled 1, 2, 3. There are n machines. Some pairs of machines share a power line and must not be placed on the same cycle. Assign every machine to exactly one of the three cycles so that no sharing pair shares a cycle, or report that it is impossible.

## Input
The first line contains two integers n and m — the number of machines and the number of sharing pairs (1 ≤ n ≤ 40, 0 ≤ m ≤ n·(n−1)/2).
Each of the next m lines contains two integers u v — a sharing pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers c₁ c₂ … cₙ (each in {1,2,3}), where cᵢ is the cycle of machine i. Among all valid assignments output the lexicographically smallest sequence (compare c₁ first, then c₂, and so on).

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
