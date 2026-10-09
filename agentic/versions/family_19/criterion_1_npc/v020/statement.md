# Problem A — Synchronized Case Processing in the Ministry

Time limit: 5 s   Memory limit: 256 MB

## Description
The Ministry of Administration consists of $n$ distinct offices. To handle paperwork, there are $m$ established one-way transfer protocols between specific pairs of offices. Each protocol has a strict daily quota on the total number of dossiers it can handle, due to the limited number of clerks assigned to verify the transfers. This quota applies to the aggregate sum of all dossiers moved via that protocol, regardless of their classification. 

Today, the Ministry must process $k$ distinct classifications of legal cases. For each classification, a precise number of dossiers has been submitted. Each classification has a designated intake office, a designated archive office, and a required quantity of dossiers that must be fully processed today.

Dossiers are indivisible physical folders. The Ministry's rules mandate strict accountability for each classification independently:
- At a classification's intake office, the total number of its dossiers sent out minus the total number received must exactly equal its required quantity.
- At its archive office, the total number of its dossiers received minus the total number sent out must exactly equal its required quantity.
- At every other office, the number of its dossiers received must exactly equal the number sent out.

All classifications are processed simultaneously and share the same transfer protocols. Consequently, different classifications compete for the limited daily quotas on the protocols. The number of dossiers of any given classification sent over any given protocol must be a non-negative integer.

You must determine if it is possible to route all dossiers of all classifications from their respective intakes to their archives within a single day without exceeding the quota of any transfer protocol. If it is possible, provide the exact number of dossiers of each classification to be routed through each protocol.

## Input
The first line contains three integers $n$, $m$, and $k$.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the intake office, the archive office, and the required quantity of dossiers for classification $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, indicating a one-way transfer protocol from office $u$ to office $v$ with a daily quota of $cap$ dossiers.

## Output
If all dossiers can be successfully processed without violating any quotas, print `YES` on the first line. Then, print $k$ lines. The $i$-th of these lines should contain $m$ integers, where the $j$-th integer represents the number of dossiers of classification $i$ routed through the $j$-th transfer protocol (in the exact order the protocols were given in the input).
If it is impossible to process all dossiers under the given constraints, print `NO`.

## Example

**Input:**
```text
4 5 2
1 4 2
2 3 1
1 2 2
2 4 1
1 3 1
3 4 2
2 3 1
```

**Output:**
```text
YES
1 1 1 1 0
0 0 0 0 1
```
