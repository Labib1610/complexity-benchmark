# Problem A — Partitioning a Network into Isolated Subnets

Time limit: 5 s   Memory limit: 256 MB

## Description
A distributed system is a network of servers joined by data links, each data link carrying a cancellation fee that reflects the contractual penalty to terminate it permanently. Several servers are designated restricted databases, each holding sensitive records that must never share an accessible network partition with the sensitive records at another restricted database. The security team will terminate a chosen set of data links; a data link, once terminated, no longer permits data transmission in either direction.

After the works, the restricted databases must be **mutually isolated**: for every pair of restricted databases, there must be no remaining path of active data links connecting them, so each database ends up in its own separated region of the network. Servers that are not restricted databases may fall into whichever region the termination produces — their placement is unconstrained and irrelevant to acceptance. What is measured is solely the total cancellation fee, the sum of the fees of the data links actually terminated.

There is a fixed security budget. Choose a set of data links to terminate whose total fee does not exceed the budget and whose removal leaves every pair of restricted databases disconnected, or report that no termination within budget can isolate all databases simultaneously. (Isolating any one pair may be cheap; the budget must cover separating all databases from one another at once.)

## Input
Line 1: four integers n, m, k, B. Line 2: k database ids. Next m lines: three integers u v w — a link.

## Output
`YES`, then a line with the number c of removed links, then c lines "u v"; or `NO`.

## Example

### Input
```
4 3 3 10
1 2 3
1 4 5
2 4 5
3 4 5
```

### Output
```
YES
2
1 4
2 4
```
