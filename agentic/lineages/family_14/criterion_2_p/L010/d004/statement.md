# Centralized Diagnostic Routing

Time limit: 2 s   Memory limit: 256 MB

## Description

An industrial manufacturing complex features $n$ distinct workstations. These are linked by $m$ bidirectional conveyor belts. The facility's infrastructure ensures that all workstations are interlinked in a single contiguous network. To minimize maintenance costs, the total number of belts $m$ is strictly fixed at exactly $n - 1$.

A specific subset of $t$ workstations are designated as quality control stations. To perform a full system diagnostic, you must designate exactly one workstation in the complex to serve as the temporary central diagnostic hub. This hub can be any of the $n$ workstations (it does not need to be one of the quality control stations). 

You must then supply power to a chosen set of conveyor belts. A quality control station can successfully participate in the diagnostic if there is a continuous sequence of powered belts connecting it to the chosen central diagnostic hub. Activating the belt between workstation $u$ and workstation $v$ incurs a specific energy overhead $w$. Once a belt is powered, it can transmit diagnostic data for any number of quality control stations simultaneously without additional energy costs.

Your task is to determine the minimum possible total energy overhead required to power a set of belts such that there exists at least one valid central diagnostic hub reachable by all $t$ quality control stations.

## Input

The first line provides three integers: $n$, $m$, and $t$. The facility's blueprint supports a maximum of two hundred thousand workstations ($1 \le n \le 200000$). The number of belts $m$ is always $n - 1$. The number of quality control stations $t$ can range from a single station up to the entire facility ($1 \le t \le n$).

The second line contains $t$ distinct integers representing the IDs of the quality control stations.

Following this, there are $m$ lines, each detailing a single conveyor belt with three integers: $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$). The energy overhead $w$ for any single belt is at least one and does not exceed one million units ($1 \le w \le 1000000$). 

## Output

Print a single integer: the minimum total energy overhead required.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1, if workstation 2 is chosen as the central diagnostic hub, quality control station 1 needs the belt between 1 and 2 powered (overhead 5). Quality control station 4 needs the belts between 4 and 3, and 3 and 2 powered (overheads 2 and 1). The total overhead is 5 + 2 + 1 = 8. Alternatively, choosing workstation 3 as the hub requires exactly the same belts to be powered. The minimum possible total overhead is 8.
In Example 2, there is only one quality control station. It can be designated as its own central diagnostic hub, requiring no belts to be powered.