# Optimal Component Alignment

Time limit: 5 s
Memory limit: 256 MB

## Description
You must design the physical layout for a series of distinct hardware modules. There is a single straight track with a number of discrete docking bays exactly equal to the number of modules. Each module must be assigned to its own unique bay.

The modules share data via a set of dedicated physical cables. Each cable directly links two specific modules. The required length of any given cable is determined entirely by the physical distance between the bays where its two endpoints are installed. If two linked modules are placed in bay $i$ and bay $j$, the cable spanning them will have a length of $|i - j|$.

Your objective is to find a bay assignment for every module such that the combined length of all cables is no greater than a specified maximum allowance $B$. The aggregate sum of the lengths is the only metric that matters; individual cables have no length restrictions. The network of cables is structured so that data can flow between any two modules, and there are exactly enough cables to achieve this without creating any alternative routing paths.

You must determine if it is possible to assign the modules to the docking bays without exceeding the allowance $B$, and if so, provide a valid layout.

## Input
The first line contains three integers $n$, $m$, and $B$, which are the total number of hardware modules, the number of cables, and the maximum allowed combined length, respectively.

The next $m$ lines each contain two integers $u$ and $v$ ($u \neq v$). These integers represent the unique serial numbers of two modules that are linked by a cable. The serial numbers start from the smallest positive integer and go up to the total number of modules. It is guaranteed that the total number of cables is exactly one less than the total number of modules, and data can flow between any two modules either directly or through other modules.

## Output
If a valid layout exists, output `YES` on the first line. On the second line, output $n$ space-separated integers, where the $i$-th integer represents the docking bay position (starting from the smallest positive integer up to $n$) assigned to the module with serial number $i$. Every docking bay must be occupied by exactly one module.

If no such layout exists, output `NO`.

## Example

### Input
```
5 4 5
1 2
1 3
2 4
2 5
```

### Output
```
YES
4 2 5 1 3
```
