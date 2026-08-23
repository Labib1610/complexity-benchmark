# Problem C — Ternary Reaction Hazard

Time limit: 2 s   Memory limit: 256 MB

You are analyzing a laboratory protocol involving $n$ distinct chemical reagents. Through preliminary testing, you have compiled a list of two-reagent mixtures that produce a precipitate. 

A specific reaction hazard, known as a ternary complex, is triggered when a precipitate-forming pair of reagents is mixed with a third distinct reagent, under the condition that this third reagent is also recorded in your testing data as producing a precipitate with each of the first two reagents individually.

Your task is to identify three reagents that create this hazard. The provided testing data guarantees that at least one such ternary complex can be formed.

## Input
The first line provides two integers, $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of reagents and the number of documented precipitate reactions, respectively. Reagents are identified by integers from $1$ to $n$.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that reagent $u$ and reagent $v$ produce a precipitate when mixed.
It is guaranteed that the provided records contain at least one ternary complex.

## Output
Output three integers $a$, $b$, and $c$ on a single line, ordered such that $a < b < c$, representing the three reagents that comprise the ternary complex. If there is more than one valid set of three reagents, you must output the one that minimizes the hazard score, calculated as $a \cdot 10^8 + b \cdot 10^4 + c$.

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