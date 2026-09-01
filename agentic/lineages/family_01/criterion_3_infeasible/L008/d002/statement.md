# Problem C — Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

Management insists on dividing the workforce into exactly two non-overlapping shifts. However, the HR department knows this plan is doomed. You must provide undeniable proof of this failure.

HR has a collection of incident files, where each file lists two specific workers who cannot be placed on the same shift. 

It is a known fact that the workforce contains at least one set of three workers where every two-person combination within that set is documented in an incident file. The existence of such a set mathematically guarantees that two shifts are inadequate. Your task is to identify and report one such set to HR.

## Input
The first line of the log provides the workforce size n and the total incident count m. The workforce size n is bounded below by the required set size of 3 and bounded above by the facility capacity of 2000. The incident count m is at least 3, and is capped by either the theoretical maximum of n·(n−1)/2 distinct combinations, or the archival capacity of 2·10⁵, whichever is smaller. Workers are identified by integers from 1 to n.

Each of the next m lines contains two integers u and v (1 ≤ u, v ≤ n, u ≠ v), identifying the two workers involved in a single incident.

It is guaranteed that at least one valid set of three workers exists.

## Output
Output three space-separated integers a, b, and c representing the IDs of the three workers in the set. They must be printed such that a < b < c.

To ensure a unique valid response when multiple such sets exist, you must select the set that minimizes the value of a. If there is a tie, minimize the value of b among the tied sets, and if a tie still persists, minimize c.

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