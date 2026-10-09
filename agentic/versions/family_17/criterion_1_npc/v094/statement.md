# Problem A — Harmonic Core Initialization

Time limit: 5 s
Memory limit: 256 MB

## Description
The starship's propulsion system requires a perfectly balanced synchronization of its harmonic power modules. The vessel's architecture dictates that the number of required cores, $q$, is a minimum of one and reaches a maximum capacity of two hundred. The total number of unique modules on board is exactly three times $q$, numbered sequentially starting from 1 up to $3q$. 

To generate thrust, these modules must be grouped into reactor cores. A reactor core operates safely only when loaded with exactly three modules that form a resonant chord. The engineering team has compiled a catalog of $t$ verified stable configurations. Depending on the system's state, this catalog might be entirely empty, or it could hold a maximum limit of twenty thousand entries. Because harmonic resonance naturally follows a monotonic frequency increase, every configuration in the catalog is presented as a strictly ascending triplet of module identifiers. 

Your objective is to filter this catalog to select exactly $q$ configurations that perfectly partition the entire set of modules on board. The resonant field requires full participation—leaving even one module uninstalled will cause a systemic failure, and each physical module can only be installed in a single core. 

Determine if it is possible to select a combination of the given configurations that perfectly distributes all $3q$ modules. If it is possible, output a valid selection.

## Input
The first line contains two integers $q$ and $t$. The values of $q$ and $t$ correspond to the core capacity and catalog limits described above.
Each of the subsequent $t$ lines provides three integers $a$, $b$, and $c$. These represent a verified stable configuration, following the ascending order and module identifier limits established by the onboard hardware.

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
