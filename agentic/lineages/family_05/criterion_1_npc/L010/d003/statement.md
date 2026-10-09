# Problem A — Protocol Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description

You are overseeing a communications network that requires establishing a full array of $k$ operational protocols. Each protocol is defined by three independent parameters: a frequency band, a spatial sector, and a temporal phase. Each parameter is identified by an integer from $1$ to $k$.

You are provided with a raw log of certified protocols. Each entry in the log is a triplet $(x, y, z)$, which specifies that frequency band $x$, spatial sector $y$, and temporal phase $z$ can be combined into a stable protocol. 

Your objective is to authorize exactly $k$ protocols from the log to form a deployment. To prevent system interference, the chosen protocols must be entirely orthogonal across all dimensions. Specifically, within the $k$ authorized protocols, no two may share the same frequency band, no two may share the same spatial sector, and no two may share the same temporal phase.

Determine whether such a deployment is possible. If it is, output the protocols that form the deployment.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 22$, $0 \le t \le k^3$), denoting the parameter bound (which is also the required number of protocols) and the total number of certified protocols in the log.
The next $t$ lines each contain three integers $x$, $y$, and $z$ ($1 \le x, y, z \le k$), detailing a certified protocol. No protocol appears more than once in the log.

## Output

If a valid deployment of $k$ protocols is possible, print `YES` on the first line. Then, print $k$ lines, each containing the three integers $x$ $y$ $z$ of an authorized protocol. The chosen protocols can be printed in any order. Any valid deployment will be accepted.

If no such deployment is possible, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both certified protocols utilize spatial sector 1. Consequently, it is impossible to authorize 2 protocols without them interfering in the spatial sector dimension, meaning a valid deployment cannot be formed.