# Problem A — Harmonic Core Initialization

Time limit: 5 s   Memory limit: 256 MB

## Description
The starship's propulsion system requires a complete synchronization of its harmonic power modules. There are exactly $3q$ unique modules on board, numbered sequentially from 1 to $3q$. 

To generate thrust, modules must be installed into reactor cores. A reactor core is only stable if it is loaded with exactly three modules whose frequencies create a resonant chord. The engineering team has provided a catalog of tested, stable configurations. Each configuration in the catalog specifies three distinct modules that can safely operate together in a single core. 

Your objective is to activate a set of reactor cores such that every single module on the ship is utilized. The resonant field requires full participation—leaving even one module uninstalled will cause a systemic failure. Furthermore, each module is a unique physical object and can only be installed in a single core. Therefore, the chosen configurations must collectively incorporate each of the $3q$ modules exactly one time.

Determine if it is possible to select a combination of the given configurations that perfectly distributes all $3q$ modules into cores. If it is possible, output a valid selection.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The total number of modules to be installed is $3q$.
Each of the subsequent $t$ lines provides three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing a verified stable configuration of three modules.

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
