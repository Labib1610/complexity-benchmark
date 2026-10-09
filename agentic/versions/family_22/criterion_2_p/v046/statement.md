# Forensic Ledger Reconstruction

Time limit: 2 s   Memory limit: 256 MB

## Description
A forensic investigator is reconstructing the chronological sequence of $n$ distinct financial transactions. The transactions occurred strictly one at a time, and every transaction must be placed exactly once in the reconstructed sequence.

The investigator has gathered $m$ pieces of documentary evidence. Each piece of evidence is defined by a pair of transactions, $a$ and $b$, proving that transaction $a$ cleared at some point before transaction $b$. The exact number of intermediate transactions between $a$ and $b$ is unknown, but their relative order is absolute.

You must establish a complete timeline from earliest to latest that aligns with all $m$ pieces of evidence simultaneously. If the recovered evidence contains logical contradictions (for instance, indirectly proving a transaction cleared before itself), forming a timeline is impossible.

Produce a valid timeline, or report that it is impossible. Any complete sequence of the $n$ transactions satisfying all evidence is considered a valid reconstruction.

## Input
The first line contains two integers $n$ and $m$, representing the number of transactions and the number of pieces of evidence, respectively. The transactions are identified by integers from $1$ to $n$.
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that transaction $a$ cleared before transaction $b$.

## Output
If a valid timeline is possible, output `YES` on the first line, followed by a second line containing a sequence of the integers $1$ through $n$ separated by spaces. If multiple valid timelines exist, you may output any of them.
If no valid timeline can be formed, output `NO`.

## Example
### Input
```
4 5
1 2
1 3
3 2
2 4
3 4
```

### Output
```
YES
1 3 2 4
```
