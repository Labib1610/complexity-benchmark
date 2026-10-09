# Problem A — Refinery Valve Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description
A chemical refinery regulates its flow using $n$ diverter valves. Every valve must be locked into either its primary position or its secondary position before the process begins; no intermediate states are mechanically possible. 

Throughout the facility, $m$ independent pressure monitors ensure the system operates within safe tolerances. Each monitor is hardwired to check exactly three specific valve conditions. A condition is simply a requirement that a particular valve be set to a specific position (for instance, "Valve 4 in the primary position" or "Valve 7 in the secondary position"). A monitor will report a safe status if at least one of its three hardwired conditions is actively met by the current valve settings. If none of the three conditions are met, the monitor detects a critical pressure imbalance and triggers an immediate plant-wide shutdown. 

Because the monitors are distributed across overlapping pipe networks, the same valve is often checked by multiple monitors. One monitor might require a valve to be in its primary position to remain safe, while another monitor might require the same valve to be in its secondary position. 

Your objective is to evaluate the entire network of monitors. You must find a single, comprehensive configuration for all $n$ valves that causes every single one of the $m$ monitors to report a safe status simultaneously. If such a configuration exists, you must provide it; if the conflicting requirements make it impossible to satisfy all monitors at once, you must determine that no valid configuration exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$), representing the number of valves and the number of monitors, respectively.
Each of the following $m$ lines corresponds to a monitor and contains exactly three non-zero signed integers $l_1, l_2, l_3$ ($|l_i| \le n$). 
A positive integer $i$ represents a condition that valve $i$ is in the primary position. A negative integer $-i$ represents a condition that valve $i$ is in the secondary position.

## Output
If no configuration can keep all monitors safe, print `NO` on a single line.
If a valid configuration exists, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$). Here, $s_i = 1$ means valve $i$ is placed in the primary position, and $s_i = 0$ means it is placed in the secondary position. If multiple valid configurations exist, any of them will be accepted.

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
Each monitor always checks exactly three conditions. The same valve index might be checked more than once by a single monitor.
