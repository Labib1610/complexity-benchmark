# Problem C — Feedback Cascade

Time limit: 2 s   Memory limit: 256 MB

You are analyzing a system of $n$ signal relays. The system contains $m$ bidirectional mirroring configurations, each linking a specific pair of relays. When two relays are linked, any signal received by one is immediately mirrored to the other.

A critical system failure known as a "feedback cascade" is triggered whenever there is a set of three distinct relays where every relay in the set is directly linked to both of the other two. This mutual mirroring traps the signal in an infinite amplification loop.

System diagnostics indicate that the network is currently unstable. Your task is to certify the instability by identifying a source. It is guaranteed that at least one such set of three relays exists, proving that the system cannot operate safely.

To standardize the diagnostic report, you must output the identifiers of the three relays involved in the cascade. The identifiers must be listed in ascending order. If there are multiple such sets of three relays, you must report the lexicographically smallest sequence of three identifiers (i.e., the set with the smallest first identifier; in case of a tie, the smallest second identifier; and finally the smallest third identifier).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of relays configured to mirror each other.
It is guaranteed that at least one feedback cascade exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that the pairs $a$–$b$, $a$–$c$, and $b$–$c$ are all linked in the configurations. Output the lexicographically smallest such triple (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
