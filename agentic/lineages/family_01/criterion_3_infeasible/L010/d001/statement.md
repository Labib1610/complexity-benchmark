# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory still has only two shifts, 1 and 2, but the roster is known to be hopeless. Your job is not to schedule — it is to search the $2^n$ possible worker combinations to certify the impossibility. A deadlock occurs when a group of three workers is identified where one worker cannot work with a second, the second cannot work with a third, and the third cannot work with the first. Such a deadlock provides an undeniable certificate that two shifts cannot suffice. Finding such a deadlock can appear daunting given the sheer number of possible combinations to check.

It is guaranteed that the conflict data contains at least one such deadlock. Output the members of one such deadlock.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000,
3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)).
Each of the next m lines contains two integers u v — a pair of workers who cannot work together.
It is guaranteed that at least one deadlock exists.

## Output
Print three integers a b c on one line with a < b < c representing the workers in the deadlock. Output the lexicographically smallest such group (smallest a; ties by smallest b; then smallest c).

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