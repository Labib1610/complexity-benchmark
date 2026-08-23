# Problem C — Special Report

Time limit: 2 s   Memory limit: 256 MB

The factory requires a report on worker incompatibilities. You are given a list of pairs of workers who cannot work together. Your task is to find a set of exactly three workers such that every pair among them is incompatible. It is guaranteed that at least one such set of three workers exists. Output one such set.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000,
3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)).
Each of the next m lines contains two integers u v — an incompatible pair of workers.
It is guaranteed that at least one such triple exists.

## Output
Print three integers a b c on one line with a < b < c such that all three pairs
a–b, a–c, b–c are incompatible. Output the lexicographically smallest such triple
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
