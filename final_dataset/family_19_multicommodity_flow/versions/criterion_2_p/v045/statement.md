# Problem B — Pneumatic Tube Logistics

Time limit: 2 s
Memory limit: 256 MB

## Description
An organization manages a complex of $n$ distinct chambers. To facilitate rapid physical communication, they have built a network of $m$ one-way pneumatic pipelines connecting specific pairs of chambers. Each pipeline is built with a specific pressure rating, which dictates a strict threshold on the quantity of cylindrical carriers it can handle during a shift. The quantity of carriers directed into any pipeline must be a whole number. A pipeline cannot operate in reverse (meaning the carrier count cannot drop below zero), and attempting to push a count of carriers greater than the pipeline's pressure rating will cause a catastrophic jam.

Chamber $s$ acts as the primary sender and must dispatch exactly $d$ more carriers into the network than it takes in. Chamber $t$ acts as the final receiver and must take in exactly $d$ more carriers from the network than it dispatches. Every other chamber acts merely as a relay: its total carrier intake must perfectly balance its total outtake. Carriers cannot be stockpiled, lost, or spontaneously created anywhere in the system.

Your objective is to deduce a valid allocation of carriers for each pipeline such that all pressure thresholds and chamber conditions are satisfied.

## Input
The first line provides three integers $n$, $m$, and $k$ (where $k = 1$, representing a single batch of carriers).
The second line provides three integers $s$, $t$, and $d$.
The subsequent $m$ lines each provide three integers $u$, $v$, and $cap$, detailing a one-way pipeline from chamber $u$ to chamber $v$ with a pressure rating of $cap$ carriers.

## Output
If a valid allocation can be achieved, output `YES` on the first line. On the second line, output $m$ space-separated integers, representing the count of carriers routed through each pipeline, in the exact order the pipelines were detailed in the input. If no valid allocation is possible, output `NO`.

## Example

### Input
```text
4 5 1
1 4 10
1 2 5
1 3 10
2 3 5
2 4 5
3 4 5
```

### Output
```text
YES
5 5 0 5 5
```
