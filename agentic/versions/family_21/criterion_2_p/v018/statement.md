# Problem B — Sealing Two Sites Apart

Time limit: 2 s   Memory limit: 256 MB

## Description
Within an underground research facility, there are $n$ distinct chambers connected by $m$ bidirectional transit tubes. For every tube, engineers have calculated a specific remediation expense required to permanently weld it shut. Once a tube is welded, it permits no passage whatsoever.

The facility's administration has allocated a financial limit, $B$, for an upcoming safety protocol. Any proposed modification must ensure that the sum of the expenses for all welded tubes does not exceed $B$. The administration does not dictate how the remaining accessible chambers are grouped; they may form any number of isolated zones, and any chamber may remain accessible to any other, provided the overall expense remains within the limit.

The catalyst for this protocol is the presence of two highly volatile containment sites, located at chambers $s$ and $t$. Your task is to determine if there is a valid set of tubes to weld shut—satisfying the financial limit—that completely eliminates any sequence of open tubes connecting site $s$ to site $t$. If such a configuration is possible, you must also provide the list of tubes to be welded.

## Input
Line 1: five integers $n, m, s, t, B$.
Next $m$ lines: three integers $u, v, w$ — representing a tube between chamber $u$ and chamber $v$ with remediation expense $w$.

## Output
If the separation is possible within the limit, print `YES`. On the next line, print an integer $c$, the number of tubes to weld shut. Then, print $c$ lines, each containing two integers $u$ and $v$ (the endpoints of a welded tube). If there are multiple valid sets of tubes, any one that meets the criteria is accepted.
If it is impossible to separate the sites without exceeding the limit, print `NO`.

## Example

**Input**
```text
4 4 1 4 10
1 2 4
1 3 5
2 4 4
3 4 5
```

**Output**
```text
YES
2
1 2
1 3
```
