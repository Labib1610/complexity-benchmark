# Problem A — Pressure State Stabilization in Fluid Networks

Time limit: 5 s   Memory limit: 256 MB

## Description
An industrial cooling system is built from a collection of fluid transfer pipes and intersection valves. Each pipe connects exactly two valves. The system's design guarantees that every valve serves as an endpoint for exactly three pipes.

The fluid in each pipe must be maintained at one of three distinct pressure states, designated as 1, 2, and 3. The valves are highly sensitive to pressure differentials. If two or more pipes meeting at the same valve operate at the same pressure state, the valve will rupture. Thus, a stable operating state requires that the pipes meeting at any given valve be assigned entirely distinct pressure states. Because there are exactly three pressure states available and exactly three pipes meeting at each valve, this means every valve must see exactly one pipe of each pressure state. 

Your task is to assign a pressure state to every pipe in the system such that no valve ruptures. If no such assignment can be found across the entire network, you must determine that it is impossible.

## Input
The first line contains two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of valves and the number of pipes, respectively.
Each of the next **m** lines contains two integers u and v (1 ≤ u < v ≤ n): a pipe connecting valve u and valve v.

## Output
If a stable operating state is possible, print `YES` on the first line. On the second line, print **m** integers from the set {1, 2, 3} — the pressure state of pipe i in input order. Otherwise, print `NO`.

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
