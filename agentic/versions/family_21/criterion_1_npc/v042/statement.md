# Problem A — Containment Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description
A massive cloud infrastructure consists of $n$ data centers connected by $m$ bidirectional fiber-optic links. A severe security breach has occurred: rogue AI instances have taken over exactly $k$ of these data centers.

To prevent the rogue instances from merging their codebases and becoming unstoppable, you must ensure that no two compromised data centers can exchange data. Because data can be routed through any sequence of active fiber-optic links, you must physically sever some links so that there is absolutely no active communication route remaining between any pair of the $k$ compromised data centers. The connectivity of the other $n - k$ data centers is irrelevant, provided the rogue instances are completely separated from one another.

Severing the link between a specific pair of data centers requires a certain number of labor hours. You have an emergency response budget of $B$ labor hours. You must select a set of links to sever such that their total labor requirement does not exceed $B$, leaving all $k$ compromised data centers fully isolated from each other in terms of data exchange. If such a containment plan is possible, you must output the links to sever; otherwise, you must declare it impossible.

## Input
The first line contains four integers $n$, $m$, $k$, and $B$.
The second line contains $k$ integers representing the identifiers of the compromised data centers.
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating a fiber-optic link between data center $u$ and data center $v$ that requires $w$ labor hours to sever.

## Output
If it is possible to achieve the containment goals without exceeding the labor budget $B$, print `YES` on the first line. On the second line, print an integer $c$ representing the number of severed links. Then, output $c$ lines, each containing two integers $u$ and $v$, representing the endpoints of a severed link.
If it is not possible, print `NO` on a single line.

## Example

### Input
```
4 3 3 10
1 2 3
1 4 3
2 4 4
3 4 5
```

### Output
```
YES
2
1 4
2 4
```
