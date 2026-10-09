# Problem B — Production Line Configuration

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing facility runs $n$ distinct machines. Each machine must be securely locked into one of two operating modes: mode `0` or mode `1`.

The facility's power grid is safeguarded by $m$ safety interlocks. Each interlock receives exactly two mechanical linkages from the machines. 
A linkage is specified in the system by a non-zero integer $c$. The absolute value $|c|$ identifies the specific machine the linkage stems from. The sign of $c$ indicates the linkage's calibration type:
- If $c$ is positive, it is a forward-calibrated linkage. It becomes rigid if its machine operates in mode `0`, and remains flexible in mode `1`.
- If $c$ is negative, it is an inverse-calibrated linkage. It becomes rigid if its machine operates in mode `1`, and remains flexible in mode `0`.

An interlock safely absorbs mechanical stress under normal conditions. However, it has a critical vulnerability: if *both* of its connected linkages become rigid simultaneously, the interlock fractures and triggers a catastrophic facility-wide shutdown.

To keep the facility operational, you must determine a facility-wide configuration (assigning mode 0 or 1 to each machine) such that all $m$ interlocks remain intact. Determine if a safe configuration exists, and if so, output the required mode for each machine.

## Input
The first line of the input provides two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of machines and the number of safety interlocks, respectively.

The next $m$ lines each contain two non-zero integers $c_1$ and $c_2$ ($|c_i| \le n$), detailing the two linkages for that interlock. 

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
There might be several safe configurations; outputting any valid one is correct. A single machine can connect linkages to multiple interlocks.