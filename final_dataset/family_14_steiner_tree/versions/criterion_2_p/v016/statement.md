# Facility Interconnection Plan

Time limit: 2 s   Memory limit: 256 MB

## Description

A large campus consists of $n$ facilities, numbered 1 through $n$. To establish a secure network, there are $m$ potential direct cable links that can be built between specific pairs of facilities. Each link has an associated installation cost. The layout of these potential links guarantees that data can travel between any two facilities via exactly one route (a sequence of links where no facility is visited more than once).

Among the $n$ facilities, exactly $t$ are designated as *critical*. You must authorize the installation of a subset of the potential cable links so that all critical facilities are able to communicate with one another. Data can be routed through non-critical facilities if necessary.

You must find the minimum possible total installation cost to achieve this.

Please note the following guaranteed properties of the network:
- The total cost of all $m$ potential links combined is at most $2 \times 10^{11}$.
- The number of critical facilities $t$ is at most $m + 1$.
- No single facility is an endpoint for more than $m$ potential links.

## Input

The first line provides three integers $n$, $m$, and $t$ (1 ≤ $t$ ≤ $n$, 1 ≤ $n$ ≤ 200,000, $m = n - 1$).
The second line lists $t$ distinct integers representing the identifiers of the critical facilities.
The following $m$ lines each contain three integers $u$, $v$, and $w$ (1 ≤ $u, v$ ≤ $n$, $u \neq v$, 1 ≤ $w$ ≤ 1,000,000), indicating a potential cable link between facility $u$ and facility $v$ with an installation cost of $w$. 

## Output

Output a single integer representing the minimum total cost required to interconnect all critical facilities.

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
