# Problem C — Volatile Mixtures

Time limit: 2 s   Memory limit: 256 MB

An industrial facility maintains an inventory of $n$ reactive substances, indexed from 1 to $n$. Specific pairs of these substances are known to react violently upon contact and require strict isolation from one another.

The facility's hazard team is searching for a critical vulnerability: a selection of exactly three substances such that there are exactly three distinct documented incompatible pairs where both substances in the pair belong to this trio. A breach involving such a group would trigger a self-sustaining chain of reactions.

You are provided with the comprehensive log of incompatible substance pairs. Your objective is to locate one such trio of substances.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each contain two integers $u$ and $v$ — representing a distinct pair of substances that react violently.
It is guaranteed that there is at least one trio of substances meeting the hazard criteria.

## Output
Output three integers $a$ $b$ $c$ on a single line, ordered such that $a < b < c$, representing the substances in the trio. If multiple such trios exist, output the one that is lexicographically smallest (the one with the smallest $a$; in case of a tie, the smallest $b$; and finally the smallest $c$).

## Example 1
Input:
4 5
1 2
1 3
2 3
2 4
3 4

Output:
1 2 3

## Example 2
Input:
5 6
1 2
1 4
2 4
3 4
3 5
4 5

Output:
1 2 4