# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory's automated rostering system operates in three stages. In the first stage, it gathers all pairwise scheduling constraints into a centralized database. In the second stage—which is the component you must implement—the system must process a roster that is already known to be hopeless. The factory has only two shifts, 1 and 2. Your job is not to assign shifts; rather, it is to generate a certificate of impossibility to pass to the third stage. The third stage will then consume this certificate to automatically trigger an expansion request for a third shift.

It is guaranteed that the conflict database contains at least one group of three workers who all mutually conflict with each other. Any such group proves two shifts cannot suffice and serves as a valid certificate. You must output one such group.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)).
Each of the next m lines contains two integers u and v — a conflicting pair.
It is guaranteed that at least one such triple exists.

## Output
Print three integers a, b, and c on one line with a < b < c such that all three pairs a–b, a–c, and b–c are conflicts. Output the lexicographically smallest such triple (smallest a; ties broken by smallest b; then smallest c).

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
