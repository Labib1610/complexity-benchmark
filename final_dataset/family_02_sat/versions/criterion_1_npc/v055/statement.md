# Problem A — Protein Folding Stabilization

Time limit: 2 s   Memory limit: 256 MB

## Description

A synthetic protein chain is being designed with exactly **n** variable residue positions. Each position must be permanently synthesized in one of two chiral forms: Levorotatory (L) or Dextrorotatory (D). There is no intermediate state, and no position can be omitted.

Molecular dynamics simulations have identified **m** structural stress points that will cause the protein to misfold. To correct a stress point, a chaperone protein must bind to a specific conformational motif near that point. Each motif consists of exactly three binding targets, where a target specifies a position index and the exact chiral form it must take. 

The chaperone binds successfully, correcting the stress point, if the final protein chain satisfies **at least one** of the three targets in its motif. If a chaperone detects none of its three required targets, it fails to bind, and the protein misfolds. A single position's chirality will often affect multiple different motifs, potentially satisfying some while failing others. The motifs may overlap heavily or barely at all—what matters is strictly whether each stress point's specific targets are met.

Your objective is to determine whether there exists a single, complete sequence of chiral assignments for all **n** positions that simultaneously corrects **every** stress point. If such a sequence exists, you must provide one. Otherwise, you must declare that the protein cannot be stabilized.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400), representing the number of position variables and the number of stress points, respectively.

Each of the following m lines describes the three targets for a single chaperone motif. Each line contains three non-zero integers, $l_1, l_2, l_3$, where the absolute value $|l_i|$ (which is $\le n$) represents the position index. 
- A positive integer $l_i$ specifies that the target requires position $|l_i|$ to be in the **Levorotatory (L)** form.
- A negative integer $l_i$ specifies that the target requires position $|l_i|$ to be in the **Dextrorotatory (D)** form.

For the protein to fold correctly, every stress point must have at least one of its three targets met.

## Output
If no valid sequence of assignments exists that corrects all stress points, print a single line containing `NO`.

If a valid sequence is possible, print `YES` on the first line. On the second line, print n space-separated integers $s_1, s_2, \dots, s_n$ (each either `0` or `1`), where $s_i = 1$ if position $i$ is Levorotatory (L), and $s_i = 0$ if position $i$ is Dextrorotatory (D). If multiple valid sequences exist, any of them will be accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each motif lists exactly three targets. The same position index may appear more than once in a single motif's list.
