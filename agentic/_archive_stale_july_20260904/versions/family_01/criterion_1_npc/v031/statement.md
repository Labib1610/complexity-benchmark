# Problem A — Orbital Zones

Time limit: 2 s   Memory limit: 256 MB

A space agency manages three orbital zones labeled 1, 2, 3. There are n satellites. Some pairs of satellites cause signal interference and must not be placed in the same orbital zone. Assign every satellite to exactly one of the three orbital zones so that no interfering pair shares a zone, or report that it is impossible.

## Input
The first line contains two integers n and m — the number of satellites and the number of interference pairs (1 ≤ n ≤ 40, 0 ≤ m ≤ n·(n−1)/2).
Each of the next m lines contains two integers u v — an interfering pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers z₁ z₂ … zₙ (each in {1,2,3}), where zᵢ is the orbital zone of satellite i. Among all valid assignments output the lexicographically smallest sequence (compare z₁ first, then z₂, and so on).

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
