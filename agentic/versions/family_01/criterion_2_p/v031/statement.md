# Problem B — Frequency Allocation

Time limit: 1 s   Memory limit: 256 MB

The new broadcast network uses only two frequencies, labeled 1 and 2. With n stations and m interference pairs, assign each station a frequency so that no interfering pair shares a frequency, or report impossibility.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 2·10⁵, 0 ≤ m ≤ 2·10⁵).
Each of the next m lines contains two integers u v — an interfering pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with n integers f₁ … fₙ (each in {1,2}), the lexicographically smallest valid assignment.

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
