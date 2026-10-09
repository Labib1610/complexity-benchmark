# Problem A — Eclipse Protocol Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description
A satellite features $n$ distinct internal subsystems. At any given time, each subsystem operates in exactly one of two modes: ACTIVE or STANDBY. There are no intermediate or alternative modes.

The science team has compiled a list of $m$ observation protocols to be run during an upcoming eclipse. Every protocol is strictly defined by three operational requirements. Each requirement targets one specific subsystem and mandates that it be in a specific mode (either ACTIVE or STANDBY). 

During the eclipse, a protocol is considered successfully executed if the satellite's overall configuration aligns with at least one of the three requirements defining that protocol. If a protocol's three requirements are all mismatched with the satellite's configuration, that protocol fails.

Your task is to determine whether it is possible to assign a permanent mode to every one of the $n$ subsystems such that every single one of the $m$ protocols is successfully executed simultaneously. If such a configuration is possible, you must provide it. If no such configuration exists, you must report that the schedule is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
The following $m$ lines each describe a protocol using three non-zero integers $c_1$, $c_2$, and $c_3$.
The absolute value $|c_i|$ indicates the required subsystem ($1 \le |c_i| \le n$).
A positive integer indicates the requirement is for the subsystem to be ACTIVE.
A negative integer indicates the requirement is for the subsystem to be STANDBY.
The same subsystem can be targeted multiple times by the requirements of a single protocol.

## Output
If there is no valid mode assignment for the subsystems that executes all protocols, print NO on a single line.
Otherwise, print YES on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$), where $s_i$ represents the mode of subsystem $i$ ($1$ for ACTIVE, $0$ for STANDBY). Any valid configuration is accepted.

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
