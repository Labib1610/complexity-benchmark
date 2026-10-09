# Industrial Gas Mixing Network

Time limit: 5 s   Memory limit: 256 MB

## Description
A chemical plant features a network of mixing vats connected by sealed tubes. The design is strictly uniform: every mixing vat is equipped with exactly three tube ports, and every tube connects exactly two vats.

The plant produces a specialized compound that requires the interaction of three distinct reactive gases. Each tube in the network must be permanently filled with exactly one of these three gases (labeled 1, 2, and 3). Because a tube connects two vats, filling a tube with a specific gas exposes both of those vats to that gas.

To achieve the correct reaction equilibrium, every single vat must have access to all three gases. This means the three tubes connected to any given vat must each contain a different gas. If a vat is exposed to two or more tubes containing the same gas, the local mixture will be unbalanced and the reaction will fail.

The structural layout of the vats and tubes is fixed. Your task is to determine whether it is possible to assign one of the three gases to each tube such that every vat is exposed to exactly one tube of gas 1, one tube of gas 2, and one tube of gas 3. If it is possible, provide the gas assignment for each tube.

## Input
The first line contains two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of vats and the number of tubes respectively.
Each of the following **m** lines contains two integers u and v (1 ≤ u < v ≤ n), indicating a tube connecting vat u and vat v.

## Output
If a valid gas assignment exists, print `YES` on the first line. On the second line, print **m** integers from the set {1, 2, 3} separated by spaces, representing the gas assigned to each tube in the order they were given in the input. If no such assignment is possible, print `NO`.

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
