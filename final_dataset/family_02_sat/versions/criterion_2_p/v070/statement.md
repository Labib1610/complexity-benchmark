# Problem B — Telemetry Calibration Sequence

Time limit: 1 s
Memory limit: 256 MB

## Description
The trajectory analysis division has generated a list of $m$ safety protocols for the observatory's $n$ data channels. Your module handles the configuration phase before the deep-space data collection sequence begins. 

Each of the $n$ channels must be locked into exactly one of two operational modes: high-gain or low-gain. 

Each of the $m$ safety protocols monitors exactly two specific channel modes. A protocol operates via a strict redundancy mechanism evaluated against your final configuration: if the first monitored mode is absent, the protocol requires the second monitored mode to be present. Conversely, if the second monitored mode is absent, the protocol requires the first monitored mode to be present. If both monitored modes are present, the protocol is inherently satisfied.

You must determine whether it is possible to assign a mode to all $n$ channels such that no safety protocol is violated. If the protocols fundamentally conflict, you must report the failure so the trajectory can be aborted and recalculated.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of data channels and the number of safety protocols, respectively.

Each of the following $m$ lines describes a single safety protocol using two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$). The absolute value $|l_i|$ indicates the channel identifier. A positive value means the protocol monitors for the high-gain mode on that channel, while a negative value means it monitors for the low-gain mode.

## Output
If no valid configuration exists that satisfies all protocols, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i$ is `1` if channel $i$ is set to high-gain, and `0` if it is set to low-gain. If multiple valid configurations exist, any of them will be accepted.

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
