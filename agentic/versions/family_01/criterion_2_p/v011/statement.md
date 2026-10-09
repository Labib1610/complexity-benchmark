# Problem B — Power Bus Redundancy

Time limit: 1 s   Memory limit: 256 MB

An orbital station consists of $n$ life-support modules. To ensure fault tolerance, the station uses two independent power buses, designated as bus 1 and bus 2. Every module must be connected to exactly one of these two buses.

The station's safety protocol defines $m$ critical redundancy links. Each link specifies a pair of modules that provide backup for one another. To prevent a single bus failure from causing a total loss of a backup function, the protocol dictates that for every redundancy link, the module $u$ and module $v$ it connects must be assigned to different buses.

Determine if it is possible to assign each module to a power bus in a way that respects all redundancy links. If there are multiple valid configurations, the automated diagnostic system requires the one that is lexicographically smallest when the bus assignments (1 or 2) are listed in order of the module numbers from $1$ to $n$.

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a redundancy link between module $u$ and module $v$.

## Output
If there is no way to connect the modules to the buses without violating the safety protocol, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer is the bus (1 or 2) assigned to the $i$-th module, representing the lexicographically smallest valid configuration.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
