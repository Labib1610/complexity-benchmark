# Problem A — Ring Architecture

Time limit: 2 s   Memory limit: 256 MB

A new operating system kernel organizes its background processes into three isolated execution rings, designated as Ring 1, Ring 2, and Ring 3. During system boot, $n$ background services (numbered 1 through $n$) must be distributed among these three rings. Every service must be assigned to exactly one ring.

Due to legacy code, certain pairs of services attempt to lock the same hardware registers. If two such services are assigned to the same execution ring, a deadlock will occur. You have been provided with a list of all unsafe service pairs.

Determine if there is a valid deployment configuration that avoids all potential deadlocks, and if so, provide one such configuration.

## Input
The first line contains two integers $n$ and $m$ — the total number of background services and the number of unsafe legacy pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$ — the identifiers of two services that will cause a deadlock if they operate in the same ring.

## Output
If a safe deployment is impossible, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $r_1, r_2, \dots, r_n$ (each in the set $\{1, 2, 3\}$), where $r_i$ is the execution ring assigned to service $i$. If multiple valid deployments exist, you may output any of them.

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
