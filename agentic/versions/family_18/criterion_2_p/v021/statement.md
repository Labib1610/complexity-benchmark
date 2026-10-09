# Problem B — Linear Facility Arrangement

Time limit: 5 s
Memory limit: 256 MB

## Description
A manufacturing company is planning to build $n$ new facilities along a single straight highway. There are $n$ available land lots on this highway, numbered sequentially from $1$ to $n$. Each facility must be built on exactly one lot, and each lot can accommodate exactly one facility.

The manufacturing process requires transferring materials between certain pairs of facilities using dedicated straight pipes. The blueprint specifies $m$ such pipes. To ensure efficiency and avoid redundant infrastructure, the blueprint is designed so that for any pair of facilities, there is exactly one route of connected pipes between them that does not pass through any facility more than once.

The cost of laying a pipe depends on the distance between the two lots it connects. If a pipe connects a facility built on lot $x$ and a facility built on lot $y$, the length of this pipe is exactly $|x - y|$ units. 

The company has a strict total allowance of $B$ units of pipe length for the entire project. There is no individual limit on the length of any single pipe, nor is there a limit on how many pipes can run parallel along the same segment of the highway. 

Your task is to determine whether it is possible to assign the $n$ facilities to the $n$ lots such that the sum of the lengths of all $m$ pipes is at most $B$. If it is possible, you must provide a valid assignment.

## Input
The first line contains three integers $n$, $m$, and $B$ — the number of facilities, the number of pipes, and the total pipe length allowance. 
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that a pipe must be built between facility $u$ and facility $v$. (Facilities are numbered from $1$ to $n$).

## Output
If the budget cannot be met, print `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers separated by spaces. The $i$-th integer should represent the lot number ($1$ to $n$) where facility $i$ is built. If there are multiple valid assignments, any of them will be accepted.

## Example 1

**Input:**
```
4 3 4
1 2
2 3
2 4
```

**Output:**
```
YES
1 2 3 4
```

## Example 2

**Input:**
```
4 3 3
1 2
2 3
2 4
```

**Output:**
```
NO
```
