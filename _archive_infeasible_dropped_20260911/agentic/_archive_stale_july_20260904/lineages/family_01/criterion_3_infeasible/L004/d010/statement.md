# Critical Interference

Time limit: 2 s
Memory limit: 256 MB

A proposed communications standard attempts to allocate $n$ transceivers (labeled 1 through $n$) into a network. However, testing has revealed $m$ specific bidirectional interference links between pairs of transceivers. Each link connects two distinct transceivers, and no two links connect the same pair.

To diagnose the core issue in the network's topology, engineers analyze the *interference energy* of transceiver triplets. For any chosen subset of exactly three transceivers, we order them by their labels as $u_1 < u_2 < u_3$. We can assign them relative phase coefficients, represented by three real numbers $x_1, x_2, x_3$. 
These coefficients must be properly normalized such that their sum is zero ($x_1 + x_2 + x_3 = 0$) and their squared sum is one ($x_1^2 + x_2^2 + x_3^2 = 1$).

The interference energy of the triplet under these coefficients is calculated by summing the products of the coefficients for every pair of transceivers in the triplet that share an interference link. Specifically:
$$E(x_1, x_2, x_3) = x_1 x_2 I_{1,2} + x_2 x_3 I_{2,3} + x_1 x_3 I_{1,3}$$
where:
- $I_{1,2} = 1$ if testing revealed an interference link between $u_1$ and $u_2$, and $0$ otherwise.
- $I_{2,3} = 1$ if testing revealed an interference link between $u_2$ and $u_3$, and $0$ otherwise.
- $I_{1,3} = 1$ if testing revealed an interference link between $u_1$ and $u_3$, and $0$ otherwise.

Your objective is to isolate a subset of exactly three transceivers that is *critically flawed*. A triplet is considered critically flawed if its interference energy $E(x_1, x_2, x_3)$ is exactly $-0.5$ for EVERY valid choice of normalized coefficients $x_1, x_2, x_3$.

## Input
The first line contains the transceiver count $n$ and the interference link count $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each detail a pair of transceivers $u$ and $v$ that share a mutual interference link.
At least one critically flawed subset of three transceivers is guaranteed to exist.

## Output
Provide the labels of the three transceivers forming the subset, printed on a single line as three integers $a$, $b$, and $c$ with $a < b < c$.
Among all valid triples $(a, b, c)$ with $a < b < c$, choose the one with the smallest $a$; if there is a tie, choose the one with the smallest $b$; if there is still a tie, choose the one with the smallest $c$.

## Example 1
### Input
```
4 5
1 2
1 3
2 3
2 4
3 4
```
### Output
```
1 2 3
```

## Example 2
### Input
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
### Output
```
1 2 4
```