# Problem B — Resonant Bond Excitation

Time limit: 2 s   Memory limit: 256 MB

## Description
A synthetic molecule is stabilized by activating its resonant bonds. The molecule is constructed from two sets of reactive sites: donor nodes and acceptor nodes. Every bond is formed by linking exactly one donor node to exactly one acceptor node. 

During the stabilization procedure, each bond must be triggered during a discrete excitation phase (numbered 1, 2, 3, and so on). The triggering schedule must obey a strict safety protocol: no node—whether it is a donor or an acceptor—can participate in more than one triggered bond during the same phase, as the overlapping energy would destabilize it.

The overall stabilization must be completed as quickly as possible. The node involved in the highest number of bonds dictates the absolute minimum number of phases required. Let this maximum local bond count be $\Delta$. Because of the strict operational rules governing how bonds are formed, it is physically guaranteed that all bonds can be safely scheduled using exactly $\Delta$ phases. 

Your task is to assign an excitation phase to every bond such that no node's safety protocol is violated, using at most $\Delta$ distinct phases.

## Input
The first line contains three integers $n_L$, $n_R$, and $m$ ($1 \le n_L, n_R \le 100000$, $0 \le m \le 400000$), representing the number of donor nodes, the number of acceptor nodes, and the total number of bonds.

The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_L$, $1 \le v \le n_R$), indicating a bond between donor node $u$ and acceptor node $v$. Multiple bonds can exist between the same pair of nodes.

## Output
Print `YES` on the first line. On the second line, print $m$ space-separated integers in the range $1 \dots \Delta$ — the assigned excitation phase for each bond in the exact order they appear in the input (bonds sharing any node must receive different phase numbers).

## Example

### Input
```text
3 3 5
1 1
1 2
2 2
2 3
3 3
```

### Output
```text
YES
1 2 1 2 1
```
