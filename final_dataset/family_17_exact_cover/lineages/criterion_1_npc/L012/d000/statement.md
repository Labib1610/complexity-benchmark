# Horological Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description
A boutique watchmaker is assembling complication modules from a limited inventory of distinct micro-gears. The inventory contains exactly 3q micro-gears, each identified by a unique serial number from 1 to 3q.

To ensure precise timekeeping, a complication module cannot be built from arbitrary parts. It must be constructed using a tested schematic. Each schematic specifies a working combination of three particular micro-gears that mesh perfectly. The watchmaker has a catalog of t such schematics. A single micro-gear might be listed in several different schematics, but a module can only be built if its exact combination of three gears matches a schematic from the catalog.

The watchmaker's goal is to process the entire inventory without any waste or shortage. This means every single micro-gear in the inventory must be incorporated into a module, and no micro-gear can be used more than once. Consequently, creating q modules will exhaust the inventory perfectly.

Determine whether it is possible to select a collection of schematics that will utilize every micro-gear exactly once. If a valid production run is possible, output the required schematics.

## Input
The first line contains two integers q and t (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
The following t lines each contain three integers a, b, and c (1 ≤ a < b < c ≤ 3q), detailing one tested schematic of three micro-gears.

## Output
If the inventory can be fully utilized under these conditions, print `YES` on the first line. Then, print q lines, each containing the three micro-gears for one of the chosen schematics.
If it is impossible to use the inventory completely following the constraints, print `NO`.

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
