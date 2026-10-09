# Pipeline Sensor Integration

Time limit: 5 s   Memory limit: 256 MB

## Description
A pipeline monitoring system requires installing $n$ distinct sensors into $n$ evenly spaced access ports along a straight pipe. The ports are numbered sequentially from 1 to $n$. Each sensor must be assigned to exactly one port.

The sensors are configured in a strict chain of command. Except for a single master controller, every sensor transmits its readings to exactly one designated receiver sensor. This configuration ensures all data flows to the master controller without any redundant communication loops.

To establish these connections, a dedicated fiber optic strand must be run between each sensor and its designated receiver. The length of the strand required for any connection is equal to the absolute difference between the port numbers of the two linked sensors.

The project has a total fiber optic cable budget of $B$ to wire all connections. Determine a valid assignment of sensors to ports whose combined strand length is at most $B$, or determine if it is impossible.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a communication link that must be wired between sensor $u$ and sensor $v$. It is guaranteed that $m = n - 1$ and the links form the chain of command described above.

## Output
If an assignment is possible, print `YES` on the first line. On the second line, print $n$ integers representing the port numbers (from $1$ to $n$) assigned to sensors $1$ through $n$, respectively.
If it is impossible, print `NO`.

## Example

### Input
```
5 4 6
1 2
1 3
1 4
1 5
```

### Output
```
YES
3 1 2 4 5
```
