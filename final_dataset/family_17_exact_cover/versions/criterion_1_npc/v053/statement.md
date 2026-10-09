# Problem A — Harmonic Core Initialization

Time limit: 5 s   Memory limit: 256 MB

## Description
The starship's propulsion system requires a perfectly balanced synchronization of its harmonic power modules. There are exactly $3q$ unique modules on board, forming a contiguous sequence numbered 1 through $3q$. 

To generate thrust, these modules must be grouped into reactor cores. A reactor core operates safely only when loaded with exactly three modules that form a resonant chord. The engineering team has compiled a comprehensive catalog of $t$ verified stable configurations. Because harmonic resonance naturally follows a monotonic frequency increase, every configuration in the catalog is presented as a strictly ascending triplet of module IDs ($a < b < c$). 

With up to 20,000 configurations available for a relatively small sequence of modules, the catalog provides a massive array of overlapping options. Your objective is to filter this catalog to select exactly $q$ configurations that perfectly partition the entire set of $3q$ modules. The resonant field requires full participation—leaving even one module uninstalled will cause a systemic failure, and each physical module can only be installed in a single core. 

Determine if it is possible to select a combination of the given configurations that perfectly distributes all $3q$ modules. If it is possible, output a valid selection.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The total number of modules to be installed is $3q$.
Each of the subsequent $t$ lines provides three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing a verified stable configuration of three modules in ascending order.

## Output
If a valid assignment exists, print `YES` on the first line. Then, print $q$ lines, each containing the three modules of a selected configuration.
If no such assignment is possible, print `NO`.

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
