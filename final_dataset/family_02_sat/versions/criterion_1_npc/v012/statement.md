# Problem A — Lighting Design

Time limit: 2 s   Memory limit: 256 MB

## Description

An art exhibition features $n$ adjustable spotlights. Each spotlight must be fitted with exactly one color filter: either warm or cool. You cannot leave a spotlight without a filter, and no other filter types are available.

The exhibition's curator has established $m$ aesthetic requirements. Each requirement highlights exactly three desired lighting configurations. A configuration consists of a specific spotlight and a requested filter type. A requirement is considered fulfilled if the final gallery setup successfully implements **at least one** of the three configurations it lists. Implementing more than one is perfectly fine, but if a requirement has none of its three configurations implemented, the lighting design is rejected. 

The same spotlight may be mentioned across many different requirements, sometimes requested to be warm and other times requested to be cool. The requirements may overlap significantly or not at all. Each requirement always lists exactly three configurations, and the same spotlight may be referenced multiple times within a single requirement.

Determine if there is a single, complete assignment of filters to all $n$ spotlights that simultaneously fulfills every requirement. If such an assignment exists, provide one. Otherwise, declare that the curator's requirements cannot be met.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines contains three space-separated non-zero integers $l_1$, $l_2$, and $l_3$, representing the three configurations for that requirement.
The absolute value $|l_i|$ ($1 \le |l_i| \le n$) identifies the spotlight. If $l_i$ is positive, it requests a warm filter for that spotlight. If $l_i$ is negative, it requests a cool filter.

## Output
If no valid filter assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each either `0` or `1`), where $s_i = 1$ if spotlight $i$ is fitted with a warm filter, and $s_i = 0$ if it is fitted with a cool filter. Any valid assignment is accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```
