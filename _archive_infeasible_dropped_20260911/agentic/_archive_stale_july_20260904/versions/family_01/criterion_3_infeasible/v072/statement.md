# Volatile Triad Identification

Time limit: 2 s   Memory limit: 256 MB

A pharmaceutical laboratory is analyzing a set of $n$ experimental compounds, indexed from $1$ to $n$. Extensive safety testing has yielded a list of known reactive pairs—combinations of two compounds that will violently react if placed in the same solution. 

The lab is searching for a specific type of mixture called a volatile triad: a combination of exactly three distinct compounds where every possible pair among the three is known to react. Identifying this mixture is critical for synthesizing a new catalyst. 

It has been mathematically verified that the current database of reactions contains at least one such volatile triad. Your task is to process the reaction data and identify one.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of compounds that react with each other.
It is guaranteed that at least one volatile triad exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are reactive. Output the lexicographically smallest such triple (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
