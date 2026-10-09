# Problem A — Operations Scheduling

Time limit: 2 s   Memory limit: 256 MB

An organization must assign its n members to an operations schedule. The available schedule codes are 1, 2, and 3. Certain combinations of two members interfere with each other and must not receive the same schedule code. Assign every member exactly one schedule code so that no two interfering members share a code, or report that it is impossible.

## Input
The first line contains two integers n and m — the number of members and the number of interfering combinations (1 ≤ n ≤ 40, 0 ≤ m ≤ n·(n−1)/2).
Each of the next m lines contains two integers u v — a combination of two members that interfere.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers s₁ s₂ … sₙ (each in {1,2,3}), where sᵢ is the schedule code of member i. Any valid assignment is accepted.

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
