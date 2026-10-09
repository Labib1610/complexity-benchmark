# Colony Provisioning

Time limit: 2 s
Memory limit: 256 MB

## Description
An ant colony needs to transport exactly $d$ food crumbs from the entrance chamber ($s$) to the queen's chamber ($t$) before winter. The nest consists of $n$ chambers and $m$ one-way tunnels connecting them.

Each tunnel is constructed with a specific number of discrete lanes. The transport occurs in a single, synchronized push. During this push, each lane can be occupied by at most one ant carrying one crumb. Tunnels are strictly one-way, meaning the count of crumbs moving through them is inherently a non-negative whole number. Because each crumb requires its own lane, it is physically impossible to send more crumbs through a tunnel than its total number of lanes.

Crumbs cannot be stored in intermediate chambers. For any chamber other than the entrance and the queen's chamber, every crumb brought in through incoming tunnels must immediately be carried out through outgoing tunnels. At the entrance chamber, the net number of departing crumbs (those leaving minus any that might loop back) must equal exactly $d$. At the queen's chamber, the net number of arriving crumbs (those arriving minus any that might leave) must equal exactly $d$.

Determine if it is possible to dispatch the $d$ crumbs under these constraints. If it is, provide the number of crumbs to be sent through each tunnel.

## Input
The first line contains three integers: $n$ (the number of chambers), $m$ (the number of tunnels), and $1$ (indicating a single crumb type).
The second line contains three integers: $s$ (the entrance chamber), $t$ (the queen's chamber), and $d$ (the required number of crumbs).
The next $m$ lines each contain three integers $u$, $v$, and $w$, describing a one-way tunnel from chamber $u$ to chamber $v$ with a width of $w$ lanes.

## Output
If the transport is possible, output `YES` on a single line, followed by a second line containing $m$ integers. These integers must represent the number of crumbs dispatched through each tunnel, matching the order the tunnels were provided in the input. If it is impossible to transport exactly $d$ crumbs under these rules, output `NO`.

## Examples

**Input 1**
```text
4 5 1
1 4 10
1 2 5
1 3 5
2 3 2
2 4 3
3 4 7
```

**Output 1**
```text
YES
5 5 2 3 7
```

**Input 2**
```text
3 2 1
1 3 10
1 2 5
2 3 4
```

**Output 2**
```text
NO
```
