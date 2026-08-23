# Vessel Calibration

Time limit: 1 s
Memory limit: 256 MB

You oversee a fleet of $n$ autonomous surveying vessels. Each vessel must be assigned an operational mode $s_i \in \{1, 2\}$. During the mission, there are $m$ proximity events where a pair of vessels will operate in close quarters. To ensure their navigation systems do not interfere, any two vessels involved in a proximity event must be assigned different operational modes.

Your task is to determine a valid operational mode assignment for all $n$ vessels, or report if it is impossible. If multiple valid assignments exist, you must choose the one that yields the minimum overall system cost. The cost is computed through a sequential evaluation process: start with an initial cost $C_0 = 0$. For each vessel $i$ from 1 to $n$ in increasing order, the cumulative cost is updated as $C_i = 2 \cdot C_{i-1} + s_i - 1$. The final system cost evaluated is $C_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of vessels and the number of proximity events.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a proximity event between vessel $u$ and vessel $v$.

## Output
If there is no valid mode assignment, output a single line containing `NO`.
If a valid assignment exists, output `YES` on the first line. On the next line, output $n$ space-separated integers $s_1, \ldots, s_n$ ($s_i \in \{1, 2\}$), representing the operational modes that minimize the final system cost.

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