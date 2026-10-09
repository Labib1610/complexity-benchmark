# Problem A — Polymer Synthesis Configuration

Time limit: 2 s
Memory limit: 256 MB

## Description
A manufacturing plant is configuring the synthesis process for a new polymer involving $n$ possible catalysts. The process requires a binary decision for each catalyst: it must be strictly active or strictly inactive, with no intermediate states permitted. 

During pilot testing, quality control engineers recorded $m$ safety protocols that the configuration must respect. Each protocol specifies exactly three conditions, where a condition is a demand that a particular catalyst be active or a demand that it be inactive. 

To ensure a stable reaction, a protocol is considered satisfied if and only if at least one of its three conditions is met by the final configuration. A protocol is violated if the configuration meets none of its three conditions. 

Your task is to determine if there exists a single global assignment of active and inactive states for all $n$ catalysts that satisfies all $m$ safety protocols simultaneously. If such a configuration is possible, you must provide one valid example.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$), representing the number of catalysts and the number of safety protocols.

Each of the subsequent $m$ lines corresponds to a safety protocol and contains three non-zero integers $l_1, l_2, l_3$ ($|l_i| \le n$). A positive value $l_i$ indicates a condition where catalyst $|l_i|$ is active, while a negative value indicates a condition where catalyst $|l_i|$ is inactive.

## Output
If there is no way to configure the catalysts to satisfy all protocols, output a single line containing `NO`.

If a valid configuration exists, output `YES` on the first line. On the second line, output $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each either 0 or 1), where $s_i = 1$ means catalyst $i$ is active, and $s_i = 0$ means catalyst $i$ is inactive. Any valid configuration is accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each protocol always lists exactly three conditions, though the same catalyst might be referenced multiple times within a single protocol.
