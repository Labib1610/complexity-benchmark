# Signal Collapse Detection

Time limit: 2 s   Memory limit: 256 MB

A telecommunications system consists of $n$ transmission towers, numbered 1 through $n$. Due to frequency misconfigurations, certain pairs of towers experience direct signal interference. You are provided with a log of $m$ such interfering pairs.

A severe system failure occurs whenever there is a group of exactly three distinct towers such that every tower in the group directly interferes with both of the other two. It is guaranteed that the current system configuration contains at least one such group.

Your task is to identify a group of three towers causing a severe system failure. To ensure a standardized report, you must list the three tower identifiers in ascending order. If there are multiple such groups of three towers, you must report the one whose sequence of three identifiers is lexicographically smallest. That is, choose the group with the smallest first identifier; in case of a tie, the smallest second identifier; and if still tied, the smallest third identifier.

## Input
The first line of the input contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$), representing the number of towers and the number of interfering pairs, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that tower $u$ and tower $v$ directly interfere with each other. Each pair of interfering towers is listed at most once.

## Output
Output a single line containing three integers $a$, $b$, and $c$ ($a < b < c$), representing the identifiers of the three towers that mutually interfere. Ensure the sequence $a, b, c$ is the lexicographically smallest valid sequence.

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
