# Problem A — Segmenting an Intranet into Isolated Security Zones

Time limit: 5 s   Memory limit: 256 MB

## Description
A corporate intranet is a network of servers joined by data links, each link carrying a termination fee that reflects the contractual penalty to cancel it permanently. Several servers are designated root controllers, each managing directories that must never share an accessible zone with the directories at another root controller. The security team will terminate a chosen set of data links; a link, once terminated, no longer permits communication in either direction.

After the works, the root controllers must be mutually isolated: for every pair of root controllers, there must be no remaining path of active data links connecting them, so each controller ends up in its own separated region of the intranet. Servers that are not root controllers may fall into whichever region the termination produces — their placement is unconstrained and irrelevant to acceptance. What is measured is solely the total termination fee, the sum of the fees of the data links actually terminated.

There is a fixed security budget. Choose a set of data links to terminate whose total fee does not exceed the budget and whose removal leaves every pair of root controllers disconnected, or report that no termination within budget can isolate all controllers simultaneously. (Isolating any one pair may be cheap; the budget must cover separating all controllers from one another at once.)

## Input
Line 1: four integers n, m, k, B.
Line 2: k root controller ids.
Next m lines: three integers u v w — a data link.

## Output
`YES`, then a line with the number c of terminated links, then c lines "u v"; or `NO`.

## Example 1

**Input**
```text
4 3 3 10
1 2 3
1 4 4
2 4 5
3 4 6
```

**Output**
```text
YES
2
1 4
2 4
```

## Example 2

**Input**
```text
4 3 3 8
1 2 3
1 4 4
2 4 5
3 4 6
```

**Output**
```text
NO
```
