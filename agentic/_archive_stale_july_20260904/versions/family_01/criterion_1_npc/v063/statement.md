# Problem A — Deployment Rings

Time limit: 2 s   Memory limit: 256 MB

You are configuring a distributed application comprising $n$ microservices, indexed by integers from 1 to $n$. Each microservice must be allocated to an isolation ring. An isolation ring is identified by a positive integer strictly less than 4.

During load testing, specific pairs of microservices have demonstrated resource-contention defects. If both microservices in such a pair are deployed in the exact same isolation ring, the application will crash. To ensure operational stability, you must place the two microservices of any defective pair into completely distinct rings.

Your task is to find a valid ring allocation for all $n$ microservices. When multiple valid configurations exist, you must select the one that assigns the lowest possible ring number to microservice 1. If there are still multiple options, you must resolve the tie by minimizing the ring number for microservice 2, and so on, proceeding sequentially up to microservice $n$. If no valid allocation can be found, you must state that it is impossible.

## Input
The first line contains $n$ and $m$ — the number of microservices and the number of defective pairs. The number of microservices is at least one, and it cannot exceed the total number of available CPU cores across the cluster (which consists of exactly 5 servers, each containing exactly 8 cores). The number of defective pairs $m$ is at least zero and is bounded by the maximum number of distinct unordered pairs that can be formed from the $n$ microservices.

The following $m$ lines each contain two integers $u$ and $v$, indicating that microservice $u$ and microservice $v$ share a resource-contention defect.

## Output
If it is impossible to stabilize the application, output a single line with the word NO.
Otherwise, output YES on the first line. On the second line, output $n$ integers separated by spaces, representing the isolation rings assigned to microservices 1 through $n$ respectively, following the tie-breaking rules described above.

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
