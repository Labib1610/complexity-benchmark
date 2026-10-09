# Linear Module Placement

Time limit: 5 s
Memory limit: 256 MB

## Description
A facility needs to install $n$ modules along a single straight track containing $n$ mounting slots. The slots are numbered consecutively from 1 to $n$. Each slot must hold exactly one module.

The modules communicate through $m$ dedicated two-way data links. The network of links guarantees that any module can send data to any other module, possibly through intermediaries. It is also guaranteed that the total number of links $m$ is strictly less than $n$. Furthermore, the network always satisfies the property that the modules can be partitioned into two groups such that no link connects two modules within the same group, and no module is directly linked to more than $n-1$ other modules.

When a link connects a module placed at slot $i$ and a module placed at slot $j$, the physical distance the link spans is $|i - j|$. You have a total budget $B$ for the sum of the distances of all $m$ links. Multiple links can overlap along the track without penalty.

Your task is to find an assignment of the $n$ modules to the $n$ slots such that the sum of the physical distances of all links is less than or equal to $B$, or determine if it is impossible.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a data link between module $u$ and module $v$.

## Output
If there is a valid placement, print `YES` on the first line. On the second line, print $n$ integers representing the slot numbers (from 1 to $n$) assigned to modules 1, 2, ..., $n$ respectively.
If no such placement exists, print `NO`.

## Example 1
### Input
```text
4 3 4
1 2
2 3
2 4
```
### Output
```text
YES
1 2 3 4
```

## Example 2
### Input
```text
4 3 3
1 2
2 3
2 4
```
### Output
```text
NO
```
