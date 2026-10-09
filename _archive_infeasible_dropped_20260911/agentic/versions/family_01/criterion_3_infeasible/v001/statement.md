# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory still has only two assignments, 1 and 2, but the plan is known to be hopeless. Your job is not to schedule — it is to certify the impossibility. It is guaranteed that the list of constraints contains at least one set of three workers who mutually interfere. Any such set proves two assignments cannot suffice. Output one such set.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000,
3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)).
Each of the next m lines contains two integers u v — an interfering pair of workers.
It is guaranteed that at least one such set of three workers exists.

## Output
Print three integers a b c on one line with a < b < c such that all three pairs
a–b, a–c, b–c are interfering. Output the lexicographically smallest such set
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
