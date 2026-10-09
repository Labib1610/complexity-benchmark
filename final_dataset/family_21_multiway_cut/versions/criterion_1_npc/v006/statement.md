# Problem A — Network Segregation of Proprietary Datasets

Time limit: 5 s   Memory limit: 256 MB

## Description
A corporate intranet consists of servers connected by bidirectional data links, each link requiring a specific number of work-hours to permanently sever. Certain servers host distinct proprietary datasets; to comply with strict information silos, no two such servers may remain able to communicate with each other. The security team must sever a chosen set of data links.

Following this operation, the proprietary servers must be completely segregated: for any pair of proprietary servers, there must be no remaining sequence of intact links connecting them. Servers that do not host proprietary datasets may maintain connectivity with any single proprietary server or none at all, as their placement does not impact compliance. The sole metric evaluated is the total work-hours required to sever the chosen links.

Given a maximum work-hour budget, determine a set of links to sever whose total work-hours do not exceed the budget and whose removal leaves every proprietary server disconnected from all others, or report that no such segregation is possible within budget.

## Input
Line 1: four integers $n$, $m$, $k$, $B$. 
Line 2: $k$ proprietary server IDs. 
Next $m$ lines: three integers $u$ $v$ $w$ — representing a data link between server $u$ and server $v$ that takes $w$ work-hours to sever.

## Output
`YES`, then a line with the number $c$ of severed links, then $c$ lines `$u$ $v$`; or `NO`.

## Example

**Input**
```text
4 4 3 11
1 2 3
1 4 4
2 4 5
3 4 6
1 2 2
```

**Output**
```text
YES
3
1 2
1 4
2 4
```
