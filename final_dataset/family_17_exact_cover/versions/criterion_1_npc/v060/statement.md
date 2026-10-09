# Problem A — Museum Display Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description
An archaeological dig has yielded a collection of unique artifact fragments. The museum plans to construct exactly **q** display pieces from these fragments. Each display piece must be assembled from exactly three fragments, meaning the total number of fragments involved is 3**q**, uniquely numbered from 1 to 3**q**.

The museum director's strict policy dictates that every single excavated fragment must be exhibited. Furthermore, since the fragments are physical objects, a fragment cannot be part of more than one display piece.

Based on fracture patterns, the restoration team has compiled a catalog of valid three-fragment assemblies. Display pieces can only be built if their exact three-fragment combination appears in this catalog. A fragment may be listed in multiple potential assemblies within the catalog, but it can only be physically used once.

You must determine if a selection of the cataloged assemblies can be chosen to build the **q** display pieces such that every fragment from 1 to 3**q** is used exactly once. If it is possible, output the chosen assemblies. (Note that the mere count of cataloged assemblies says nothing: an extensive catalog can still fail to satisfy the requirement, and a bare-minimum list can still succeed.)

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000), where **q** is the number of display pieces to build and **t** is the number of valid assemblies in the catalog.
Each of the following **t** lines contains three integers a, b, and c (1 ≤ a < b < c ≤ 3q), representing the fragment numbers that form a valid assembly.

## Output
If a valid selection exists, print `YES`, then **q** lines each with the three fragment numbers of one chosen assembly.
Otherwise print `NO`.

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
