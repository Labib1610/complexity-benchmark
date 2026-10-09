# Cross-Zone Link Activation

Time limit: 2 s   Memory limit: 256 MB

## Description
A communication network consists of $2q$ endpoints. The network is physically partitioned into two distinct zones to prevent internal interference: Zone A contains endpoints identified by integers 1 through $q$, and Zone B contains endpoints identified by integers $q+1$ through $2q$. 

You are provided with a survey of $t$ viable bidirectional links. Due to the hardware constraints of the partition, a viable link is strictly formed by crossing between the zones—meaning it connects exactly one endpoint from Zone A with exactly one endpoint from Zone B. The provided survey exclusively contains links that obey this crossing rule.

Your objective is to lock in a subset of these viable links to form a complete network configuration. A complete configuration requires that every single endpoint in the network (from 1 to $2q$) is utilized by exactly one locked-in link. 

Determine whether it is possible to establish this configuration. If it is achievable, output the links that should be locked in; otherwise, indicate that it cannot be done.

## Input
The first line contains two integers $q$ and $t$ (1 ≤ $q$ ≤ 100000, 0 ≤ $t$ ≤ 400000).
The next $t$ lines each contain two integers $a$ and $b$ (1 ≤ $a$ ≤ $q$ < $b$ ≤ $2q$), representing a viable link between endpoint $a$ and endpoint $b$.

## Output
If a complete configuration is possible, print `YES` on the first line, followed by $q$ lines each containing the two endpoints of a locked-in link. If it is impossible, print `NO`.

## Example 1
### Input
```
3 4
1 4
2 5
3 5
3 6
```
### Output
```
YES
1 4
2 5
3 6
```

## Example 2
### Input
```
2 2
1 3
2 3
```
### Output
```
NO
```
