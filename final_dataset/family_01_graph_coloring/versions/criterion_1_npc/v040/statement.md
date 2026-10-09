# Problem A — Deployment Pipeline Allocation

Time limit: 2 s   Memory limit: 256 MB

Before rolling out a new microservice architecture, an automated static analyzer scans the $n$ core services to detect shared resource locks. This preliminary step produces a raw log of $m$ interacting service pairs.

Your software module sits in the middle of the continuous integration pipeline. It receives the analyzer's log of interacting pairs. The deployment environment provides a trio of isolated execution clusters, designated by the identifiers 1, 2, and 3. You must determine an allocation where each service is placed into exactly one of these clusters. To prevent runtime deadlocks, any two services that appear together in a logged pair must be placed into different clusters.

Once your module outputs a valid allocation, the downstream provisioner will automatically spin up the clusters and initialize the services. If you determine that no valid allocation exists for the given log, the pipeline will halt so engineers can manually refactor the services.

## Input
The first line contains two integers $n$ and $m$ — the number of core services and the number of interacting pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of services flagged by the analyzer.

## Output
If the pipeline must halt because no valid allocation exists, print a single line NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the cluster identifier allocated to service $i$. Any valid allocation is accepted.

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
