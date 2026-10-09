# Problem C — Roster Evaluation

Time limit: 2 s   Memory limit: 256 MB

The factory maintains a roster of workers and a list of conflicts. Your job is to analyze the roster. It is guaranteed that the given data contains at least one set of three workers who pairwise conflict. Output one such set.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)).
Each of the next m lines contains two integers u v — a conflicting pair.
It is guaranteed that at least one such triple exists.

## Output
Print three integers a b c on one line with a < b < c such that all three pairs a–b, a–c, b–c are conflicts. Output the lexicographically smallest such triple (smallest a; ties by smallest b; then smallest c).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
