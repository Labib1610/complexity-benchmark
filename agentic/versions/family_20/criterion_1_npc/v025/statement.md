# Quantum Spin Configurations in Synthetic Molecules

Time limit: 5 s   Memory limit: 256 MB

## Description
You are simulating a synthetic molecule composed of $n$ atoms and $m$ covalent bonds. The molecule is synthesized such that every atom has exactly three bonds connected to it. 

To achieve a stable quantum state, each bond must be assigned one of three possible spin signatures, labeled 1, 2, and 3. The exclusion principle dictates that no two bonds sharing an atom can have the same spin signature. In other words, for every atom, the three bonds attached to it must carry the signatures 1, 2, and 3 in some permutation.

The physical properties of these synthetic molecules dictate that the following conditions are always met:
- The total number of atoms ($n$) is strictly even.
- The total number of bonds ($m$) is always an exact multiple of 3.
- The atoms are indexed with integers from 1 to $n$. For any bond connecting atom $u$ and atom $v$, the sum of their indices ($u+v$) is strictly greater than 2 and strictly less than $2n$.

Given the topology of the molecule, determine if there is a valid assignment of spin signatures to all $m$ bonds. If such an assignment exists, provide one. If it is impossible to satisfy the exclusion principle for all atoms simultaneously, report that it is not possible.

## Input
The first line contains two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u < v \le n$), representing a bond between atom $u$ and atom $v$.

## Output
If a valid spin signature assignment exists, output `YES` on the first line. On the second line, output $m$ integers, each chosen from {1, 2, 3}, representing the spin signature for each bond in the order they were provided in the input. If multiple valid assignments exist, you may output any of them.
If no such assignment is possible, output `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
