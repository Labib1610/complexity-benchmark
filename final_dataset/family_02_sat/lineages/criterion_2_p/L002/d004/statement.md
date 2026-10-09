# Problem B — Production Line Configuration

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing facility runs $n$ distinct machines. Each machine must be securely locked into one of two states: mode 0 or mode 1. The facility's power grid is safeguarded by $m$ safety interlocks. Each interlock receives two signal feeds from the machines. 

A signal feed is defined by a non-zero integer $c$. The feed carries a high voltage depending on the mode of machine $|c|$:
- If $c > 0$, the feed carries a high voltage when machine $c$ is set to mode 0.
- If $c < 0$, the feed carries a high voltage when machine $|c|$ is set to mode 1.

A catastrophic shutdown is triggered by an interlock if and only if both of its signal feeds carry a high voltage at the exact same time. To keep the facility running, you must determine a facility-wide configuration (assigning mode 0 or mode 1 to each machine) such that no interlock receives two high voltage feeds simultaneously. 

Determine if a safe configuration exists, and if so, output the required mode for each machine.

## Input
The first line of the input provides two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of machines and the number of safety interlocks, respectively.

The next $m$ lines each contain two non-zero integers $c_1$ and $c_2$ ($|c_i| \le n$), detailing the two signal feeds for that interlock. 

## Output
If it is impossible to configure all $n$ machines without causing a shutdown, output a single line with the word `NO`.

If a safe configuration is possible, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) to specify the chosen mode for each machine from 1 to $n$.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
There might be several safe configurations; outputting any valid one is correct. A single machine can provide signal feeds to multiple interlocks.