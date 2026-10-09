# Problem A — Protocol Segregation in Distributed Systems

Time limit: 5 s   Memory limit: 256 MB

## Description
A distributed system consists of processing modules connected by bidirectional data links. Each link requires a specific energy expenditure to be physically severed. Certain modules are designated as primary anchors.

If a primary anchor can send a signal to another primary anchor, their conflicting protocols will cause a system failure. A signal can traverse any sequence of intact links, passing through intermediate modules along the way. 

To prevent failure, you must sever a selection of links. A severed link no longer permits signals to pass in either direction. The selection is successful if no signal can travel between any pair of distinct primary anchors. Once the chosen links are severed, each primary anchor must reside in a completely disjoint communication zone from all other primary anchors. The routing of signals among non-anchor modules is irrelevant, provided the anchors themselves are fully segregated from one another.

You are given an overall energy threshold. Determine if there is a valid selection of links to sever such that the sum of their required energy expenditures is at most the threshold.

## Input
Line 1: four integers $n$, $m$, $k$, $B$. 
Line 2: $k$ integers, the IDs of the primary anchors. 
Next $m$ lines: three integers $u$, $v$, $w$ per line, indicating a link between module $u$ and module $v$ with severance energy $w$.

## Output
If there is a valid selection of links that costs at most $B$, print `YES`. On the next line, print the number of severed links, $c$. Then, output $c$ lines, each containing the two module IDs $u$ and $v$ of a severed link. If no such selection exists within the threshold, print `NO`.

## Example 1

**Input**
```
4 3 3 10
1 2 3
1 4 4
2 4 5
3 4 6
```

**Output**
```
YES
2
1 4
2 4
```
