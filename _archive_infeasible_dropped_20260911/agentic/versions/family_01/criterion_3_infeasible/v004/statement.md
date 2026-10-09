# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory still has only two shifts, 1 and 2, but the roster is known to be hopeless. Your job is not to schedule — it is to search the expansive space of all possible worker subsets to certify the impossibility. A subset is entirely incompatible if every individual in it conflicts with every other individual in that same subset. It is guaranteed that the conflict data contains at least one entirely incompatible subset of exactly three workers. Any such set proves two shifts cannot suffice. Output one such set of three.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000,
3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)).
Each of the next m lines contains two integers u v — a conflicting pair.
It is guaranteed that at least one such triple exists.

## Output
Print three integers a b c on one line with a < b < c such that all three pairs
a–b, a–c, b–c are conflicts. Output the lexicographically smallest such triple
(smallest a; ties by smallest b; then smallest c).

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
