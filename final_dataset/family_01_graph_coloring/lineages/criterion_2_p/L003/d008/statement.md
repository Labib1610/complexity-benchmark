# Problem B — System Configuration

Time limit: 1 s   Memory limit: 256 MB

A cloud provider must configure the operation mode for $n$ database instances. The configuration requires assigning each instance $i$ an operation mode $s_i$, which must be chosen from the set $\{1, 2\}$.

The system includes $m$ shared backup storage arrays, each connecting two specific database instances. A backup array continuously monitors the joint state of its two connected instances. To prevent data collision, the configuration must guarantee that for every backup array connecting instances $u$ and $v$, they are assigned different operation modes (i.e., $s_u \neq s_v$).

You must assign a mode to each instance to satisfy all collision constraints across all backup arrays, or determine that no such configuration exists. 

If multiple valid configurations exist, the automated deployment system requires the configuration that minimizes the total network energy score $E$, defined as:
$$E = \sum_{i=1}^n s_i \cdot 2^{n-i}$$

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of database instances and the number of shared backup arrays.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that instances $u$ and $v$ share a backup array.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the valid configuration with the minimum energy score.

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