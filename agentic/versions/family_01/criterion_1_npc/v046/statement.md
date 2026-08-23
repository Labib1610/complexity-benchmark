# Problem A — Distributed Deployment Configuration

Time limit: 2 s   Memory limit: 256 MB

You must deploy $n$ service instances into three isolated hosting environments, designated 1, 2, and 3. Each service instance must be assigned to exactly one of these environments.

To ensure fault tolerance, the deployment is subject to a set of mutual exclusion rules. Each rule specifies a pair of instances that cannot be deployed into the same environment. Your task is to determine whether a valid deployment configuration exists.

If multiple valid configurations are possible, the deployment system requires the one that prioritizes lower-numbered environments for lower-numbered instances. Specifically, when comparing two valid configurations, find the lowest-numbered instance where they differ; the configuration that assigns this instance to the smaller environment number is strictly preferred.

## Input
The first line contains two integers $n$ and $m$ — the number of service instances and the number of mutual exclusion rules ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a mutually exclusive pair of instances.

## Output
If no valid deployment configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $e_1, e_2, \dots, e_n$ (each in $\{1, 2, 3\}$), where $e_i$ is the environment assigned to service instance $i$. Output the single strictly preferred configuration as defined above.

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
