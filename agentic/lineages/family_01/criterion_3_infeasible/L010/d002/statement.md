# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory still has only two shifts, 1 and 2, but the roster is known to be hopeless. Your job is not to schedule — it is to search the conflict data to certify the impossibility. 

A deadlock is defined as a subset of exactly three conflict records that, across their six total positions, contain exactly three distinct worker IDs. Furthermore, each of these three IDs must appear in exactly two of the three records. Such a configuration provides an undeniable certificate that two shifts cannot suffice. Finding such a deadlock can appear daunting given the sheer number of possible subsets to check.

It is guaranteed that the conflict data contains at least one such deadlock. Output the worker IDs involved in one such deadlock.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)).
Each of the next m lines contains two integers u v — a conflict record representing a pair of workers who cannot work together.
It is guaranteed that at least one deadlock exists.

## Output
Print three integers a b c on one line with a < b < c representing the three distinct workers involved in the deadlock. Output the lexicographically smallest such group of workers (smallest a; ties by smallest b; then smallest c).

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