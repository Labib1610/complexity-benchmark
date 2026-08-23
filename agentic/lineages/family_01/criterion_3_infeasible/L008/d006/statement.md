# Problem C — Flavor Harmonies

Time limit: 2 s   Memory limit: 256 MB

You are developing a new culinary algorithm using a database of $n$ distinct ingredients. Through extensive taste testing, you have compiled a list of ingredient pairs that complement each other perfectly.

A "perfect harmony" is achieved by a set of exactly three distinct ingredients if each of the three ingredients complements both of the other two.

Your task is to identify a set of three ingredients that creates a perfect harmony. The provided testing data guarantees that at least one such set exists.

## Input
The first line provides two integers, $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of ingredients and the number of complementary pairs, respectively. Ingredients are identified by integers from $1$ to $n$.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that ingredient $u$ and ingredient $v$ complement each other.
It is guaranteed that the provided records contain at least one set of three ingredients forming a perfect harmony.

## Output
Output three integers $a$, $b$, and $c$ on a single line, ordered such that $a < b < c$, representing the three ingredients that comprise the perfect harmony. If there is more than one valid set of three ingredients, you must output the one that minimizes the harmony score, calculated as $a \cdot 10^8 + b \cdot 10^4 + c$.

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