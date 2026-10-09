# Thermal Conduit Assignment

Time limit: 5 s   Memory limit: 256 MB

## Description
A refinery operates a set of reaction chambers. Each chamber is manufactured with exactly three heat-exchange conduits. Every conduit directly links exactly two chambers.

The refinery relies on three cooling fluids, identified as 1, 2, and 3. Each conduit must be filled with exactly one of these fluids. Because a conduit connects two chambers, the fluid inside it cools both of those chambers.

To prevent thermal runaway, every chamber must be cooled by all three fluids simultaneously. Consequently, the three conduits attached to any individual chamber must each contain a different fluid.

Based on the fixed layout of the chambers and conduits, determine if a safe fluid assignment is possible. If it is, output the assignment.

## Input
The first line contains two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of chambers and the number of conduits respectively.
Each of the following **m** lines contains two integers u and v (1 ≤ u < v ≤ n), indicating a conduit connecting chamber u and chamber v.

## Output
If a valid fluid assignment exists, print `YES` on the first line. On the second line, print **m** integers from the set {1, 2, 3} separated by spaces, representing the fluid assigned to each conduit in the order they were given in the input. If no such assignment is possible, print `NO`.

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
