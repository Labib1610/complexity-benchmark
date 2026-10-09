# Problem B — Spacecraft Thermal Management

Time limit: 1 s   Memory limit: 256 MB

## Description
You are programming the automated thermal control system for a new orbital station. The station relies on $n$ coolant valves. Each valve must be permanently locked into one of two operational modes: bypass mode (represented as 1) or radiator mode (represented as 0).

To ensure the station does not suffer catastrophic temperature fluctuations, the engineering team has established $m$ safety protocols. Every protocol dictates two acceptable valve conditions. A protocol is considered secure as long as at least one of its two conditions is currently met by the valves. The entire thermal control system is stable only if all $m$ protocols are simultaneously secure.

Each condition in a protocol refers to a single valve and the mode it should be in. You need to determine if there is a way to configure all $n$ valves such that no safety protocol is violated.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of coolant valves and the number of safety protocols.

The following $m$ lines each detail a safety protocol using two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$). 
- A positive integer $x$ indicates a condition where valve $x$ is placed in bypass mode.
- A negative integer $x$ indicates a condition where valve $|x|$ is placed in radiator mode.

## Output
If there is no way to set the valves to secure all protocols, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{0, 1\}$), where $s_i$ is the mode assigned to valve $i$ (1 for bypass mode, 0 for radiator mode). If there are multiple valid configurations, you may print any of them.

## Example 1
### Input
```
2 2
1 2
-1 -2
```
### Output
```
YES
1 0
```

## Example 2
### Input
```
1 2
1 1
-1 -1
```
### Output
```
NO
```

## Note
The same valve condition may appear in multiple different safety protocols.
