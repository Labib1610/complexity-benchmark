# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant uses an automated system to divide its workforce into exactly two daily shifts. The system's pipeline has three distinct phases. Phase one compiles a comprehensive log of worker incompatibilities. You are responsible for phase two: analyzing a log that has already been flagged as unresolvable. Your task is not to attempt a valid shift allocation, but to extract a definitive proof of failure to feed into phase three, which will then use your proof to justify opening a third shift.

An incompatibility means that two specific workers cannot be scheduled during the same shift. This relationship is strictly symmetric; an incompatibility between worker $x$ and worker $y$ applies in both directions. 

To prove that a two-shift schedule is unachievable, you must identify a triad of workers where every individual in the triad is incompatible with both of the other two. The log is guaranteed to contain at least one such triad.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of workers and the number of incompatibilities, respectively.
The following $m$ lines each contain two integers $u$ and $v$, specifying that worker $u$ and worker $v$ are incompatible.
The input is guaranteed to contain at least one valid triad.

## Output
Output a single line containing three integers $a$, $b$, and $c$ representing the workers in your chosen triad. These must be formatted such that $a < b < c$. All three corresponding pairs (the pair $a, b$, the pair $a, c$, and the pair $b, c$) must exist in the incompatibility log. 
If multiple valid triads exist, you must output the lexicographically earliest one (prioritizing the smallest possible value for $a$, then the smallest for $b$, and finally the smallest for $c$).

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