# Problem B — Regional Oversight

Time limit: 1 s   Memory limit: 256 MB

A corporation operates $n$ regional branches, numbered 1 through $n$. A recent restructuring requires that every branch be placed under the direct oversight of exactly one of two senior executives: Executive 1 or Executive 2.

The corporate audit has identified $m$ client overlap disputes. Each dispute involves a specific pair of branches that are aggressively competing for the same local accounts. To guarantee impartial mediation and prevent internal conflict, any two branches involved in a dispute must report to different executives.

You must determine an executive assignment for all $n$ branches that resolves all disputes according to this rule. If no such assignment is possible, you must report the failure.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of branches involved in a client overlap dispute.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```