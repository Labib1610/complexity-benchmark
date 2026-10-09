# Problem B — Isotope Containment

Time limit: 1 s
Memory limit: 256 MB

A research station must store $n$ unstable isotopes, numbered 1 through $n$. The station has two distinct magnetic containment fields, labeled Field 1 and Field 2. Every isotope must be placed into exactly one of these two fields.

Certain pairs of isotopes will resonate dangerously if they are exposed to the same magnetic field. You are given a list of $m$ such resonating pairs. For safety, no two isotopes that resonate with each other can be assigned to the same field.

The station has exactly 2000 storage racks, each capable of holding exactly 100 isotopes. The number of isotopes $n$ to be stored is at least one, and cannot exceed the total physical capacity of all these racks combined. The number of known resonance pairs $m$ can be zero, and its maximum possible value is equal to that same total capacity of all racks.

Your task is to determine if it is possible to safely assign all $n$ isotopes to the two containment fields. If multiple safe assignments exist, the automated sorting system requires the lexicographically smallest assignment. (An assignment sequence is lexicographically smaller than another if, at the first isotope where their field assignments differ, it assigns the isotope to Field 1 instead of Field 2).

## Input
The first line of input contains two integers $n$ and $m$.
Each of the following $m$ lines contains two integers $u$ and $v$, representing a pair of isotopes that resonate with each other.

## Output
If it is impossible to safely assign all isotopes to the two fields, print a single line containing `NO`.
If a safe assignment is possible, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each in {1, 2}) representing the field assignment for each isotope. This sequence must be the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
