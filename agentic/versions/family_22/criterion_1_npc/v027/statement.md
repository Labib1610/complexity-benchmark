# Problem A — Botanical Nutrient Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description
A botanical research facility cultivates a rare flora requiring precise nutrient management. The protocol involves exactly $n$ distinct nutrient injections, numbered 1 to $n$.

The greenhouse's automated delivery system operates on a daily cycle. During any single day, the system's manifold can safely deliver a maximum of $M$ injections. There is no requirement to maximize daily usage, but the daily limit of $M$ cannot be exceeded.

Furthermore, the plant's biological absorption dictates strict sequential dependencies between certain pairs of nutrients. You are given $m$ specific rules of the form $(a, b)$, which mandate that nutrient $a$ must be entirely absorbed before nutrient $b$ is introduced. Since absorption requires a full day of resting, injection $a$ must be administered on a strictly earlier day than injection $b$. Administering them on the same day is invalid.

The plant's critical growth phase is finite, providing a rigid window of $T$ consecutive days to complete the entire protocol.

Determine if there exists a valid assignment that allocates every one of the $n$ injections to a specific day (from 1 to $T$) such that no day exceeds the $M$-injection capacity and all absorption dependencies are respected. If a valid assignment exists, output it; otherwise, report that the protocol cannot be completed within the window.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$.
The following $m$ lines each contain two integers $a$ and $b$, indicating that injection $a$ must be administered on a strictly earlier day than injection $b$.

## Output
Print `YES` followed by $n$ integers $d_1, d_2, \dots, d_n$ (the day assigned to each injection, in the range 1 to $T$); otherwise, print `NO`. If multiple valid assignments exist, any of them will be accepted.

## Example
**Input:**
```
5 2 3 4
1 3
2 3
3 4
3 5
```

**Output:**
```
YES
1 1 2 3 3
```
