# Problem B — Symbiotic Habitat Allocation

Time limit: 2 s   Memory limit: 256 MB

## Description
A major conservation initiative aims to preserve a delicate ecosystem consisting of $2q$ distinct species, identified by sequential tags from $1$ to $2q$.

Researchers have compiled a registry of $t$ potential habitat blueprints. Any subset of these $t$ blueprints could theoretically be chosen. Your system must find a valid subset among all possible combinations. A subset is considered a valid allocation if and only if it perfectly partitions the species collection: every single species from $1$ to $2q$ must appear in exactly one blueprint within the chosen subset. No species can be omitted, and no species can appear in multiple chosen blueprints.

Each blueprint in the registry contains exactly two species. Specifically, every blueprint in the registry pairs one species whose tag is in the range $1 \dots q$ with another species whose tag is in the range $q+1 \dots 2q$. Unlisted combinations cannot be used.

Determine if there exists at least one valid allocation of blueprints that includes all $2q$ species exactly once. If such an allocation exists, output it. Otherwise, indicate that the collection cannot be fully preserved under these conditions.

## Input
The first line provides two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$). The total number of species is $2q$, and $t$ is the number of blueprints in the registry.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a blueprint containing species $a$ and species $b$.

## Output
If a valid allocation is possible, print `YES` on the first line, followed by $q$ lines each containing the two integers of a selected blueprint. If no such allocation exists, print `NO`.

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
