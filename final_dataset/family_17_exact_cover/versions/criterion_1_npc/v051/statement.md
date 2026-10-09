# Centrifuge Balancing

Time limit: 5 s   Memory limit: 256 MB

## Description
A geology lab must process soil samples collected from exactly $3q$ distinct extraction sites. The sites are numbered sequentially from $1$ to $3q$.

The samples are processed in a high-speed centrifuge that holds exactly three samples per run. Due to extreme variations in soil density, loading an arbitrary combination of three samples will cause unbalanced rotation and damage the centrifuge. Following a mass analysis, the lab has compiled a list of $t$ specific triplets of sites that are perfectly balanced and safe to process together. 

The lab must adhere to two strict processing rules:
1. Each extraction site yielded only enough material for a single centrifuge run. Therefore, a site cannot be included in more than one run.
2. The analysis must be complete. Every single extraction site must be processed.

You must determine whether it is possible to choose a selection of balanced centrifuge runs such that all $3q$ sites are processed without violating the rules. If such a selection exists, you must also provide it.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
Each of the next $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the three sites that make up one safe centrifuge run.

## Output
If a valid selection exists, print `YES`, followed by $q$ lines each containing the three sites of a chosen run.
Otherwise, print `NO`.

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
