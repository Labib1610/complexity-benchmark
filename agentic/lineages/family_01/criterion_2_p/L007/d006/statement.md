# Reagent Oxidation States

Time limit: 1 s   Memory limit: 256 MB

A laboratory is preparing $n$ chemical reagents, numbered 1 to $n$. To stabilize the reagents for a series of tests, each one must be assigned an oxidation state of either 1 or 2.

The testing protocol involves $m$ distinct experiments. Each experiment combines a specific pair of reagents. For an experiment to be successful, the arithmetic mean of the oxidation states of the two combined reagents must evaluate to exactly 1.5.

You need to determine if there is a valid assignment of oxidation states for all $n$ reagents that guarantees all $m$ experiments will be successful. If a valid assignment exists, you must output it. In cases where multiple valid assignments satisfy all requirements, you must output the assignment that forms the lexicographically smallest sequence of oxidation states.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the numbers of the two reagents combined in an experiment.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (each being 1 or 2), representing the lexicographically smallest valid sequence of oxidation states.

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