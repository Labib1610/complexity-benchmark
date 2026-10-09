# Problem A — Tri-zone Enclosures

Time limit: 2 s   Memory limit: 256 MB

A sanctuary manages three enclosures labeled 1, 2, 3. There are n animals. Some pairs of animals are incompatible and must not be placed in the same enclosure. Assign every animal to exactly one of the three enclosures so that no incompatible pair shares an enclosure, or report that it is impossible.

## Input
The first line contains two integers n and m — the number of animals and the number of incompatible pairs (1 ≤ n ≤ 40, 0 ≤ m ≤ n·(n−1)/2).
Each of the next m lines contains two integers u v — an incompatible pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers e₁ e₂ … eₙ (each in {1,2,3}), where eᵢ is the enclosure of animal i. Any valid assignment is accepted.

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
