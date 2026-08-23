# Synthetic Cell Compartmentalization

Time limit: 2 s   Memory limit: 256 MB

A synthetic biology lab is designing a cell with $n$ distinct engineered proteins. The cell has exactly two isolated environments for these proteins: the cytosol and the nucleus. Certain pairs of proteins exhibit strong binding affinity and will form inactive aggregates if they are placed in the same environment. Therefore, any two proteins with a binding affinity must be assigned to different environments.

Currently, the cell design is unviable because a valid assignment is impossible. Analysis shows that the failure is caused by a "tertiary aggregation knot". A knot is formed when a pair of binding proteins both exhibit an affinity for the exact same third protein. Because all three proteins in this group bind to one another, distributing them across just two environments inevitably forces at least two of them into the same environment, causing aggregation.

Your task is to identify the three proteins that constitute a tertiary aggregation knot. If multiple such triplets exist, you must identify the one with the minimum sequence trace. For a knot consisting of protein IDs $a, b,$ and $c$ (ordered such that $a < b < c$), the sequence trace is calculated as $a \cdot 10^8 + b \cdot 10^4 + c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of engineered proteins and the number of known binding affinities. The proteins are identified by integers from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that protein $u$ and protein $v$ have a binding affinity. 

The input data is guaranteed to contain at least one tertiary aggregation knot.

## Output
Output a single line containing three space-separated integers $a$, $b$, and $c$ ($a < b < c$) representing the IDs of the three proteins forming the knot. You must output the triplet that produces the minimum sequence trace as defined above.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```