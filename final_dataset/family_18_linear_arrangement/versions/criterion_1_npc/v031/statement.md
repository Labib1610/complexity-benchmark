# Problem A — Exhibition Ribbon Routing

Time limit: 5 s   Memory limit: 256 MB

## Description
A new historical exhibition is being curated, and its artifacts must be arranged along a single straight
gallery hallway. The hallway is divided into a fixed number of consecutive display cases, exactly one
artifact per case, and every artifact ends up in some case; there are precisely as many cases as artifacts, so the
arrangement is a one-to-one placement of artifacts into case positions numbered along the hallway.

The artifacts share thematic links indicated by point-to-point decorative ribbons. Whenever two artifacts share a thematic link, a
ribbon is run between their cases along the hallway's floorboard. Because the floorboard runs the length of the
hallway, the physical length of a ribbon is determined solely by how many case positions separate the two
artifacts it connects — adjacent cases cost one unit of ribbon, cases two apart cost two units, and so on.
The specific mounting hardware, attachment types, and viewing directions are immaterial to this calculation;
only the separation in cases matters.

The design committee has fixed a **total** ribbon budget for the exhibition: summed over every required thematic link,
the combined ribbon length must not exceed the given budget. There is no per-ribbon limit and no limit
on how many ribbons share the floorboard — the only constraint that binds is the grand total.

Decide whether the artifacts can be placed one-per-case so that the total ribbon length over all required
links stays within the budget, and if so output a placement; otherwise report that no placement
fits the budget. (A placement that is excellent for some links may overshoot the total because of
others, so local good choices do not guarantee a feasible total.)

## Input
First line: three integers n, m, B. Each of the next m lines: two integers u v — a thematic link between two artifacts.

## Output
Print `YES` then a line with n integers — the case position (1..n, a permutation) of artifact 1,2,...,n —
such that the total stretch is <= B. Otherwise print `NO`.

## Example

**Input:**
```
4 4 6
1 2
2 3
3 4
4 1
```

**Output:**
```
YES
1 2 4 3
```
