# Problem B — Optical Orthogonality

Time limit: 1 s
Memory limit: 256 MB

A deep-sea optical network consists of $n$ transceivers. Each transceiver must be configured with a polarization mode chosen from the set $\{1, 2\}$. 

The network includes $m$ bidirectional fiber links, each connecting a specific pair of transceivers. In order to prevent signal reflection, the two transceivers at the endpoints of any link must be configured in orthogonal modes. The hardware controllers verify this by computing the bitwise XOR of the two mode integers. A link will only activate if this bitwise XOR evaluates to exactly 3. If the result is anything else, the link remains inactive.

Your task is to determine whether it is possible to assign a polarization mode to every transceiver such that all $m$ fiber links activate simultaneously.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that a fiber link connects transceiver $u$ and transceiver $v$.

## Output
If it is impossible to configure the network so that all links are active, output a single line containing NO.
Otherwise, output YES on the first line. On the second line, output $n$ integers $p_1 \dots p_n$ (where each $p_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of polarization modes.

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