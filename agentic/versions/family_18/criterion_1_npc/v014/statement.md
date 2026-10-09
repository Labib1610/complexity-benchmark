# Problem A — Backbone Trenching for the Control Vault

Time limit: 5 s   Memory limit: 256 MB

## Description
The main control vault requires installing a set of processing modules. These modules are to be mounted on a single straight DIN rail. The rail features a sequence of evenly spaced slots, numbered consecutively starting from 1. There are exactly as many slots as there are modules in the inventory, and each slot acts as a receptacle for exactly one module.

Modules must communicate with each other. The blueprint specifies pairs of modules that require a direct data link. For each such link, a physical wire is routed parallel to the rail. The amount of wire consumed by a single link is determined entirely by the separation of the slots holding the two communicating modules. If they are placed in contiguous slots, they consume exactly one unit of wire; if there is one slot between them, they consume two units, and in general, the wire consumed is the absolute difference between their assigned slot numbers. 

The installation team has been issued a single, pre-cut spool of wire for the entire project. Every required link must be cut from this single spool. The installation is considered feasible only if the spool contains sufficient wire to complete all data links without running out. The order in which the modules are placed on the rail dictates the total wire consumption.

Determine if there is a placement of modules into the slots such that the spool is not exhausted. If such a placement exists, provide it.

## Input
The first line contains three integers representing the module inventory size ($n$), the count of required data links ($m$), and the total units of wire on the spool ($B$).
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that the blueprint requires a link between module $u$ and module $v$. Modules are identified by integers from $1$ to $n$.

## Output
If a valid placement exists, print `YES` on the first line. On the second line, print $n$ integers representing the slot numbers (from $1$ to $n$) assigned to module 1, module 2, ..., module $n$ respectively. This sequence must be a permutation of the integers from $1$ to $n$.
If no such placement is possible, print `NO`.

## Example

### Input
```text
4 3 4
1 2
1 3
1 4
```

### Output
```text
YES
2 1 3 4
```
