# Synchronous Module Activation

Time limit: 2 s   Memory limit: 256 MB

## Description
A critical system consists of $q$ primary modules (assigned sequential identifiers from $1$ to $q$) and $q$ secondary modules (assigned sequential identifiers from $q+1$ to $2q$).

A full system diagnostic requires every single module to be activated simultaneously. However, modules can only be activated in linked pairs consisting of exactly one primary module and exactly one secondary module. 

You are given a catalog of $t$ tested links. Each link indicates a specific primary module and a specific secondary module that can safely operate together. To ensure signal integrity, the hardware design guarantees that every tested link in the catalog adheres to two physical invariants:
1. The identifier of the secondary module is strictly greater than the identifier of the primary module.
2. The sum of the two identifiers in any given link never exceeds $3q$.

The catalog may contain many overlapping possibilities, but a valid diagnostic configuration must select a subset of these links such that every primary module and every secondary module is part of exactly one active link. No module may be left unlinked, and no module may be shared between multiple active links. 

Determine whether a complete, one-to-one linkage of all $2q$ modules can be formed using only the tested links. If so, provide one such configuration; otherwise, report that a full diagnostic is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of primary modules and the number of tested links.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a tested link between primary module $a$ and secondary module $b$.

## Output
If a valid diagnostic configuration is possible, print `YES` on the first line, followed by $q$ lines each containing the two integers of a selected link. If it is impossible, print `NO`.

## Example
### Input
```
3 4
1 4
2 5
2 6
3 5
```
### Output
```
YES
1 4
2 6
3 5
```
