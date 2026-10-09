# Problem A — Synchronization Links

Time limit: 5 s   Memory limit: 256 MB

## Description

An industrial facility operates **n** automated workstations (numbered 1 through **n**). A specific subset of **t** primary workstations must be inspected by a diagnostic program.

To allow the diagnostic program to run, you must activate a subset of the available bidirectional data links. The facility has a set of potential links that can be activated, each requiring a known continuous energy draw. 

Once a subset of links is activated, there must exist a sequence of movements along these activated links such that the diagnostic program can start at one primary workstation and eventually visit all the other primary workstations. The program is allowed to visit any workstation (primary or otherwise) multiple times, and it can traverse any activated link multiple times.

Your task is to determine the minimum total continuous energy draw required to activate a subset of links that makes this complete inspection possible. The energy requirement for each link is continuous: you pay its activation energy exactly once when you include it in your activated subset, regardless of how many times the diagnostic program travels across it.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the primary workstations.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a potential bidirectional data link between workstation **u** and workstation **v** that requires **w** units of energy to activate.
It is guaranteed that there exists at least one subset of links that allows the diagnostic program to complete its inspection.

## Output

Print a single integer: the minimum total energy draw required to activate a valid subset of links.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, the optimal configuration includes the links (1, 4), (2, 4), and (3, 4) in the activated subset for a total energy draw of 1 + 1 + 1 = 3. Using this subset, the diagnostic program can start at workstation 1, travel to 4, then to 2, back to 4, and finally to 3, successfully visiting all primary workstations (1, 2, and 3). 

In Example 3, there is only one primary workstation. The inspection is complete without moving, so no links need to be activated, resulting in a total energy draw of 0.