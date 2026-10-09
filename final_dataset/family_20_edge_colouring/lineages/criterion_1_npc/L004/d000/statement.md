# Problem A — Structural Alloy Assignment

Time limit: 5 s   Memory limit: 256 MB

## Description
An architectural firm is designing a framework consisting of steel joints connected by load-bearing struts. The framework is configured such that every joint connects exactly three struts. 

To manage thermal expansion, each strut must be fabricated using one of three distinct alloys, designated 1, 2, and 3. To ensure symmetrical stress distribution at the connections, the three struts meeting at any single joint must each be made of a different alloy. 

Determine if it is possible to assign an alloy to each strut to satisfy this local symmetry requirement across the entire framework.

## Input
The first line contains two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of joints and struts, respectively.
Each of the following **m** lines contains two integers u and v (1 ≤ u < v ≤ n), indicating a strut connecting joint u and joint v.

## Output
If a valid alloy assignment exists, print `YES`, then a line with **m** integers in {1, 2, 3} — the alloy of strut i in input order (struts sharing a joint must have different alloys). Otherwise print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
