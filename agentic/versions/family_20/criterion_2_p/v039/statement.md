# Problem B — Data Center Service Windows

Time limit: 2 s   Memory limit: 256 MB

## Description
A data center exchange fabric connects a bank of upstream ports to a bank of downstream ports. Each installed cable joins exactly one upstream port to exactly one downstream port, and no cable ever runs between two ports on the same side. The physical wiring dictates that some ports terminate more cables than others; the port terminating the highest number of cables determines the length of the maintenance cycle. Let this maximum number of cables on a single port be $K$.

Routine maintenance requires taking each cable offline for exactly one service window. During any single service window, a port's internal routing processor can only handle the reconfiguration of a single cable. Consequently, two cables terminating at the same port—whether upstream or downstream—cannot be serviced in the same window. 

Since the busiest port terminates $K$ cables, and none of its cables can share a window, the maintenance cycle requires at least $K$ windows. Your task is to generate a maintenance schedule that uses exactly $K$ service windows. You must assign every cable to a service window from $1$ to $K$ such that no port is involved in more than one cable reconfiguration per window.

## Input
First line: three integers $n_U$, $n_D$, $m$ ($1 \le n_U, n_D \le 100000$, $0 \le m \le 400000$), representing the number of upstream ports, the number of downstream ports, and the number of cables.
Next $m$ lines: two integers $u$ $v$ ($1 \le u \le n_U$, $1 \le v \le n_D$) representing a cable between upstream port $u$ and downstream port $v$.

## Output
Print `YES`, then a line with $m$ integers in $1 \dots K$ — the service window assigned to cable $i$ in input order (cables meeting at any port must be assigned different windows).

## Example

### Input
```text
3 3 4
1 1
1 2
2 2
3 3
```

### Output
```text
YES
1 2 1 1
```
