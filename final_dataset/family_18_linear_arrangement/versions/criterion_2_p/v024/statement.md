# Deep-Sea Observatory Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description
A deep-sea observatory requires $n$ sensor modules to be deployed along a single vertical tether. The tether has $n$ attachment points, spaced equally and numbered 1 to $n$ from top to bottom. Each module must be assigned to exactly one distinct attachment point.

The modules are wired together for power distribution. The wiring forms a strict hierarchy: one main module draws power from the surface, and every other module receives power from exactly one upstream module. This ensures all modules are powered through a single connected, loop-free system.

A dedicated power cable is required for each connection between two modules. The length of cable needed to connect a module at attachment point $x$ and a module at attachment point $y$ is exactly $|x - y|$ units. 

The deployment vessel has a strict limit on the total amount of cabling it can use. The sum of the lengths of all individual power cables must not exceed the maximum allowed length $B$.

Determine if there is an assignment of modules to attachment points that keeps the total cable length within the limit.

## Input
The first line contains three integers $n$, $m$, and $B$, representing the number of modules, the number of wiring connections, and the total cable length limit.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a wiring connection between module $u$ and module $v$. The connections form the strict hierarchy described above (thus $m = n - 1$).

## Output
If the modules can be assigned to the attachment points such that the total cable length is at most $B$, print `YES` on the first line. On the second line, print $n$ integers, where the $i$-th integer is the attachment point (from 1 to $n$) assigned to module $i$. If there are multiple valid assignments, any one is acceptable.
If no such assignment exists, print `NO`.

## Example

**Input:**
```text
5 4 6
1 2
1 3
3 4
3 5
```

**Output:**
```text
YES
3 2 4 1 5
```
