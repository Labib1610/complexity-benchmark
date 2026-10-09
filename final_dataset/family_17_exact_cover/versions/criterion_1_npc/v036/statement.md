# Problem A — Curing Fixture Allocation

Time limit: 5 s
Memory limit: 256 MB

## Description
A manufacturing facility is processing a batch of components, which are sequentially numbered starting from 1. The total number of components in the batch is exactly $3q$.

The components must be placed into curing fixtures that hold exactly three items at a time. Due to physical clearances, only certain specific combinations of three components can be safely mounted together in a fixture. A catalog of these physically compatible combinations is provided.

The goal is to process the entire batch of components. Every component must be mounted in a fixture exactly once. Omitting a component leaves the batch incomplete, and processing a component more than once destroys it. You must determine if it is possible to choose a collection of compatible combinations from the catalog to meet these requirements.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The total number of components is $3q$.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing one compatible combination of three components.

## Output
If a valid choice of combinations exists, print `YES`. Then, output $q$ lines, each containing the three components of one chosen combination.
If no such choice is possible, print `NO`.

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
