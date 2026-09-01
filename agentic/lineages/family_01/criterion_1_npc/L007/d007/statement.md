# Problem A — Security Clearance Resolution

Time limit: 2 s   Memory limit: 256 MB

A secure facility is configuring the access levels for a network of $n$ interdependent modules. Each module must receive exactly one access level from the set $\{1, 2, 3\}$.

To prevent critical vulnerabilities, the facility evaluates the entire network's configuration using an energy minimization model based on $m$ separation protocols. Each protocol specifies a pair of interacting modules. 

When a module $u$ is assigned an access level $c_u \in \{1, 2, 3\}$, it generates a 3-dimensional polarization vector $\mathbf{v}_u = (v_{u,1}, v_{u,2}, v_{u,3})$. The $k$-th component of this vector (for $k \in \{1, 2, 3\}$) is defined as:
- $v_{u,k} = 2$ if $k = c_u$
- $v_{u,k} = -1$ if $k \neq c_u$

For any two modules $u$ and $v$ linked by a separation protocol, their pairwise interference energy $\Delta E(u, v)$ is calculated as the standard dot product of their polarization vectors:
$$ \Delta E(u, v) = \mathbf{v}_u \cdot \mathbf{v}_v $$

The total interference energy of the network is defined as the sum of $\Delta E(u, v)$ across all $m$ separation protocols. The network is deemed completely stable if and only if its total interference energy is exactly $-3m$.

The test suite contains maximum-size adversarial instances. Naive generation of all assignments will result in an astronomical number of dead ends and will exceed the time limit before a stable state is found or proven impossible.

Your task is to determine if there exists a complete access assignment that makes the network completely stable. If at least one valid assignment exists, you must identify the one that is lexicographically smallest.

## Input
The first line of the input provides two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). These represent the total number of modules and the number of separation protocols, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that module $u$ and module $v$ are linked by a separation protocol.

## Output
If no completely stable assignment can be found, print `NO` on a single line.
If a stable assignment is possible, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2, 3\}$) representing the access level assigned to each respective module. Among all valid stable configurations, the sequence of access levels you output must be the lexicographically smallest (i.e., comparing the access level of module 1 first, then module 2, and so forth).

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