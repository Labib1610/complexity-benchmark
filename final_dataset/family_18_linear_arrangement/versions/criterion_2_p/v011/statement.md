# Problem B — Synthetic Protein Backbone

Time limit: 5 s   Memory limit: 256 MB

## Description
A synthetic protein consists of $n$ distinct amino acid domains. These domains must be assembled into a single linear chain, meaning each domain is assigned a unique integer position from $1$ to $n$ along the backbone.

The molecule's tertiary structure is defined by $m$ essential chemical bonds between specific pairs of domains. These bonds are designed such that they link all $n$ domains together into a single unified framework without forming any closed rings.

When a bond connects a domain placed at sequence position $x$ and a domain placed at sequence position $y$, the backbone must fold to bring them together. This folding imposes a structural strain on the molecule exactly equal to the sequence distance $|x - y|$.

The total strain energy of the synthesized protein is the sum of the structural strains from all $m$ essential bonds. For the protein to remain stable, its total strain energy must not exceed a given threshold $B$.

You must determine whether it is possible to assign the $n$ domains to the $n$ backbone positions such that the total strain energy is at most $B$.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that an essential bond must form between domain $u$ and domain $v$. (The bonds form a ring-free connected framework, so $m = n - 1$).

## Output
If a stable linear chain can be formed, print `YES` on the first line. On the second line, print $n$ integers, where the $i$-th integer represents the backbone position (from $1$ to $n$) assigned to domain $i$. 
If no arrangement can meet the stability threshold, print `NO`.

## Example

### Input
```text
5 4 6
1 2
1 3
1 4
1 5
```

### Output
```text
YES
3 1 2 4 5
```
