# Problem B — Paired Menu Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

A banquet features $n$ dishes. Each dish must be prepared in exactly one of two ways: SPICY or MILD. The head chef has established $m$ tasting rules. Every rule specifies exactly two dish-seasoning conditions and is considered satisfied if at least one of the two conditions is met. 

Because each rule links exactly two conditions, failing to meet one condition in a rule strictly forces the other condition to be met. The rules thus propagate as chains of forced consequences. 

To ensure the kitchen is not overwhelmed, the menu planning committee guarantees two properties about the requirements:
1. The sum of the number of dishes and the number of rules ($n + m$) is at most $300,000$.
2. Any chain of strictly distinct forced consequences (where failing one condition forces another, which in turn forces another, without repeating any condition) will never exceed $2n$ steps.

The caterers need to know if there is a single global SPICY/MILD assignment for all $n$ dishes that simultaneously satisfies all $m$ rules. If such an assignment exists, you must provide one. Otherwise, you must report that the rules are mutually contradictory.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two non-zero integers $l_1$ and $l_2$, where $|l_i| \le n$. 
A positive integer $x$ means dish $x$ being SPICY is a condition. A negative integer $-x$ means dish $x$ being MILD is a condition. At least one of the two conditions in each rule must hold.

## Output
If no valid menu exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) forming any valid menu. Output $1$ for SPICY and $0$ for MILD.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid menus may exist; any one is accepted. The same dish index may appear in multiple requirements.
