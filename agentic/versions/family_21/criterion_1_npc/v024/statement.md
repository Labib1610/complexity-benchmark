# Divesting the Corporate Network

Time limit: 5 s   Memory limit: 256 MB

## Description
A multinational corporation is spinning off several of its divisions into completely independent businesses. The legacy corporate IT infrastructure consists of various hardware appliances wired together by direct data cables. Each cable has a known decommissioning impact score, representing the operational disruption caused by removing that specific cable. 

Among the appliances, there are several designated primary mainframes, each belonging exclusively to one of the newly independent businesses. To comply with strict data separation laws, the network must be physically partitioned so that no data can travel between any two primary mainframes. A cable, once removed, stops all data transmission between the two appliances it previously connected. 

The reorganization committee must select a set of cables to remove. After removal, there must be no sequence of remaining cables that connects any primary mainframe to any other primary mainframe. Appliances that are not primary mainframes do not have strict assignment rules; they may remain connected to one primary mainframe, multiple non-primary appliances, or be isolated entirely. The only regulatory requirement is the mutual disconnection of all primary mainframes.

The committee has a maximum allowable disruption threshold. Determine a set of cables to remove such that all primary mainframes are mutually separated and the sum of their decommissioning impact scores is less than or equal to this threshold. If no such set of cables exists within the threshold, the separation is deemed impossible.

## Input
Line 1: four integers $n$, $m$, $k$, $B$.
Line 2: $k$ integers, the identifiers of the primary mainframes.
Next $m$ lines: three integers $u$, $v$, $w$ — a cable connecting appliance $u$ and appliance $v$ with disruption score $w$.

## Output
`YES`, then a line with the number $c$ of removed cables, then $c$ lines "$u$ $v$" (the endpoints of each removed cable); or `NO`.

## Examples

**Input 1:**
```
4 3 3 6
1 2 3
1 4 3
2 4 4
3 4 2
```

**Output 1:**
```
YES
2
1 4
3 4
```

**Input 2:**
```
4 3 3 4
1 2 3
1 4 3
2 4 4
3 4 2
```

**Output 2:**
```
NO
```
