# Stable Ternary Mixture

Time limit: 2 s
Memory limit: 256 MB

A chemical laboratory is analyzing a set of $n$ experimental compounds. Through pairwise testing, they have identified $m$ specific combinations of two compounds that are completely inert when mixed together.

The laboratory needs to formulate a new solution containing exactly three distinct compounds. A mixture of three compounds will only remain stable if every possible pair of compounds within the mixture is inert. If even one pair within the three is not on the list of inert combinations, the entire mixture will degrade.

You are provided with the records of the $m$ inert pairs. It is guaranteed that at least one stable mixture of three compounds can be formulated. Your task is to select the three compounds for the solution.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of compounds and the number of inert pairs, respectively. The compounds are assigned integer identifiers from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that compound $u$ and compound $v$ are inert when mixed.

It is guaranteed that at least one stable mixture of three compounds can be formulated.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the identifiers of the three compounds. The identifiers must be printed in strictly increasing order ($a < b < c$).

If multiple such valid mixtures exist, output the one that is lexicographically smallest (i.e., minimize $a$; in case of a tie, minimize $b$; and if still tied, minimize $c$).

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