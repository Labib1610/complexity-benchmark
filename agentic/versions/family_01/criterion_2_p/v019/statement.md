# Problem B — Genetic Modification Protocols

Time limit: 1 s   Memory limit: 256 MB

You are designing a genetic therapy involving $n$ target genes, numbered 1 through $n$. Each gene must be treated with exactly one of two available enzymes, designated as Enzyme 1 and Enzyme 2.

Through clinical trials, you have identified $m$ epistatic interactions between specific pairs of genes. If two genes that share an epistatic interaction are treated with the exact same enzyme, the combined effect produces a toxic response. Therefore, every interacting pair must be treated with different enzymes.

Determine if there is a safe treatment plan for all $n$ genes. If multiple safe plans exist, you must output the unique plan that prioritizes Enzyme 1. Specifically, if you compare the correct plan to any other valid treatment plan gene by gene starting from gene 1, the correct plan will always feature Enzyme 1 at the first gene where the two plans differ.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of genes and the number of epistatic interactions.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that gene $u$ and gene $v$ share an epistatic interaction.

## Output
If there is no safe treatment plan that avoids all toxic responses, output a single line containing `NO`.
If a safe plan is possible, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer (either 1 or 2) represents the enzyme assigned to gene $i$. This sequence must satisfy the priority condition described above.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
