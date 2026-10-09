# Phase II: Divestment of Conflicting Subsidiaries

Time limit: 5 s   Memory limit: 256 MB

## Description
The corporate restructuring pipeline consists of three distinct phases. 

In Phase I (Audit), the forensic accounting team mapped a conglomerate consisting of $n$ shell companies and $m$ bilateral joint ventures. Dissolving any single joint venture incurs a specific legal cost. Furthermore, the audit identified exactly $k$ specific companies that hold mutually exclusive regulatory licenses.

Your task is to execute Phase II (Divestment). To comply with anti-monopoly laws, the conglomerate must be fractured. You must select a set of joint ventures to dissolve such that no two licensed companies remain connected through any chain of active joint ventures. The remaining unlicensed companies may end up grouped with any licensed company or in completely independent clusters; the only requirement is that the $k$ licensed companies are completely isolated from one another. You are given a maximum legal budget of $B$ to perform these dissolutions.

If Phase II is successful, Phase III (Spin-off) will auction the resulting independent corporate groups to different buyers. You are only responsible for Phase II: determine if the required separation can be achieved without exceeding the budget, and if so, specify exactly which joint ventures to dissolve.

## Input
The first line contains four integers $n$, $m$, $k$, and $B$: the number of companies, the number of joint ventures, the number of licensed companies, and the maximum legal budget. Companies are numbered from $1$ to $n$.
The second line contains $k$ integers representing the IDs of the licensed companies.
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating an active joint venture between company $u$ and company $v$ that requires a dissolution cost of $w$.

## Output
If the separation is possible within the budget, output `YES` on the first line. On the second line, output the number $c$ of joint ventures to dissolve. Then, output $c$ lines, each containing two integers $u$ and $v$, specifying the joint ventures you have chosen to dissolve. If it is impossible to isolate all licensed companies within the budget, output `NO`.

## Example

### Input
```text
4 3 3 6
1 2 3
1 4 2
2 4 3
3 4 4
```

### Output
```text
YES
2
1 4
2 4
```
