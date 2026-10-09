# Problem A — Harmonic Resonance Clusters

Time limit: 5 s   Memory limit: 256 MB

## Description
The expedition has recovered a cache of distinct harmonic crystals, uniquely numbered from 1 up to $3q$. There is exactly one crystal of each number in the inventory.

To restore power to the primary relay, the engineering team must construct exactly $q$ independent resonance generators. A generator is constructed by placing a specific combination of three crystals into a confinement matrix. Once placed, those three crystals are permanently fused and cannot be used for any other generator.

The expedition's database contains $t$ verified schematics. Each schematic specifies a rigid combination of three distinct crystals that are known to safely resonate together. Attempting to use any unverified combination, or a combination with fewer or more than three crystals, will result in a matrix collapse.

Your task is to determine whether it is possible to construct the required $q$ generators using the available verified schematics. 

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), representing the number of generators to build and the number of verified schematics, respectively.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), detailing the crystal numbers required for that schematic.

## Output
If the required generators can be built, print `YES` on the first line. Then, output $q$ lines, each containing the three crystal numbers of a schematic used in the plan.
If it is not possible, print `NO`.

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
