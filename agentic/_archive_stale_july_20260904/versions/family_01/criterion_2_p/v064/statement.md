# Hazardous Cargo Allocation

**Time limit:** 1 s  
**Memory limit:** 256 MB  

A logistics company must load $n$ cargo shipping containers onto exactly two transport vessels, designated Vessel 1 and Vessel 2. The manifest lists $m$ pairs of containers that hold mutually reactive hazardous materials. Safety regulations dictate that reactive containers must never be loaded onto the same vessel. 

You must assign each container to a vessel such that all safety regulations are followed. If it is impossible to safely transport all containers on just two vessels, you must report this failure. To standardize loading manifests, if multiple safe assignments are possible, you must select the one where the resulting sequence of vessel assignments ($f_1 \dots f_n$, where $f_i \in \{1, 2\}$) is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a pair of reactive containers.

## Output
If no safe assignment exists, print a single line `NO`.
Otherwise print `YES`, then a second line with $n$ integers $f_1 \dots f_n$ (each either 1 or 2), representing the lexicographically smallest valid assignment.

## Example 1
**Input:**
```
4 4
1 2
2 3
3 4
1 4
```
**Output:**
```
YES
1 2 1 2
```

## Example 2
**Input:**
```
3 3
1 2
1 3
2 3
```
**Output:**
```
NO
```
