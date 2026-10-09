# Problem A — Sealing a Facility into Isolated Containment Zones

Time limit: 5 s   Memory limit: 256 MB

## Description
A research facility is a network of $n$ rooms joined by $m$ bidirectional corridors. Each corridor has a known sealing cost, reflecting the labour and materials required to close it permanently. $k$ of these rooms are designated as containment sites, which hold hazardous materials. 

To ensure safety, the facility must be divided into isolated regions. Your objective is to seal a chosen set of corridors so that no two containment sites remain connected by any path of unsealed corridors. Once a corridor is sealed, it no longer permits passage in either direction.

Notice that the $n - k$ ordinary rooms are completely unconstrained. They do not hold hazardous materials and do not need to be separated from anything in particular. This means they can freely join the safe zone of any containment site without penalty. Because of this structural flexibility, the boundaries separating the containment sites can be shifted locally to wherever the corridors are cheapest to seal. You are essentially just assigning each ordinary room to a containment site's zone in a way that minimizes the sum of the costs of the corridors that end up bridging different zones.

You are given a fixed remediation budget $B$. Choose a set of corridors to seal whose total cost does not exceed $B$ and whose removal perfectly isolates all $k$ containment sites from one another simultaneously. If no such sealing plan is possible within the budget, you must report it. What is measured is solely the total sealing cost (the sum of the costs of the corridors actually sealed).

## Input
Line 1: four integers $n$, $m$, $k$, $B$.
Line 2: $k$ integers, representing the room IDs of the containment sites.
Next $m$ lines: three integers $u$, $v$, $w$ representing a corridor between room $u$ and room $v$ with a sealing cost of $w$.

## Output
`YES`, then a line with the number $c$ of sealed corridors, then $c$ lines each containing two integers $u$ and $v$ representing a sealed corridor; or `NO`.

## Example

### Input
```text
5 6 3 16
1 3 5
1 2 4
2 3 5
2 4 3
3 4 6
4 5 4
1 5 8
```

### Output
```text
YES
3
1 2
4 5
1 5
```
