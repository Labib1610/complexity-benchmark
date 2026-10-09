# Problem C — Shift Expansion Certificate

Time limit: 2 s   Memory limit: 256 MB

The factory operates on a two-shift schedule. Certain pairs of workers require exclusive access to the same specialized equipment, meaning they cannot be assigned to the same shift. The rostering software receives a list of these pairwise restrictions.

The current set of restrictions makes it impossible to assign all workers to just two shifts. To automatically trigger a budget request for a third shift, your module must generate a formal impossibility certificate. This certificate must consist of exactly three distinct workers where every pair among the three shares equipment, making any two-shift assignment for them invalid.

It is guaranteed that the list of restrictions contains at least one such trio of workers. Your module must output the IDs of the chosen three workers in increasing order. To ensure deterministic behavior in the automated system, if multiple valid trios exist, you must output the one that is lexicographically smallest (minimize the first worker's ID, then the second worker's ID, then the third worker's ID).

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the number of workers and the number of equipment-sharing restrictions. Workers are identified by integers from 1 to n.
Each of the following m lines contains two integers u and v, indicating that worker u and worker v share equipment.
It is guaranteed that at least one trio of mutually restricted workers exists.

## Output
Print three integers a, b, and c on a single line, representing the worker IDs of the impossibility certificate. The IDs must be printed in increasing order (a < b < c). Output the lexicographically smallest valid trio.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
