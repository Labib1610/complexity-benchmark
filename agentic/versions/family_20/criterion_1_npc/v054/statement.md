# Problem A — Thermal Network Stabilization

Time limit: 5 s   Memory limit: 256 MB

## Description
A specialized thermal regulation array consists of junctions and connecting conduits. Each conduit links exactly two junctions. The architecture of the array strictly dictates that every junction serves as an endpoint for exactly three conduits.

The coolant flowing through each conduit must be configured to one of three distinct thermal states, labeled 1, 2, and 3. Junctions are highly vulnerable to thermal interference. If two or more conduits meeting at the same junction carry coolant in the same thermal state, the junction will overheat and fail. Therefore, a stable configuration requires that all conduits meeting at any specific junction be set to completely different thermal states. Since there are exactly three available thermal states and exactly three conduits meeting at each junction, a stable configuration means every junction experiences exactly one conduit of each thermal state.

The smallest valid prototype array contains exactly a single pair of junctions. The maximum scale of any deployed array is constrained by the facility's inventory, which holds a strict maximum of 3000 conduits. Because every junction requires exactly three conduit endpoints and each conduit provides exactly two, the total number of junctions is strictly an even number, and the total number of conduits is mathematically fixed by the junction count.

Your objective is to determine a thermal state assignment for every conduit in the array such that no junction fails. If no such configuration is possible for the given architecture, you must report that it is impossible.

## Input
The first line contains two integers **n** and **m**, representing the number of junctions and the number of conduits, respectively. The values of **n** and **m** are guaranteed to conform to the physical limits and topological requirements described above.

Each of the subsequent **m** lines provides two integers *u* and *v*, identifying the two distinct junctions connected by a conduit. Junctions are numbered sequentially starting from 1 up to **n**, and the first identifier *u* is always strictly less than the second identifier *v*.

## Output
If a stable configuration is achievable, print `YES` on the first line. On the second line, print **m** integers from the set {1, 2, 3} — the thermal state of the *i*-th conduit in the exact order they were provided in the input. Otherwise, print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
