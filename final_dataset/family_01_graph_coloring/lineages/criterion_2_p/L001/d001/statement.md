# Problem B — Power Bus Redundancy

Time limit: 1 s   Memory limit: 256 MB

An orbital station contains $n$ life-support modules. The automated diagnostic system must configure the backup network by assigning a redundancy tier to each module. This tier must be an integer value of either $1$ or $2$.

The safety protocol includes $m$ critical links. Each link identifies two modules that serve as mutual backups. To guarantee operational stability, the configuration must satisfy a strict numerical condition: for any two modules $u$ and $v$ connected by a critical link, the product of their assigned tier values must equal exactly $2$.

You must determine whether a valid tier assignment exists for all modules. When multiple valid assignments are possible, the diagnostic system mandates selecting the configuration that produces the lexicographically smallest sequence of tier values, ordered by module number from $1$ to $n$.

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a redundancy link between module $u$ and module $v$.

## Output
If there is no way to assign the tier values without violating the safety protocol, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer is the tier value ($1$ or $2$) assigned to the $i$-th module, representing the lexicographically smallest valid configuration.

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