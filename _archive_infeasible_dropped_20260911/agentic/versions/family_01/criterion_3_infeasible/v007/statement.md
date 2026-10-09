# Shift Assignment Failure Report

Time limit: 2 s   Memory limit: 256 MB

The manufacturing facility operates with exactly two daily production periods. The provided list of personnel incompatibilities is already known to be unresolvable. Your task is to generate a formal failure report rather than a schedule. The database guarantees the existence of at least one group of three employees who mutually refuse to work together. Documenting any such group provides conclusive evidence that two production periods are inadequate. Output one such group.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the number of employees and the number of incompatibility records.
Each of the next m lines contains two integers u v — representing a pair of employees who refuse to work in the same production period.
It is guaranteed that at least one such mutually incompatible group of three exists.

## Output
Print three integers a b c on one line with a < b < c such that all three pairs a–b, a–c, and b–c are listed as incompatibilities. Output the lexicographically smallest such group (smallest a; ties broken by smallest b; then smallest c).

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
