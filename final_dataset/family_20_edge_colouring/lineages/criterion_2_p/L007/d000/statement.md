# Problem B — Firmware Maintenance on an Exchange Fabric

Time limit: 2 s   Memory limit: 256 MB

## Description
A datacenter exchange fabric routes traffic from a bank of ingress switches to a bank of egress switches. 
Every fiber-optic link connects exactly one ingress switch to exactly one egress switch. 
The fabric contains no links between two ingress switches, and no links between two egress switches.

Each link requires a diagnostic test that takes exactly one maintenance cycle. 
To maintain routing stability, any single switch—whether ingress or egress—can have at most one of its connected links tested during the same maintenance cycle. 
The total number of maintenance cycles allowed for the entire operation is strictly determined by the switch with the highest number of connected links. 
If the busiest switch in the entire fabric is connected to $K$ links, the operation must conclude in exactly $K$ maintenance cycles.

Your task is to assign a maintenance cycle (numbered 1 through $K$) to every link such that no switch has multiple links tested in the same cycle. 
The strict two-sided topology of this exchange fabric guarantees that a schedule requiring only $K$ cycles is always mathematically possible.

## Input
The first line provides three integers $n_L$, $n_R$, and $m$ (1 ≤ $n_L$, $n_R$ ≤ 100000, 0 ≤ $m$ ≤ 400000), representing the number of ingress switches, the number of egress switches, and the total number of links, respectively.
The following $m$ lines each contain two integers $u$ and $v$ (1 ≤ $u$ ≤ $n_L$, 1 ≤ $v$ ≤ $n_R$), indicating a link connecting ingress switch $u$ to egress switch $v$.

## Output
Print `YES` on the first line.
On the second line, print $m$ space-separated integers, each between 1 and $K$, representing the cycle assigned to each link in the order they were given in the input.

## Example

### Input
```text
3 3 4
1 1
1 2
2 2
3 3
```

### Output
```text
YES
1 2 1 1
```
