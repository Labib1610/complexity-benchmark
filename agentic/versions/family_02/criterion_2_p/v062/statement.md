# Problem B — Ecological Safeguards

Time limit: 1 s   Memory limit: 256 MB

## Description

A botanical research facility houses $n$ distinct plant species. To maintain the artificial ecosystem, a central control system must determine a global climate configuration. The configuration space is vast: each of the $n$ species must be assigned to exactly one of two micro-climates, Humid (represented by 1) or Arid (represented by 0), resulting in $2^n$ potential global states.

The ecosystem's stability is governed by a complex set of $m$ interacting survival criteria. A failure to satisfy even a single criterion will lead to ecological collapse. To evaluate a criterion, we look at specific species and their assigned micro-climates. A climate condition is denoted by a non-zero integer $v$: if $v > 0$, the condition is that species $v$ is in the Humid micro-climate. If $v < 0$, the condition is that species $|v|$ is in the Arid micro-climate. Each of the $m$ criteria lists exactly two such conditions, and requires that a valid ecosystem must exhibit at least one of them.

Searching for a valid global state requires navigating the enormous $2^n$ state space to find an assignment that respects all $m$ local rules simultaneously. Because of the intricate dependencies between species, a choice made for one plant can trigger a cascade of forced assignments across the facility. 

Your task is to determine if there exists at least one global climate configuration out of the $2^n$ possibilities that simultaneously fulfills all $m$ survival criteria. If such a configuration exists, you must provide it; otherwise, declare that no such arrangement is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of species and the number of survival criteria.
Each of the next $m$ lines specifies a single survival criterion using two non-zero signed integers $l_1$ and $l_2$, where $|l_i| \le n$. The criterion is fulfilled if at least one of these two climate conditions is satisfied by the global configuration.

## Output
If no valid configuration can be found among all possible states, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) representing any valid global configuration, where $s_i$ represents the micro-climate assigned to species $i$.

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
Multiple valid configurations may exist; any one is accepted. The same species or climate state may appear in multiple survival criteria.
