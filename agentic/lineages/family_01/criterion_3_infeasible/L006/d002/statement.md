# Hazardous Cargo Certificate

Time limit: 2 s   Memory limit: 256 MB

You are managing the logistics for transporting $n$ containers of hazardous chemicals, numbered 1 through $n$. Safety regulations mandate that certain combinations of two chemicals will react catastrophically if they are stored in the same cargo hold. You are provided with a manifest detailing $m$ such reactive combinations.

Your transport vessel currently has only two isolated cargo holds. The provided safety regulations make it impossible to load all the containers into just two holds without risking a reaction. Your task is to generate a minimal proof of this impossibility to justify requisitioning a vessel with a third cargo hold.

Specifically, you must identify a set of exactly three containers where every possible grouping of two containers within that set is listed as reactive in the manifest. Because only two holds are available, any such set guarantees that at least two of its containers would be forced to share a hold, violating the safety regulations. Output one such set.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of containers and the number of reactive combinations.
Each of the next $m$ lines contains two integers $u$ and $v$ — a specific combination of two containers that react with each other.
It is guaranteed that at least one set of three containers meeting this criteria exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that the two-container combinations $a$–$b$, $a$–$c$, and $b$–$c$ are all reactive. Output the lexicographically smallest such set (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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