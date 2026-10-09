# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The facility still has only two time slots, 1 and 2, but the arrangement is known to be hopeless. Your job is not to assign the slots — it is to certify the impossibility. It is guaranteed that the provided list of restrictions contains at least one group of three entities where each entity is restricted with both of the other two. Any such group proves two time slots cannot suffice. Output one such group.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000,
3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)).
Each of the next m lines contains two integers u v — a restricted pair.
It is guaranteed that at least one such group of three exists.

## Output
Print three integers a b c on one line with a < b < c such that all three pairs
a–b, a–c, b–c are restricted. Output the lexicographically smallest such group
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
