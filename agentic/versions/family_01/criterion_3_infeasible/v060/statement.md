# Problem C — Feedback Cascade

Time limit: 2 s   Memory limit: 256 MB

The system you are evaluating consists of $n$ signal relays. Among these relays, there are $m$ active bidirectional mirroring configurations. Each configuration links two specific relays such that any signal received by either is instantaneously mirrored to the other.

When three distinct relays are all mutually linked by these mirroring configurations—meaning each relay in the group of three is directly linked to both of the other two—any signal entering the group is trapped in an infinite amplification loop. Such a configuration triggers a critical failure known as a feedback cascade. Diagnostic scans confirm that the current network architecture is unstable and contains at least one such group of three relays.

Your objective is to pinpoint a source of this instability. You must find three relays that form a feedback cascade. To standardize the diagnostic report, the three relay identifiers must be listed in ascending order. If there is more than one such group of three relays, you must output the lexicographically smallest sequence of three identifiers (meaning the group with the lowest first identifier, tying groups broken by the lowest second identifier, and finally the lowest third).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of relays linked by a mirroring configuration.
It is guaranteed that at least one feedback cascade exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that the pairs $a$–$b$, $a$–$c$, and $b$–$c$ are all linked by mirroring configurations. Output the lexicographically smallest such triple (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
