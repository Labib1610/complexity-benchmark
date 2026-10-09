# Crystallization Phase: Molecular Assembler

Time limit: 5 s
Memory limit: 256 MB

## Description
You are programming a molecular assembler to crystallize a new synthetic compound. The reaction chamber contains a substrate with reactive atoms. You are given a target number of tri-bonds to form. The reaction parameters guarantee a perfectly balanced substrate: the total number of atoms is exactly three times the target number of tri-bonds, meaning there are no surplus atoms. Atoms are indexed sequentially starting from 1.

To stabilize the compound, the assembler must trigger the formation of tri-bonds—specialized linkages that connect exactly three atoms simultaneously. A preliminary quantum simulation has generated a comprehensive database of energetically viable tri-bond configurations. Each configuration specifies three distinct atoms that can be successfully linked.

Your task is to program the assembler's laser to activate a specific selection of these configurations. To achieve perfect crystallization, every single atom in the substrate must participate in exactly one tri-bond. Because an atom's valence is fully saturated once it enters a tri-bond, no atom can be part of more than one activated configuration. Notice that due to the perfect balance of the substrate, any valid activation of exactly **q** non-overlapping tri-bonds will automatically fulfill the requirement of saturating the entire substrate without omissions.

Determine if there is a valid selection of tri-bonds from the database that perfectly saturates the substrate. If such a selection exists, output it. If the database does not contain a combination that saturates every atom exactly once, your module must flag this so human operators can adjust the reaction parameters.

## Input
The first line provides two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000). The value **q** is the required number of tri-bonds, establishing a total substrate size of 3q atoms (numbered 1 through 3q). The value **t** represents the total number of viable tri-bond configurations in the database.

Following this, there are **t** lines representing the database. Each line contains three integers a, b, and c (1 ≤ a < b < c ≤ 3q), specifying the indices of three atoms that can form a tri-bond.

## Output
If perfect crystallization is possible, print `YES` on the first line. Then, print **q** lines, each containing the three atom indices of one of the activated tri-bonds. 
If it is impossible to saturate all atoms exactly once using the provided configurations, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
