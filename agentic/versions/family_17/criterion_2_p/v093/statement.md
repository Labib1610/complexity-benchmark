# Problem B — Symbiotic Habitat Allocation

Time limit: 2 s   Memory limit: 256 MB

## Description
A major conservation initiative aims to preserve a delicate ecosystem consisting of $2q$ species. To ensure their survival, researchers must establish a series of isolated greenhouse habitats. 

Extensive field observations have produced a registry of $t$ viable pairings. You are tasked with finding a valid configuration of habitats. A configuration is defined as any subset of the $t$ documented pairings. Since any pairing can independently be included or excluded, there are $2^t$ theoretical configurations to consider. 

A configuration is deemed valid if and only if it perfectly partitions the full set of species. That is, every single species from $1$ to $2q$ must be present in exactly one pairing within your chosen configuration. No species can be omitted, and no species can be present in more than one active habitat. 

The ecosystem consists of flowers (assigned tags $1$ through $q$) and moths (assigned tags $q+1$ through $2q$). The documented pairings exclusively feature one flower and one moth.

Determine if there is at least one valid configuration in the search space. If one exists, output the chosen pairings. If no such configuration exists, indicate that preservation is impossible.

## Input
The first line provides two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of flower species (which is identical to the number of moth species) and the total number of documented pairings, respectively.

The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating a viable pairing between flower $a$ and moth $b$.

## Output
If a valid configuration is possible, print `YES` on the first line, followed by $q$ lines each containing the two integers of a selected pairing. If no such configuration exists, print `NO`.

## Example

### Input
```
3 5
1 4
1 5
2 5
3 5
3 6
```

### Output
```
YES
1 4
2 5
3 6
```
