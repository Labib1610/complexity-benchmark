# Problem A — Exhibit Placement for the Museum Wing

Time limit: 5 s   Memory limit: 256 MB

## Description
A new museum wing is being commissioned, and its exhibits must be installed along a single straight hallway. The hallway is divided into a fixed number of consecutive display alcoves, exactly one exhibit per alcove, and every exhibit ends up in some alcove; there are precisely as many alcoves as exhibits, so the installation is a one-to-one placement of exhibits onto alcove positions numbered along the hallway.

The exhibits share thematic elements that are highlighted by guided audio tours. Whenever two exhibits are thematically linked, the audio guide directs visitors between their alcoves. Because visitors follow the linear path of the hallway, the walking distance for a link is determined solely by how many alcove positions separate the two exhibits it connects — adjacent alcoves cost one unit of distance, alcoves two apart cost two units, and so on. The specific exhibit contents, display sizes, and direction of travel are immaterial to this calculation; only the separation in alcoves matters.

The curators have fixed a **total** walking budget for the wing: summed over every required thematic link, the combined walking distance must not exceed the given budget. There is no per-link limit and no limit on how many links cross the same section of hallway — the only constraint that binds is the grand total.

Decide whether the exhibits can be placed one-per-alcove so that the total walking distance over all required links stays within the budget, and if so output a placement; otherwise report that no placement fits the budget. (A placement that is excellent for some links may overshoot the total because of others, so local good choices do not guarantee a feasible total.)

## Input
First line: three integers n, m, B. Each of the next m lines: two integers u v — a thematic link between exhibit u and exhibit v.

## Output
Print `YES` then a line with n integers — the position (1..n, a permutation) of exhibit 1,2,...,n — such that the total walking distance is <= B. Otherwise print `NO`.

### Example

**Input**
```
4 4 6
1 2
2 3
3 4
4 1
```

**Output**
```
YES
1 2 4 3
```
