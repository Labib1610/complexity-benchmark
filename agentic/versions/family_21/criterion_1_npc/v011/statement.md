# Problem A — Preventing Cross-Contamination

Time limit: 5 s   Memory limit: 256 MB

## Description
An industrial processing plant consists of a network of fluid tanks connected by bidirectional transfer lines. Some of these tanks are designated as primary injection points, each receiving a different, highly reactive chemical agent. 

During an upcoming overhaul, the plant managers must guarantee that no two reactive agents can possibly mix. To achieve this, they will install solid blind flanges on a chosen set of transfer lines. Once a flange is installed on a transfer line, no fluid can flow through it in either direction. 

The goal is to ensure that the injection points are **mutually segregated**: after the flanges are installed, there must be no remaining sequence of open transfer lines that allows fluid to travel between any two primary injection points. The other, standard tanks in the plant may fall into whichever segregated region the flanging produces—their placement is unconstrained and irrelevant to acceptance. What is measured is solely the total flanging cost, which is the sum of the installation costs for the transfer lines actually flanged.

Installing a flange requires specialized labor and parts, resulting in a specific cost for each transfer line. The plant has a strict maintenance budget. You must determine a set of transfer lines to flange such that their total cost does not exceed the budget, and their closure leaves every pair of injection points disconnected. If it is impossible to achieve this segregation without exceeding the budget, you must report so. (Isolating any single pair of injection points might be inexpensive, but the budget must cover the simultaneous segregation of all injection points from one another.)

## Input
The first line contains four integers $n$, $m$, $k$, and $B$: the number of fluid tanks, the number of transfer lines, the number of primary injection points, and the total maintenance budget. 
The second line contains $k$ distinct integers representing the identifiers of the tanks that are injection points.
The following $m$ lines each contain three integers $u$, $v$, and $w$, indicating a transfer line between tank $u$ and tank $v$ that costs $w$ to flange. Tanks are numbered from $1$ to $n$.

## Output
If a valid set of transfer lines can be flanged within the budget, output `YES` on the first line. On the second line, output an integer $c$ representing the number of transfer lines chosen. Then, output $c$ lines, each containing two integers $u$ and $v$, specifying the endpoints of a flanged line. If no such set exists, output `NO`.

## Example

### Input
```text
4 3 3 10
1 2 3
1 4 2
2 4 3
3 4 4
```

### Output
```text
YES
2
1 4
2 4
```
