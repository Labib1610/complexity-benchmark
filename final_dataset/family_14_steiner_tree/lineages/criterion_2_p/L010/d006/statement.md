# Subsystem Activation Procurement

Time limit: 2 s   Memory limit: 256 MB

## Description

An industrial manufacturing complex features $n$ distinct workstations, numbered $1$ to $n$. These are linked by $m$ bidirectional conveyor belts. The facility's infrastructure ensures that all workstations are interlinked in a single contiguous network. To minimize maintenance costs, the total number of belts $m$ is strictly fixed at exactly $n - 1$, meaning there is exactly one unique sequence of belts between any two workstations.

A specific subset of $t$ workstations are designated as quality-control stations. 

You must select a subset of the $m$ available belts to authorize for operation. Authorizing the belt between workstation $u$ and workstation $v$ incurs a one-time energy overhead of $w$. Belts that are not authorized cannot be used.

The selected subset of authorized belts must satisfy the following connectivity mandate: every quality-control station must be capable of routing materials to every other quality-control station using only authorized belts. Materials may pass through intermediate non-quality-control workstations along the way, provided every belt along the route has been authorized.

Your objective is to determine the minimum possible total energy overhead required to authorize a valid set of belts that satisfies this mandate. (If only one quality-control station exists, no routing between stations is needed, and zero belts need to be authorized).

## Input

The first line provides three integers: $n$, $m$, and $t$. The facility's blueprint supports a maximum of two hundred thousand workstations ($1 \le n \le 200000$). The number of belts $m$ is always $n - 1$. The number of quality-control stations $t$ can range from a single station up to the entire facility ($1 \le t \le n$).

The second line contains $t$ distinct integers representing the IDs of the quality-control stations.

Following this, there are $m$ lines, each detailing a single conveyor belt with three integers: $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$). The energy overhead $w$ for authorizing any single belt is at least one and does not exceed one million units ($1 \le w \le 1000000$). 

## Output

Print a single integer: the minimum possible total energy overhead required to authorize a set of belts such that all quality-control stations are connected.

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

In Example 1, the quality-control stations are 1 and 4. To ensure station 1 can route materials to station 4, the belts between 1 and 2 (overhead 5), 2 and 3 (overhead 1), and 3 and 4 (overhead 2) must be authorized. The total overhead is 5 + 1 + 2 = 8. This is the minimum possible total overhead.
In Example 2, there is only one quality-control station (station 3). Since no routing between multiple stations is required, no belts need to be authorized. The minimum possible total overhead is 0.