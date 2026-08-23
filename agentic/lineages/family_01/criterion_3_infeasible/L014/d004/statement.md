# Problem C — Platform Foundation

Time limit: 2 s   Memory limit: 256 MB

You are designing an offshore facility supported by $n$ structural pillars. Due to the underwater terrain, only certain pairs of pillars are positioned such that a standard load-bearing beam can be installed between them. You have a survey listing $m$ such valid pillar pairs.

You need to construct a rigid primary deck. This deck must be supported by exactly three distinct pillars. To ensure structural integrity, a load-bearing beam must be installed between every pair of those three pillars. Therefore, a set of three pillars can only support the deck if all three possible pairs among them appear in your survey of valid pairs.

Find a set of three pillars that can support the primary deck.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of pillars and the number of valid pillar pairs. Pillars are numbered from $1$ to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that a beam can be installed between pillar $u$ and pillar $v$.
It is guaranteed that the input contains at least one valid set of three pillars for the deck.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the IDs of the three pillars.
If there are multiple valid sets of three pillars, output the one that is lexicographically smallest (i.e., smallest $a$; ties broken by smallest $b$; then smallest $c$).

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