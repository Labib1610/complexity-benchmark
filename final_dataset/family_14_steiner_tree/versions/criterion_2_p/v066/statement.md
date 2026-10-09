# Problem B — Telemetry Server Provisioning

Time limit: 2 s   Memory limit: 256 MB

## Description

The annual IT upgrade for a regional healthcare system follows a strict three-stage procedure.

**Stage 1: Needs Assessment.** The medical board evaluates all $n$ facilities in the region (numbered 1 to $n$) and selects a subset of $t$ facilities to host specialized telemetry servers.

**Stage 2: Infrastructure Provisioning.** The engineering team must establish communication between all chosen telemetry servers. The region's underground infrastructure provides $m$ potential conduit links between facilities. To strictly prevent routing loops, the infrastructure was built such that $m = n - 1$, and there is exactly one valid sequence of conduits connecting any two facilities. Each conduit has a specific activation cost. The team must select a set of conduits to activate so that data can flow between all telemetry servers (potentially passing through intermediate facilities). They are mandated to choose the set that results in the lowest possible total activation cost.

**Stage 3: Budget Approval.** The finance department reviews the provisioning plan. Before physical hardware deployment can begin, they must receive the exact total cost of the activated conduits from Stage 2.

You are tasked with the computation required at the end of Stage 2. Given the facilities selected in Stage 1 and the conduit infrastructure, calculate the final integer value required by the finance department in Stage 3.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line contains $t$ distinct integers: the IDs of the facilities selected to host telemetry servers.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \ne v$, $1 \le w \le 1000000$), representing a potential conduit between facility $u$ and facility $v$ with an activation cost of $w$. The conduits adhere to the structural rules described in Stage 2.

## Output

Print a single integer: the minimum total activation cost required by the finance department to connect all telemetry servers.

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

In Example 1, the telemetry servers at facilities 1 and 4 are joined only through facilities 2 and 3, so all three conduits (5 + 1 + 2 = 8) are needed. In Example 2, there is one telemetry server, so no conduits are needed.
