# Problem A — Reactive Storage

Time limit: 2 s   Memory limit: 256 MB

A facility has three storage silos labeled 1, 2, 3. There are n chemicals. Some pairs of chemicals are reactive and must not be placed in the same silo. Assign every chemical to exactly one of the three silos so that no reactive pair shares a silo, or report that it is impossible.

## Input
The first line contains two integers n and m — the number of chemicals and the number of reactive pairs (1 ≤ n ≤ 40, 0 ≤ m ≤ n·(n−1)/2).
Each of the next m lines contains two integers u v — a reactive pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers s₁ s₂ … sₙ (each in {1,2,3}), where sᵢ is the silo of chemical i. Any valid assignment is accepted.

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
