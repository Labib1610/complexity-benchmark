# Problem A — Zone Distribution

Time limit: 2 s   Memory limit: 256 MB

A cloud application runs across three availability zones labeled 1, 2, 3. There are n microservices. Some pairs of microservices provide redundant backups for each other and must not be placed in the same availability zone to prevent simultaneous failures. Assign every microservice to exactly one of the three availability zones so that no redundant pair shares a zone, or report that it is impossible.

## Input
The first line contains two integers n and m — the number of microservices and the number of redundant pairs (1 ≤ n ≤ 40, 0 ≤ m ≤ n·(n−1)/2).
Each of the next m lines contains two integers u v — a redundant pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers z₁ z₂ … zₙ (each in {1,2,3}), where zᵢ is the availability zone of microservice i. Among all valid assignments output the lexicographically smallest sequence (compare z₁ first, then z₂, and so on).

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
