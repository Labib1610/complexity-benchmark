# Problem A — Orbital Tether Assembly

Time limit: 5 s
Memory limit: 256 MB

## Description
A new orbital station is being constructed by linking several specialized habitat modules in a single straight line. The assembly truss provides a sequence of docking bays. The first parameter of the construction manifest establishes the fleet size. This single value dictates three things: the total count of arriving modules, the number of available docking bays, and the highest module identifier (with the numbering starting at 1). 

Each module must be locked into exactly one bay, and no bay may remain empty. The bays are numbered sequentially starting from 1 up to the fleet size.

The station's design requires direct atmospheric transfer tubes between specific pairs of modules. Because the modules are arranged in a straight line, the physical length of a tube connecting two modules is determined solely by the distance between their assigned bays. Specifically, if two modules are placed in adjacent bays, the tube length is 1 unit. If they are separated by one intervening bay, the tube length is 2 units, and so on. Multiple tubes can run parallel to each other along the truss without interfering, but their lengths all contribute to the aggregate total.

The total amount of tube material available on the supply ship is strictly limited. This physical inventory is provided as a budget. Determine if there is a valid bay assignment for all modules such that the combined length of all necessary tubes does not exceed the available material. If it is possible, provide the exact bay assignment for each module; otherwise, declare the assembly impossible.

## Input
The first line of the manifest contains three integers: the fleet size, the number of tube blueprints, and the total tube material inventory.
Following this are a number of lines equal to the number of tube blueprints. Each line contains two integers representing the identifiers of a pair of modules that must be connected by a tube. 

## Output
If the modules can be assigned to the bays without exceeding the tube material inventory, output `YES` on the first line. On the second line, output a sequence of integers separated by spaces, where the first integer is the bay number assigned to module 1, the second integer is the bay number assigned to module 2, and so forth, up to the last module. The sequence must contain every bay number exactly once.
If no such assignment is possible, output `NO`.

## Example 1
### Input
```
4 3 4
1 2
1 3
1 4
```
### Output
```
YES
2 1 3 4
```

## Example 2
### Input
```
4 3 3
1 2
1 3
1 4
```
### Output
```
NO
```
