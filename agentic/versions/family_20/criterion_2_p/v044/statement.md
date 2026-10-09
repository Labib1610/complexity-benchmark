# Problem B — Routing Matrix Maintenance

Time limit: 2 s
Memory limit: 256 MB

## Description
A high-frequency trading exchange relies on a routing matrix with two distinct banks of ports: ingress ports and egress ports. The matrix is populated with $m$ discrete physical links. Every link connects exactly one ingress port to exactly one egress port. Links never run between two ports in the same bank.

Routine maintenance requires taking links offline during designated service windows. The strict hardware limitation is that a port cannot have more than one of its attached links taken offline simultaneously. Therefore, any two links that share a port (whether ingress or egress) must be assigned to strictly different service windows. 

Let $\Delta$ be the maximum number of links attached to any single port across the entire matrix. Since all $\Delta$ links at this busiest port must be assigned distinct windows, any valid maintenance schedule requires at least $\Delta$ service windows. 

Your task is to assign each of the $m$ links to a service window chosen from the set $\{1, 2, \dots, \Delta\}$. Because each of the $m$ links can potentially be assigned to any of the $\Delta$ windows, the configuration space consists of $\Delta^m$ possible schedules. For the scale of the exchange, this state space is astronomically large. You must explore this vast space of assignments to find a valid schedule that satisfies all port overlap constraints without exceeding $\Delta$ total windows. It is guaranteed that at least one such valid configuration exists.

## Input
The first line contains three integers $n_L$, $n_R$, and $m$ ($1 \le n_L, n_R \le 100000$, $0 \le m \le 400000$), representing the number of ingress ports, the number of egress ports, and the number of links, respectively.
The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_L$, $1 \le v \le n_R$), representing a physical link between ingress port $u$ and egress port $v$.

## Output
Print `YES` on the first line.
On the second line, print $m$ space-separated integers, where the $i$-th integer is the service window (from $1$ to $\Delta$, inclusive) assigned to the $i$-th link in the input order. If there are multiple valid configurations, you may output any of them.

## Example

### Input
```text
3 3 4
1 1
1 2
2 1
3 3
```

### Output
```text
YES
1 2 2 1
```
