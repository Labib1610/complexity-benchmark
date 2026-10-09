# Orbital Debris Sweeping

Time limit: 5 s
Memory limit: 256 MB

## Description
A planetary orbit contains $3q$ distinct zones of debris, numbered sequentially from $1$ to $3q$. You need to deploy a fleet of collector drones to completely clear the orbit.

Through orbital dynamics, a single drone can only collect debris from a specific set of exactly three zones during its flight. You are provided with a catalog of $t$ feasible three-zone flight paths.

A valid deployment strategy is a selection of these flight paths satisfying all of the following requirements:
1. Every debris zone from $1$ to $3q$ is visited by exactly one deployed drone. Drones cannot safely cross paths in the same zone, and no zone can be left uncleared.
2. The total number of deployed drones must be exactly $q$.
3. To satisfy the local energy conservation laws of the orbital sector, the deployment must be perfectly balanced: the grand total of all $3q$ zone identifiers across all deployed drones' flight paths must exactly equal $\frac{3q(3q+1)}{2}$.

Your task is to determine whether a valid deployment strategy exists, and if so, to output one. If the catalog of flight paths cannot satisfy all these requirements simultaneously, report that it is impossible. (Note that a large catalog of flight paths does not guarantee a valid strategy, while a very small catalog might still succeed).

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing a feasible flight path that visits zones $a$, $b$, and $c$.

## Output
If a valid deployment strategy exists, print `YES` on the first line. Then, print $q$ lines, each containing the three zone identifiers of a chosen flight path. If there are multiple valid strategies, you may output any of them.
If no such strategy exists, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
