# Liquid Catalyst Transfer

Time limit: 2 s   Memory limit: 256 MB

## Description
A chemical processing facility relies on a network of vats connected by one-way pipes. You need to configure the system for a specific production run involving a set number of vats and pipes.

For this run, exactly `d` units of a volatile liquid catalyst must be moved from the primary extraction vat to the final synthesis vat. 

Each pipe allows a non-negative whole number of units of fluid to flow in a single direction from one specific vat to another. Due to pressure constraints, each pipe has a strict upper limit on the number of units of catalyst it can safely transport. 

The vats themselves (aside from the extraction and synthesis vats) have no storage capacity for this catalyst. They merely redirect the fluid. Consequently, for every intermediate vat, the total units of catalyst flowing into it must perfectly match the total units flowing out. 

For the extraction vat, the total units sent out minus any units flowing back into it must equal exactly the target volume `d`. Similarly, for the synthesis vat, the total units received minus any units sent out must equal exactly `d`. The physical layout, pipe length, and fluid travel time do not matter—only the pipe limits, the strict in-out balance at intermediate vats, and the target volume determine if a configuration is viable.

Determine if it is possible to transfer exactly the target volume of catalyst through the facility without exceeding any pipe's upper limit. If a valid configuration exists, specify the exact number of units to route through each pipe.

## Input
Line 1: Three integers `n` (the number of vats), `m` (the number of one-way pipes), and `1` (representing the single production run).
Line 2: Three integers `s` (the extraction vat's identifier), `t` (the synthesis vat's identifier), and `d` (the target volume of catalyst).
Next `m` lines: Three integers `u`, `v`, and `cap`, representing a pipe that carries fluid from vat `u` to vat `v` with an upper limit of `cap` units.

## Output
If the target volume can be successfully transferred, print `YES` on the first line. On the second line, print `m` integers indicating the units of catalyst routed through each pipe, corresponding to the exact order the pipes appear in the input. If it cannot be done, print `NO`.

## Example

**Input:**
```
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

**Output:**
```
YES
5 5 0 5 5
```
