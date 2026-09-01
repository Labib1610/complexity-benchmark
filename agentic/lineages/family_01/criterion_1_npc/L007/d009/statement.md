# Problem A — Channel Separation Configuration

Time limit: 2 s   Memory limit: 256 MB

A data center needs to assign a channel $c_u \in \{1, 2, 3\}$ to each of $n$ communication nodes.
There are $m$ interference links, each connecting a pair of nodes.

To evaluate the configuration, each channel is associated with a 2D signature vector $\vec{w}$:
- Channel 1 uses $\vec{w}_1 = (-1, \sqrt{3})$.
- Channel 2 uses $\vec{w}_2 = (-1, -\sqrt{3})$.
- Channel 3 uses $\vec{w}_3 = (2, 0)$.

For each of the $m$ links connecting a pair of nodes $u$ and $v$, the link's stress is defined as the squared Euclidean length (the square of the magnitude) of the vector sum $\vec{w}_{c_u} + \vec{w}_{c_v}$. 

The overall network is considered fully separated if and only if the sum of the stress values across all $m$ links is exactly $4m$.

Your task is to determine if there exists a channel assignment that makes the network fully separated. If at least one valid assignment exists, you must identify the one that is lexicographically smallest.

## Input
The first line of the input provides two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). These represent the total number of nodes and the number of interference links, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that node $u$ and node $v$ are connected by an interference link.

## Output
If no fully separated assignment can be found, print `NO` on a single line.
If a valid assignment is possible, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2, 3\}$) representing the channel assigned to each respective node. Among all valid configurations, the sequence of channels you output must be the lexicographically smallest (i.e., comparing the channel of node 1 first, then node 2, and so forth).

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