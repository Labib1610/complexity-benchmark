# Problem B — Structural Isolation

Time limit: 2 s   Memory limit: 256 MB

## Description
A subterranean archive consists of various vaults connected by passageways. Each passageway requires a certain amount of structural sealant to be permanently barricaded. Two specific vaults have been designated as hazardous zones. To prevent cross-contamination, these two hazardous zones must not be able to communicate through any sequence of unbarricaded passageways. Once a passageway is barricaded, nothing can travel through it in either direction.

Other vaults can remain accessible to either hazardous zone, as long as the two hazardous zones are completely isolated from one another. You are given a strict limit on the total amount of structural sealant available. You must select a set of passageways to barricade such that the total sealant used does not exceed this limit, and the two hazardous zones are mutually inaccessible. If it is impossible to achieve this within the sealant limit, you must state so.

## Input
The first line contains five integers: the number of vaults, the number of passageways, the identifier of the first hazardous vault, the identifier of the second hazardous vault, and the total sealant limit. 
The following lines describe the passageways, one per line. Each line contains three integers: the identifiers of the two vaults it connects, and the amount of sealant required to barricade it. 

## Output
If the isolation can be achieved within the limit, print `YES` on the first line. On the second line, print the number of barricaded passageways, $c$. Then, print $c$ lines, each containing the two vault identifiers of a barricaded passageway. If the limit is strictly exceeded or isolation is impossible, print `NO`.

## Example

**Input**
```text
4 4 1 4 10
1 2 4
1 3 7
2 4 5
3 4 2
```

**Output**
```text
YES
2
1 2
3 4
```
